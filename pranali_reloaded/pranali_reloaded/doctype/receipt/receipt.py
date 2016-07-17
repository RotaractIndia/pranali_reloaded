# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Receipt(Document):
	def on_submit(self):
		if self.credit_amount:
			balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
			frappe.db.set_value("Club", self.club, "balance_amount", balance_amount + self.amount)
		
		total_amount = frappe.db.get_value("Club", self.club, "total_amount")
		frappe.db.set_value("Club", self.club, "total_amount", total_amount + self.amount)
		
	def on_cancel(self):
		if self.credit_amount:
			balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
			frappe.db.set_value("Club", self.club, "balance_amount", balance_amount - self.amount)
		
		total_amount = frappe.db.get_value("Club", self.club, "total_amount")
		frappe.db.set_value("Club", self.club, "total_amount", total_amount - self.amount)
		