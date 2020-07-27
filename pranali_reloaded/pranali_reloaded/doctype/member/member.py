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

	def on_trash(self):
		club = frappe.get_doc("Club", self.club)
		district_dues = flt(frappe.db.get_single_value("Pranali Settings", "membership_dues"))
		frappe.db.set_value('Club', self.club, 'amount_spent_from_wallet', club.amount_spent_from_wallet - district_dues)
		frappe.db.set_value('Club', self.club, 'balance_amount', club.balance_amount + district_dues)
		frappe.db.set_value('Club', self.club, 'members_registered', club.members_registered - 1)