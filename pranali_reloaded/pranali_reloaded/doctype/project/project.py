# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document

class Project(Document):
	def validate(self):
		self.calculate_totals()
		
	def calculate_totals(self):
		self.total = self.home_club + self.other_club + self.dcm \
			+ self.alumini + self.rotarians + self.pis + self.guest
