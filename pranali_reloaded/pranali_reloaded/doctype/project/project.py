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
		self.calculate_totals()
		self.set_zone()
		self.document_status='draft'
		self.rotaract_year = frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")

	def on_submit(self):
		self.validate_account()
		self.validate_reporting_access()
		frappe.db.set_value('Project', self.name, 'document_status', 'submitted')

	def on_cancel(self):
		frappe.db.set_value('Project', self.name, 'document_status', 'cancelled')

	def set_status(self):
		self.time_stamp = now()
		self.reporting_month = getdate(self.end_time).strftime("%B")
		d = add_months(getdate(self.end_time), 1)
		early = frappe.db.get_single_value("Pranali Settings", "early_reporting_days")
		reporting_deadline = frappe.db.get_single_value("Pranali Settings", "reporting_deadline")
		deadline = cstr(getdate(d).strftime("%Y")) + "-" + cstr(getdate(d).strftime("%m")) + "-" + cstr(reporting_deadline)
		if getdate(self.time_stamp) > getdate(deadline):
			self.project_status = "Late"
		elif early > 0 and getdate(self.time_stamp) <= getdate(add_days(getdate(self.end_time), early)):
			self.project_status = "Early"
		else:
			self.project_status = "On Time"

		if self.reporting_month in ["July", "August", "September"]:
			self.quarter = "One"
		elif self.reporting_month in ["October", "November", "December"]:
			self.quarter = "Two"
		elif self.reporting_month in ["January", "February", "March"]:
			self.quarter = "Three"
		elif self.reporting_month in ["April", "May", "June"]:
			self.quarter = "Four"

	def calculate_totals(self):
		self.total = cint(self.home_club) + cint(self.other_club) + cint(self.dcm) \
			+ cint(self.alumini) + cint(self.rotarians) + cint(self.pis) + cint(self.guest) + cint(self.other_district) 

	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")

	def validate_date(self):
		if self.end_time > now():
			frappe.throw("Did you fix the Flux Capacitor ? \n Project End Time is Greater than today.")

		if self.start_time > self.end_time:
			frappe.throw("Start Time cannot be greater than End Time.")

	def validate_account(self):
		balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
		if balance_amount < 0:
			frappe.throw("Your account has been locked due to Negative funds in your wallet. Please pay INR {0} to Unlock !".format(abs(balance_amount)))

	def validate_reporting_access(self):
		if frappe.db.get_value("Club", self.club, "disable_reporting_access"):
			frappe.throw("Reporting Access has been disabled for your club. Please contact the District Secretary.")