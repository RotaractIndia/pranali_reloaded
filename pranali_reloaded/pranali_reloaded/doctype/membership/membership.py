# -*- coding: utf-8 -*-
# Copyright (c) 2021, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import today, flt
from frappe.model.document import Document

class Membership(Document):
	def validate(self):
		self.valid_from = frappe.utils.today()
		self.rotaract_year = frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")
		self.valid_till = frappe.db.get_value("Rotaract Year", self.rotaract_year, "end_date")
		self.membership_amount = flt(frappe.db.get_single_value("Pranali Settings", "membership_dues"))
		
	def before_submit(self):
		self.validate_funds()

	def on_submit(self):
		self.update_member(True)
		self.update_club()
		
	def validate_funds(self):
		balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
		if balance_amount < self.membership_amount:
			frappe.throw("Insufficient funds! You cannot add a new Member")

	def update_member(self, dues_paid):
		member = frappe.get_doc("Member", self.member)
		member.dues_paid = dues_paid
		if dues_paid:
			member.membership_valid_till = self.valid_till
			member.status = "Active Rotaractor"
			frappe.msgprint("Membership is renewed till {0}.".format(self.valid_till))
		else:
			member.membership_valid_till = None
			frappe.msgprint("Membership Revoked")
		member.save()
	
	def update_club(self):
		frappe.get_doc("Club", self.club).save()
		
	def on_cancel(self):
		self.update_member(False)
		club = frappe.get_doc("Club", self.club)
		district_dues = flt(frappe.db.get_single_value("Pranali Settings", "membership_dues"))
		frappe.db.set_value('Club', self.club, 'amount_spent_from_wallet', club.amount_spent_from_wallet - district_dues)
		frappe.db.set_value('Club', self.club, 'balance_amount', club.balance_amount + district_dues)
		frappe.db.set_value('Club', self.club, 'members_registered', club.members_registered - 1)
