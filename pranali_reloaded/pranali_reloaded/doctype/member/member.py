# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Member(Document):
	def validate(self):
		self.set_zone()
		self.validate_dues()
		self.member_name = self.member_name.title()
		
	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")
		
	def validate_dues(self):
		if not self.dues_paid and self.is_new():
			balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
			if balance_amount < 50:
				frappe.throw("You cannot add a new Member")
			else:
				self.dues_paid = 1
				rotaract_year=frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")
				self.set("year", [{"rotaract_year": rotaract_year, "membership_status":"District Dues Paid"}])
				frappe.db.set_value("Club", self.club, "balance_amount", balance_amount - 70)
				members_registered = frappe.db.get_value("Club", self.club, "members_registered")
				frappe.db.set_value("Club", self.club, "members_registered", members_registered + 1 )

	def on_trash(self):
		if self.dues_paid:
			balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
			frappe.db.set_value("Club", self.club, "balance_amount", balance_amount + 70)
			members_registered = frappe.db.get_value("Club", self.club, "members_registered")
			frappe.db.set_value("Club", self.club, "members_registered", members_registered - 1 )

@frappe.whitelist()
def register_member(member_name):
	member = frappe.get_doc("Member", member_name)
	if not member.dues_paid:
		balance_amount = frappe.db.get_value("Club", member.club, "balance_amount")
		if balance_amount < 50:
			frappe.throw("You cannot add a new Member")
		else:
			member.dues_paid = 1
			rotaract_year=frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")
			member.append("year", dict(rotaract_year= rotaract_year, membership_status= "District Dues Paid" ))
			frappe.db.set_value("Club", member.club, "balance_amount", balance_amount - 70)
			members_registered = frappe.db.get_value("Club", member.club, "members_registered")
			frappe.db.set_value("Club", member.club, "members_registered", members_registered + 1 )
			member.save()
			return True
	else:
		frappe.throw("Already Registered")