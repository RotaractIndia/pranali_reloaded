# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import now
from frappe.model.document import Document

class AmbassadorialReport(Document):
	def validate(self):
		self.set_zone()
		self.document_status='draft'
		self.check_duplicates()
		self.count_total()

	def on_submit(self):
		self.time_stamp = now()
		frappe.db.set_value('Ambassadorial Report', self.name, 'document_status', 'submitted')
	
	def on_cancel(self):
		frappe.db.set_value('Ambassadorial Report', self.name, 'document_status', 'cancelled')

	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")

	def check_duplicates(self):
		members= []
		for d in self.members:
			if not d.member_id in members:
				members.append(d.member_id)
			else:
				frappe.throw("Attendence for {0} appears multiple times.".format(d.member_name))
	
	def count_total(self):
		self.total_attendence = 0
		for d in self.members:
			self.total_attendence +=1