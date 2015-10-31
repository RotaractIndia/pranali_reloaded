# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class OCV(Document):
	def validate(self):
		print "validatng"
		self.set_zone()
		self.calculate_points()
	
	def calculate_points(self):
		self.points = 0
	
	def set_zone(self):
		print self.zone
		self.zone = frappe.db.get_value("Club", self.club, "zone")
	
