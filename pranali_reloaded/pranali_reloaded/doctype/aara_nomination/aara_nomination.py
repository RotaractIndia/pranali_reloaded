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
		ongoing = 0
		flagship = 0 
		nomination_avenue = []
		limits = get_avenue_limit()
		
		if self.quarter == "One":
			nomination_avenue = [ "July", "August", "September"]
		elif self.quarter == "Two":
			nomination_avenue = ["October", "November", "December"]
		elif self.quarter == "Three":
			nomination_avenue = ["January", "February", "March"]
		elif self.quarter == "Four":
			nomination_avenue = ["April", "May"]

		for nomination in self.projects:
			self.validate_reporting_status(nomination)
			
			if nomination.nominate_for == "Ongoing":
				if ongoing==2:
					frappe.throw("You cannot nominate more than 2 ongoing Projects in a quarter")
				else:
					ongoing = ongoing + 1
			elif nomination.nominate_for == "Flagship":
				if flagship==2:
						frappe.throw("You cannot nominate more than 2 flagship Projects in a quarter")
				else:
					flagship = flagship + 1
			else:
				reporting_month = frappe.db.get_value("Project", nomination.project, "reporting_month")
				if reporting_month not in nomination_avenue:
					frappe.throw("You cannot Nominate {0} - {1} for Quarter {2} as it was reported in the month of {3}"
						.format(nomination.project, nomination.project_name, self.quarter, reporting_month))
									
				if nomination.nominate_for == "Joint":
					if joint==2:
							frappe.throw("You cannot nominate more than 2 Joint Projects in a quarter")
					else:
						joint = joint + 1
				else:
					nomination.avenue = frappe.db.get_value("Project", nomination.project, frappe.scrub(nomination.nominate_for))
					if frappe.db.get_value("Project", nomination.project, "joint_project"):
						frappe.throw("You cannot Nominate {0} - {1} since its a Joint Project".format(nomination.project, nomination.project_name))
					
					if not nomination.avenue in avenue_list.keys():
						avenue_list.update({nomination.avenue: 1})
					else:
						if avenue_list.get(nomination.avenue)==limits.get(nomination.avenue):
							frappe.throw("You cannot nominate more that {0} Projects under Avenue {1} for Quarter {2}".format(limits.get(nomination.avenue), nomination.avenue, self.quarter))
						else:
							avenue_list.update({nomination.avenue: 2})

	def before_submit(self):
		existing_nomination = frappe.get_all("AARA Nomination", filters={"Club": self.club, "Quarter": self.quarter, "docstatus": 1})
		if existing_nomination:
			frappe.throw("You have already submitted a Nomination for Quarter {0}. Please cancel {1} to proceed".format(self.quarter, existing_nomination[0].name))

	def validate_reporting_status(self, nomination):
		if frappe.db.get_value("Project", nomination.project, "project_status")== "Late":
				frappe.throw("You cannot nominate project {0} - {1} as it was reported late".format(nomination.project, nomination.project_name))

def get_avenue_limit():
	limits = {}
	for avenue in frappe.get_all("Avenue", fields=["name", "nominations_per_quarter"]):
		limits[avenue.get('name')] = avenue.get('nominations_per_quarter')
	return limits

@frappe.whitelist()
def get_nomination_avenue(project=None, avenue=None):
	return frappe.db.get_value("Project", project, frappe.scrub(avenue))