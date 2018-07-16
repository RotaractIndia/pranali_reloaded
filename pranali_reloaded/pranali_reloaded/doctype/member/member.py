# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt

class Member(Document):
	def validate(self):
		self.set_zone()
		self.validate_dues()
		self.member_name = self.member_name.title()
		
	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")
		
	def validate_dues(self):
		district_dues = flt(frappe.db.get_single_value("Pranali Settings", "membership_dues"))
		if not self.dues_paid:
			balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
			if balance_amount < district_dues:
				frappe.throw("You cannot add a new Member")
			else:
				self.dues_paid = 1
				frappe.db.set_value("Club", self.club, "balance_amount", balance_amount - district_dues)
				members_registered = frappe.db.get_value("Club", self.club, "members_registered")
				frappe.db.set_value("Club", self.club, "members_registered", members_registered + 1 )

	def on_trash(self):
		if self.dues_paid:	
			district_dues = flt(frappe.db.get_single_value("Pranali Settings", "membership_dues"))
			balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
			frappe.db.set_value("Club", self.club, "balance_amount", balance_amount + district_dues)
			members_registered = frappe.db.get_value("Club", self.club, "members_registered")
			frappe.db.set_value("Club", self.club, "members_registered", members_registered - 1 )
