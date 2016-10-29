# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class OCV(Document):
	def validate(self):
		self.points = 0
		print frappe.utils.now()
		if frappe.utils.now() < "2017-03-01":
			self.points = 5000
		if self.gavel:
			self.points += 300
		if self.charter:
			self.points += 1500
		if self.collar:
			self.points += 1000
		if self.saa:
			self.points += 500
		if self.minutes:
			self.points += 750
		if self.attendance:
			self.points += 750
		if self.banner:
			self.points += 500
		if self.rooster:
			self.points += 500
		if self.website:
			self.points += 500
		if self.membership:
			self.points += 1500
		if self.bye_laws:
			self.points += 3000
		if self.finance:
			self.points += 3000
