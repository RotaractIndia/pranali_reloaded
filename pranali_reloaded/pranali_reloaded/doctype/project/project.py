# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint, cstr, now, getdate, add_months, add_days
from frappe.model.document import Document

class Project(Document):
	def validate(self):
		self.validate_date()
		self.set_status()
		self.validate_ambassadorial()
		self.calculate_totals()
		self.set_zone()
		self.document_status='draft'
	
	def on_submit(self):
		frappe.db.set_value('Project', self.name, 'document_status', 'submitted')
		
	def on_cancel(self):
		frappe.db.set_value('Project', self.name, 'document_status', 'cancelled')
		
	def set_status(self):
		self.time_stamp = now()
		self.reporting_month = getdate(self.end_time).strftime("%B")
		d = add_months(getdate(self.end_time), 1)
		deadline = cstr(getdate(d).strftime("%Y")) + "-" + cstr(getdate(d).strftime("%m")) + "-10"
		if getdate(self.time_stamp) > getdate(deadline):
			self.project_status = "Late"
		elif getdate(self.time_stamp) < getdate(add_days(getdate(self.end_time), 10)):
			self.project_status = "Early"
		else:
			self.project_status = "On Time"
	
	def validate_ambassadorial(self):
		if not self.ambassadorial:
			self.other_club=0
	
	def calculate_totals(self):
		self.total = cint(self.home_club) + cint(self.other_club) + cint(self.dcm) \
			+ cint(self.alumini) + cint(self.rotarians) + cint(self.pis) + cint(self.guest)

	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")

	def validate_date(self):
		if self.end_time > now():
			frappe.throw("Did you fix the Flux Capacitor ? \n Project End Time is Greater than today.")
			
		if self.start_time > self.end_time:
			frappe.throw("Start Time cannot be greater than End Time.")
