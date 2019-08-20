# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import add_years
from frappe.model.document import Document
from pranali_reloaded.pranali_reloaded.utils import calculate_wallet_amount

class Club(Document):
	def validate(self):
		wallet_details = calculate_wallet_amount(self.club_name)
		self.total_amount_credited_in_wallet = wallet_details.get("total_amount")
		self.amount_spent_from_wallet = wallet_details.get("amount_spent")
		self.balance_amount = wallet_details.get("balance_amount")
		self.members_registered = wallet_details.get("total_members")

		if not frappe.db.exists("Club List", self.club_name):
			club_list = frappe.new_doc("Club List")
			club_list.club_name = self.club_name
			club_list.save()
