# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import today

class OnlinePayments(Document):
	def validate(self):
		pass

	def on_payment_authorized(self, *args, **kwargs):
			self.db_set('paid', 1)
			self.make_payment_entry()


	def make_payment_entry(self):
		receipt = frappe.new_doc("Receipt")
		receipt.update({
			"club": self.club,
			"receivers_name": self.club,
			"amount": self.amount,
			"receivers_email_id": self.owner,
			"description": " Online Payment ID: " + self.name,
			"date": today(),
			"rotaract_year": frappe.db.get_single_value("Pranali Settings", "current_rotaract_year"),
			"credit_amount": True
		})
		receipt.flags.ignore_permissions = 1
		receipt.save()
		receipt.submit()