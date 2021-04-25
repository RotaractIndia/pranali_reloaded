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

	def before_insert(self):
		self.validate_dues()

	def after_insert(self):
		frappe.get_doc("Club", self.club).save()

	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")

	def validate_dues(self):
		district_dues = flt(frappe.db.get_single_value("Pranali Settings", "membership_dues"))
		balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
		if balance_amount < district_dues:
			frappe.throw("Insufficient funds! You cannot add a new Member")
	
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

	def on_trash(self):
		club = frappe.get_doc("Club", self.club)
		district_dues = flt(frappe.db.get_single_value("Pranali Settings", "membership_dues"))
		frappe.db.set_value('Club', self.club, 'amount_spent_from_wallet', club.amount_spent_from_wallet - district_dues)
		frappe.db.set_value('Club', self.club, 'balance_amount', club.balance_amount + district_dues)
		frappe.db.set_value('Club', self.club, 'members_registered', club.members_registered - 1)