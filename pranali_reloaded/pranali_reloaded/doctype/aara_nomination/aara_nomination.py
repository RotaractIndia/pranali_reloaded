# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class AARANomination(Document):
	def validate(self):
		avenue_list = {}
		joint = 0
		nomination_avenue = []
		if self.quarter == "One":
			nomination_avenue = [ "July", "August", "September"]
		elif self.quarter == "Two":
			nomination_avenue = ["October", "November", "December"]
		elif self.quarter == "Three":
			nomination_avenue = ["January", "February", "March"]
		elif self.quarter == "Four":
			nomination_avenue = ["April", "May"]

		for d in self.projects:
			if frappe.db.get_value("Project", d.project, "project_status")== "Late":
				frappe.throw("You cannot nominate project {0} - {1} as it was reported late".format(d.project, d.project_name))

			reporting_month = frappe.db.get_value("Project", d.project, "reporting_month")
			if reporting_month not in nomination_avenue:
				frappe.throw("You cannot Nominate {0} - {1} for Quarter {2} as it was reported in the month of {3}"
					.format(d.project, d.project_name, self.quarter, reporting_month))
								
			if d.nominate_for == "Joint":

				if joint==2:
					frappe.throw("You cannot nominate more than 2 Joint Projects in a quarter")
				else:
					joint = joint + 1
				
			else:
				d.avenue = frappe.db.get_value("Project", d.project, frappe.scrub(d.nominate_for))
				if frappe.db.get_value("Project", d.project, "joint_project"):
					frappe.throw("You cannot Nominate {0} - {1} since its a Joint Project".format(d.project, d.project_name))
				
				if not d.avenue in avenue_list.keys():
					avenue_list.update({d.avenue: 1})
				else:
					if avenue_list.get(d.avenue)==2:
						frappe.throw("You cannot nominate more that 2 Projects under Avenue {0} for Quarter {1}".format(d.avenue, self.quarter))
					else:
						avenue_list.update({d.avenue: 2})

@frappe.whitelist()
def get_nomination_avenue(project=None, avenue=None):
	return frappe.db.get_value("Project", project, frappe.scrub(avenue))
