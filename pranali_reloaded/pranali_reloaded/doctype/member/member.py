# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import print_function, unicode_literals
import frappe, os
from frappe.model.document import Document
from frappe.utils import get_url, today
from pyqrcode import create as qrcreate

class Member(Document):
	def validate(self):
		self.set_zone()
		self.member_name = self.member_name.title()
		if self.email: self.email = self.email.lower()
		self.validate_status()
		self.validate_pranali_access()
		if not self.qr_code:
			self.verification_hash = frappe.generate_hash(length=20).upper()
			self.qr_code = qrcode_as_png(self.name, self.verification_hash)

	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")
	
	def validate_status(self):
		if self.dues_paid and self.status != "Active Rotaractor":
			self.dues_paid = False
			self.enable_pranali_access = False
			self.in_directory = False
		elif self.membership_valid_till > today():
			self.dues_paid = True

	def validate_pranali_access(self):
		if not self.check_dcm_access():
			if self.user and not self.email:
				self.disable_user()
			elif self.user and self.user != self.email:
				self.rename_user()
			
			if not self.user and self.email and self.enable_pranali_access:
				if not frappe.db.exists("User", self.email):
					self.make_user()
				else:
					self.user = self.email
					self.update_user()
			elif self.user and self.email:
				self.update_user()
		
	def check_dcm_access(self):
		rotaract_year = frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")
		dcm_list = frappe.get_doc("Rotaract Year", rotaract_year)
		for user in dcm_list.district_core_team:
			if user.email == self.email: 
				return True
		for user in dcm_list.district_council:
			if user.email == self.email: 
				return True

	def make_user(self):
		user = frappe.new_doc("User")
		user.update({
			"first_name": self.member_name,
			"email": self.email,
			"mobile_no": self.contact_number,
			"send_welcome_email": 1
		})
		user.save(ignore_permissions=True)
		if self.designation:
			user.bio = self.designation + ', ' + self.club
		else:
			user.bio = self.club		
		user.update({
			"roles": [
				{"role": "Club Member - Limited Access"}
			]
		})
		user.save(ignore_permissions=True)
		self.user = user.name
		self.limited_access=True
		self.restrict_user_to_club()

	def update_user(self):
		user=frappe.get_doc("User", self.user)
		user.enabled=self.enable_pranali_access
		user.email = self.email
		user.mobile_no = self.contact_number
		if self.designation:
			user.bio = self.designation + ', ' + self.club
		else:
			user.bio = self.club		
		if self.limited_access:
			user.update({
				"roles": [
					{"role": "Club Member - Limited Access"}
				]
			})
		else:
			user.update({
				"roles": [
					{"role": "Club Member - Full Access"}
				]
			})
		user.save(ignore_permissions=True)
		if self.enable_pranali_access:
			self.restrict_user_to_club()
		else:
			self.remove_club_restriction()

	def rename_user(self):
		frappe.rename_doc("User", self.user, self.email, ignore_permissions=True)
		self.user = self.email

	def disable_user(self):
		self.enable_pranali_access = False
		user=frappe.get_doc("User", self.user)
		user.enabled=self.enable_pranali_access
		user.save(ignore_permissions=True)
		self.remove_club_restriction()

	def restrict_user_to_club(self):
		user_permissions = frappe.get_all("User Permission", filters={
			"user": self.user, 
			"allow": "Club"
		})
		if not user_permissions:
			permission = frappe.new_doc("User Permission")
			permission.user = self.user
			permission.allow = "Club"
			permission.for_value = self.club
			permission.save(ignore_permissions=True)
	
	def remove_club_restriction(self):
		user_permissions = frappe.get_all("User Permission", filters={
			"user": self.user, 
			"allow": "Club"
		})
		if user_permissions:
			frappe.delete_doc("User Permission", user_permissions[0].name, ignore_permissions=True)

def qrcode_as_png(member, verification_hash):
	site_name = frappe.db.get_single_value("Pranali Settings", "site_name")
	qr_data = site_name + '/verify?id=' + verification_hash
	folder = create_barcode_folder()
	png_file_name = '{}.png'.format(verification_hash)
	_file = frappe.get_doc({
		"doctype": "File",
		"file_name": png_file_name,
		"attached_to_doctype": 'Member',
		"attached_to_name": member,
		"folder": folder,
		"content": png_file_name})
	_file.save()
	frappe.db.commit()
	file_url = get_url(_file.file_url)
	file_path = os.path.join(frappe.get_site_path('public', 'files'), _file.file_name)
	url = qrcreate(qr_data)
	with open(file_path, 'wb') as png_file:
		url.png(png_file, scale=3, module_color=[0, 0, 0, 180])
	return file_url

def create_barcode_folder():
	'''Get Barcodes folder.'''
	folder_name = 'Barcodes'
	folder = frappe.db.exists('File', {'file_name': folder_name})
	if folder:
		return folder
	folder = frappe.get_doc({
			'doctype': 'File',
			'file_name': folder_name,
			'is_folder':1,
			'folder': 'Home'
		})
	folder.insert(ignore_permissions=True)
	return folder.name

@frappe.whitelist()
def pay_dues(member_id):
	membership = frappe.new_doc("Membership")
	membership.member = member_id
	membership.save()
	membership.submit()