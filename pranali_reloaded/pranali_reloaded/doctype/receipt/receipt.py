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
		if self.club and self.credit_amount:
			frappe.get_doc("Club", self.club).save()

	def on_cancel(self):
		if self.club and self.credit_amount:
			frappe.get_doc("Club", self.club).save()
