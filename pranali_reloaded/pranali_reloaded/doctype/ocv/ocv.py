# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class OCV(Document):
	def validate(self):
		self.set_zone()
		self.calculate_points()
	
	def calculate_points(self):
		self.points = 0
		
		if self.insti_date:
			if self.insti_date <= "2015-08-31":
				self.points += 500
			else:
				self.points += 250
		
		if self.insti_att and self.insti_att > 100:
			self.points += 500
		
		if self.gavel_gong:
			self.points += 300
			
		if self.charter:
			self.points += 1500
			
		if self.collar:
			self.points += 1000
			
		if self.saa_arm_band:
			self.points += 500
			
		if self.minutes_book:
			self.points += 750
			
		if self.attendence_muster:
			self.points += 750
			
		if self.banner:
			self.points += 500
			
		if self.rooster:
			self.points += 500
			
		if self.website:
			self.points += 500
			
		if self.membership_file:
			self.points += 1500
		
		if self.by_laws:
			self.points += 3000
			
		if self.financial_accounts:
			self.points += 3000
			
		if nowdate() <= "2016-03-31":
			self.points += 5000
	
	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")
	
