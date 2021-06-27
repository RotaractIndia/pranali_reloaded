# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, os
from frappe.model.document import Document
from frappe.utils import get_url
from pyqrcode import create as qrcreate

class Member(Document):
	def validate(self):
		self.set_zone()
		self.validate_pranali_access()
		self.member_name = self.member_name.title()
		if not self.qr_code:
			self.verification_hash = frappe.generate_hash(length=20).upper()
			self.qr_code = qrcode_as_png(self.name, self.verification_hash)

	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")
	
	def validate_pranali_access(self):
		if self.user and not self.email:
			self.disable_user()
		elif self.user and self.user != self.email:
			self.rename_user()
		
		if not self.user and self.email and self.enable_pranali_access:
			if not frappe.db.exists("User", self.email):
				self.make_user()
			else:
				self.user = self.email
		elif self.user and self.email:
			self.update_user()
		
	def make_user(self):
		user = frappe.new_doc("User")
		user.update({
			"first_name": self.member_name,
			"email": self.email,
			"mobile_no": self.contact_number,
			"send_welcome_email": 1
		})
		user.save(ignore_permissions=True)
		user.update({
			"roles": [
				{"role": "Club Member - Limited Access"}
			],
			"bio": self.club
		})
		user.save(ignore_permissions=True)
		self.user = user.name
		self.limited_access=True
		permission = frappe.new_doc("User Permission")
		permission.user = user.name
		permission.allow = "Club"
		permission.for_value = self.club
		permission.save(ignore_permissions=True)

	def update_user(self):
		user=frappe.get_doc("User", self.user)
		user.enabled=self.enable_pranali_access
		user.email = self.email
		user.mobile_no = self.contact_number
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

	def rename_user(self):
		frappe.rename_doc("User", self.user, self.email)
		self.user = self.email

	def disable_user(self):
		self.enable_pranali_access = False
		user=frappe.get_doc("User", self.user)
		user.enabled=self.enable_pranali_access
		user.save(ignore_permissions=True)
		self.user = None

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