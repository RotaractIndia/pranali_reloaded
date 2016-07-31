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

def get_timeline_data(doctype, name):
	'''returns timeline data for the past one year'''
	from frappe.desk.form.load import get_communication_data
	data = get_communication_data(doctype, name,
		fields = 'unix_timestamp(date(creation)), count(name)',
		after = add_years(None, -1).strftime('%Y-%m-%d'),
		group_by='group by date(creation)', as_dict=False)
	return dict(data)