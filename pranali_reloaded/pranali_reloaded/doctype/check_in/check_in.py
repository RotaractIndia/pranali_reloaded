# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CheckIn(Document):
	def get_details(self):
		if not self.code:
			return
		self.member_name = self.club = self.zone = None
		if len(self.code) == 4:
			d = frappe.db.sql("select member_name, club, zone, checked_in from `tabCode List` where code=%s", self.code, as_dict=1)
		else:
			d = frappe.db.sql("select member_name, club, zone, checked_in from `tabOTS Code List` where code=%s", self.code, as_dict=1)
			self.is_ots = 1
		if not d:
			frappe.throw("Invalid Code")
		elif d[0].checked_in:
			frappe.throw("Already Checked In")
		else:
			self.member_name = d[0].member_name
			self.club = d[0].club
			self.zone = d[0].zone
			
	def check_in(self):
		if not self.is_ots:
			if self.member_name == frappe.db.get_value("Code List", self.code, "member_name"):
				if not frappe.db.get_value("Code List", self.code, "checked_in"):
					frappe.db.set_value("Code List", self.code, "checked_in", 1)
					frappe.msgprint("Check in Successful")
				else:
					frappe.throw("Already Checked In")
			else:
				frappe.throw("Data Mismatch - Please try again")
				
		else:
			name = frappe.db.sql("select name from `tabOTS Code List` where code=%s", self.code)[0][0]
			if self.member_name == frappe.db.get_value("OTS Code List", name, "member_name"):
				if not frappe.db.get_value("OTS Code List", name, "checked_in"):
					frappe.db.set_value("OTS Code List", name, "checked_in", 1)
					frappe.msgprint("OTS Check in Successful. Please Collect Rs.200/-")
				else:
					frappe.throw("Already Checked In")
			else:
				frappe.throw("Data Mismatch - Please try again")