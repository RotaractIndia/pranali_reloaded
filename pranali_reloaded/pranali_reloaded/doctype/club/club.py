# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import add_years
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from pranali_reloaded.pranali_reloaded.utils import calculate_wallet_amount

class Club(Document):
	def validate(self):
		wallet_details = calculate_wallet_amount(self.club_name)
		self.total_amount_credited_in_wallet = wallet_details.get("total_amount")
		self.amount_spent_from_wallet = wallet_details.get("amount_spent")
		self.balance_amount = wallet_details.get("balance_amount")
		self.members_registered = wallet_details.get("total_members")
		self.set_board_of_directors()
		
	def set_board_of_directors(self):
		bod = frappe.get_all("Member", filters={
			"designation": ["is", "set"],
			"designation": ["!=", "General Body Member"],
			"dues_paid": True,
			"club": self.name
		})
		self.board_of_directors = len(bod)

def get_timeline_data(doctype, name):
	project_data = dict(frappe.db.sql('''select unix_timestamp(date(end_time)), count(*)
		from `tabProject` where club=%s
			and end_time > date_sub(curdate(), interval 1 year)
			and docstatus < 2
			group by date(end_time)''', name))

	meeting_data = dict(frappe.db.sql('''select unix_timestamp(date), count(*)
		from `tabMeeting` where club=%s
			and date > date_sub(curdate(), interval 1 year)
			and docstatus < 2
			group by date(date)''', name))

	heatmap_data = merge_dicts(project_data, meeting_data)
	return heatmap_data

def merge_dicts(dict1, dict2):
	''' Merge dictionaries and add values of common keys'''
	dict3 = {**dict1, **dict2}
	for key, value in dict3.items():
		if key in dict1 and key in dict2:
			dict3[key] = value + dict1[key]
	return dict3

@frappe.whitelist()
def pay_district(source_name, target_doc=None):
	doc = get_mapped_doc("Club", source_name, {
		"Club": {
			"doctype": "District Payments",
			"field_map":{
				"name" : "club"
			}
		},
	}, target_doc)

	return doc