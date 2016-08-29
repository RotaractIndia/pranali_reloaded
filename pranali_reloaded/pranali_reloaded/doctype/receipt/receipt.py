# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import now

class Receipt(Document):
	def validate(self):
		if not self.club:
			self.title = self.receivers_name
			
	def on_submit(self):
		self.date = now()
		if self.club:
			if self.credit_amount:
				balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
				frappe.db.set_value("Club", self.club, "balance_amount", balance_amount + self.amount)
		
			total_amount = frappe.db.get_value("Club", self.club, "total_amount")
			frappe.db.set_value("Club", self.club, "total_amount", total_amount + self.amount)
		
	def on_cancel(self):
		if self.club:
			if self.credit_amount:
				balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
				frappe.db.set_value("Club", self.club, "balance_amount", balance_amount - self.amount)
		
			total_amount = frappe.db.get_value("Club", self.club, "total_amount")
			frappe.db.set_value("Club", self.club, "total_amount", total_amount - self.amount)
		