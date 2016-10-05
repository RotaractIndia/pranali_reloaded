# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Member(Document):
	def validate(self):
		self.set_zone()
		self.validate_dues()
		
	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")
		
	def validate_dues(self):
		if not self.dues_paid:
			balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
			if balance_amount < 50:
				frappe.throw("You cannot add a new Member")
			else:
				self.dues_paid = 1
				frappe.db.set_value("Club", self.club, "balance_amount", balance_amount - 50)
				members_registered = frappe.db.get_value("Club", self.club, "members_registered")
				frappe.db.set_value("Club", self.club, "members_registered", members_registered + 1 )

	def on_trash(self):
		if self.dues_paid:
			balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
			frappe.db.set_value("Club", self.club, "balance_amount", balance_amount + 50)
			members_registered = frappe.db.get_value("Club", self.club, "members_registered")
			frappe.db.set_value("Club", self.club, "members_registered", members_registered - 1 )
		