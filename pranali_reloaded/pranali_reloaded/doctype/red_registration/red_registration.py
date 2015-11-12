# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class REDRegistration(Document):
	def validate(self):
		self.single_day = 0
		self.both_days = 0
		for d in self.members:
			d.member_name = frappe.db.get_value("Member", d.member, "member_name")
			if d.day1 and d.day2:
				self.both_days +=1
			elif d.day1 or d.day2:
				self.single_day +=1
			else:
				frappe.throw("Please select Day 1 or Day 2 for Member {0}".format(d.member_name))
		self.single_day_amount = self.single_day * 70
		self.both_days_amount = self.both_days * 100
		self.total_amount = self.single_day_amount + self.both_days_amount
		
		self.zone = frappe.db.get_value("Club", self.club, "zone")