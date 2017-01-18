# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DCRegistrations(Document):
	def validate(self):
		if self.nightout:
			if self.dcm:
				self.amount = 300
			else:
				self.amount = 400
		else:
			self.amount = 100
		
	def on_payment_authorized(self, *args, **kwargs):
			self.db_set('paid', 1)
			self.db_set('docstatus', 1)
			frappe.get_doc('Email Alert', "DC Ticket").send(self)