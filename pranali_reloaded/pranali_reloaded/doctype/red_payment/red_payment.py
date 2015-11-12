# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class REDPayment(Document):
	def validate(self):
		if not self.amount == frappe.db.get_value("RED Registration", self.red_registration, "total_amount"):
			frappe.throw("Incorrect Amount")
	
	def on_submit(self):
		frappe.db.set_value("RED Registration", self.red_registration, "status", "Paid")
