# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import add_years
from frappe.model.document import Document

class Club(Document):
	def validate(self):
		if not frappe.db.exists("Club List", self.club_name):
			club_list = frappe.new_doc("Club List")
			club_list.club_name = self.club_name
			club_list.save()