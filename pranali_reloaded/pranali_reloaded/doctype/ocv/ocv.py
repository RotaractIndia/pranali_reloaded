# -*- coding: utf-8 -*-
# Copyright (c) 2020, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class OCV(Document):
	def validate(self):
		rules = ['gavel', 'charter', 'collar', 'saa', 'minutes', 'attendance', 
			'banner', 'rooster', 'website', 'membership', 'bye_laws', 'finance']
		
		rule_points = frappe.get_single("OCV Points Configuration")
		self.max_points = rule_points.max_points
		self.points = 0

		if self.ocv_date < rule_points.cut_off_date:
			self.points += rule_points.additional_points
		
		for rule in rules:
			if self.get(rule):
				self.points += rule_points.get(rule)

		self.percentage_points_earned = (self.points/self.max_points) * 100