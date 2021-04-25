# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt

class Member(Document):
	def validate(self):
		self.set_zone()
		self.validate_pranali_access()
		self.member_name = self.member_name.title()

	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")
	
	def validate_pranali_access(self):
		if not self.email:
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

@frappe.whitelist()
def pay_dues(member_id):
	membership = frappe.new_doc("Membership")
	membership.member = member_id
	membership.save()
	membership.submit()