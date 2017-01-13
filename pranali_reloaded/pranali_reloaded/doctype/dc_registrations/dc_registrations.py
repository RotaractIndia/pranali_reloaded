# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DCRegistrations(Document):
	def validate(self):
		print "Call"
		if self.nightout:
			if self.dcm:
				self.amount = 350
			else:
				self.amount = 450
		else:
			self.amount = 100
		
