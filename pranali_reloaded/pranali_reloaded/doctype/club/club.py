# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Club(Document):
	def validate(self):
		if not frappe.db.exists("Club List", self.club_name):
			club_list = frappe.new_doc("Club List")
			club_list.club_name = self.club_name
			club_list.save()

@frappe.whitelist()
def update_statistics(club):
	members = frappe.db.sql("select count(name) from `tabMember` where club= %s", club)
	meetings = frappe.db.sql("select count(name) from `tabMeeting` where club= %s", club)
	projects = frappe.db.sql("select count(name) from `tabProject` where club= %s", club)
	ambassodorial_reports = frappe.db.sql("select count(name) from `tabAmbassadorial Report` where club= %s", club)
	frappe.db.sql("update `tabClub` set members= %s, meetings= %s, projects= %s, \
		ambassadorial_reports= %s where name= %s", (members, meetings, projects, ambassodorial_reports, club))
	