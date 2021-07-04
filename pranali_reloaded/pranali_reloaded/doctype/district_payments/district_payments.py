# -*- coding: utf-8 -*-
# Copyright (c) 2021, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DistrictPayments(Document):
	def before_submit(self):
		self.validate_funds()

	def on_submit(self):
		self.update_club()

	def on_cancel(self):
		self.update_club()
		
	def validate_funds(self):
		balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
		if balance_amount < self.grand_total:
			frappe.throw("Insufficient funds! Please add funds to your Pranali wallet to proceed.")

	def update_club(self):
		frappe.get_doc("Club", self.club).save()

