# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt

class Member(Document):
	def validate(self):
		self.set_zone()
		self.member_name = self.member_name.title()

	def after_insert(self):
		self.validate_dues()
		frappe.get_doc("Club", self.club).save()
	
	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")
		
	def validate_dues(self):
		district_dues = flt(frappe.db.get_single_value("Pranali Settings", "membership_dues"))
		balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
		if balance_amount < district_dues:
			frappe.throw("Insufficient funds! You cannot add a new Member")

	def on_trash(self):
		frappe.get_doc("Club", self.club).save()