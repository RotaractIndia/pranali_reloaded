# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class AmbassadorialReport(Document):
	def validate(self):
		self.set_zone()
		self.document_status='draft'

	def on_submit(self):
		frappe.db.set_value('Ambassadorial Report', self.name, 'document_status', 'submitted')
	
	def on_cancel(self):
		frappe.db.set_value('Ambassadorial Report', self.name, 'document_status', 'cancelled')

	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")
