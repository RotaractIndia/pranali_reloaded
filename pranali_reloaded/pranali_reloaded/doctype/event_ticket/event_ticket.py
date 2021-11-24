# -*- coding: utf-8 -*-
# Copyright (c) 2021, Rtr. Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class EventTicket(Document):
	def validate(self):
		self.convenience_fee = self.event_cost * 0.02
		self.grand_total = self.event_cost * 1.02

	def on_payment_authorized(self, *args, **kwargs):
		self.db_set('paid', 1)
		self.flags.ignore_permissions = 1
		self.save()
		self.submit()

