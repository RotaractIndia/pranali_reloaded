# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import today

class Receipt(Document):
	def validate(self):
		self.date = today()
		self.rotaract_year = frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")
	
	def on_submit(self):
		if self.club and self.credit_amount:
			frappe.get_doc("Club", self.club).save()

	def on_cancel(self):
		if self.club and self.credit_amount:
			frappe.get_doc("Club", self.club).save()
