# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class AmbassadorialReport(Document):
	def validate(self):
		self.set_zone()

	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")

@frappe.whitelist()
def get_member_name(id):
	return frappe.db.get_value("Member", id, "member_name")