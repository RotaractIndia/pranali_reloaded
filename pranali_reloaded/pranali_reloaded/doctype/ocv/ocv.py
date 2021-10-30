# -*- coding: utf-8 -*-
# Copyright (c) 2020, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint
from frappe.model.document import Document

class OCV(Document):
	def validate(self):
		self.rotaract_year = frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")
		self.validate_club()
		self.set_points()

	def validate_club(self):
		rotaract_year = frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")
		self.existing_ocv = frappe.get_all("OCV", filters={"club": self.club, 'docstatus':1, 'rotaract_year': rotaract_year})
		if self.existing_ocv:
			frappe.throw("OCV Record is already created for Club {0}. <a href='/desk#Form/OCV/{1}'>Please cancel {1} to proceed.</a>".format(self.club, self.existing_ocv[0].get('name')))

	def set_points(self):
		rules = ['gavel', 'charter', 'collar', 'saa', 'minutes', 'attendance', 
			'banner', 'rooster', 'website', 'membership', 'bye_laws', 'finance']
		
		rule_points = frappe.get_single("OCV Points Configuration")
		self.max_points = rule_points.max_points
		self.points = 0

		if rule_points.cut_off_date and self.ocv_date < rule_points.cut_off_date:
			self.points += rule_points.additional_points
		
		for rule in rules:
			if self.get(rule):
				self.points += rule_points.get(rule)
		
		for custom_rule in rule_points.custom_ocv_points:
			if self.get(custom_rule.field_name):
				self.points += cint(custom_rule.points)

		self.percentage_points_earned = (self.points/self.max_points) * 100