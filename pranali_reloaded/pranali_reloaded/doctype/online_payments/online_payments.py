# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class OnlinePayments(Document):
	def validate(self):
		pass

	def on_payment_authorized(self, *args, **kwargs):
			self.db_set('paid', 1)
			total_amount_credited_in_wallet = frappe.db.get_value("Club", self.club, "total_amount_credited_in_wallet")
			frappe.db.set_value("Club", self.club, "total_amount_credited_in_wallet", total_amount_credited_in_wallet + self.amount)
			balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
			frappe.db.set_value("Club", self.club, "balance_amount", balance_amount + self.amount)
