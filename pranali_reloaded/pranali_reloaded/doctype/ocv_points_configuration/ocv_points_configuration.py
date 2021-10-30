# -*- coding: utf-8 -*-
# Copyright (c) 2020, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class OCVPointsConfiguration(Document):
	def validate(self):
		rules = ['gavel', 'charter', 'collar', 'saa', 'minutes', 'attendance', 
			'banner', 'rooster', 'website', 'membership', 'bye_laws', 'finance', 'additional_points']
		
		self.max_points = 0

		for rule in rules:
			self.max_points += self.get(rule)

		for custom_points in self.custom_ocv_points:
			self.max_points += custom_points.points
