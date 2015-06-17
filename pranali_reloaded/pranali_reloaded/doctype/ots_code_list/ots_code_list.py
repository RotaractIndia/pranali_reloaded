# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import random
import string
from frappe.model.document import Document

class OTSCodeList(Document):
	def validate(self):
		if self.checked_in:
			frappe.throw("Already Checked In.")
		if self.code:
			frappe.msgprint("Your Code is: {0}".format(self.code))
		else:
			self.code = random_char(5)
			frappe.msgprint("Your Code is: {0}".format(self.code))

def random_char(y):
       return ''.join(random.choice(string.ascii_uppercase) for x in range(y))