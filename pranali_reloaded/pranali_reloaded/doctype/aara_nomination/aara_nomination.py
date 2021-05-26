# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class AARANomination(Document):
	def validate(self):
		avenue_list = {}
		nomination_avenue = []
		self.rotaract_year = frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")
		limits = get_avenue_limit()
		yearly_limits = get_yearly_limit()
		joint_limit = frappe.db.get_single_value("Pranali Settings", "joint_project_limit")

		if self.quarter == "Yearly":
			self.projects = []
			print(self.projects)
		else:
			self.yearly_nomination = []
		
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
			reporting_month = frappe.db.get_value("Project", nomination.project, "reporting_month")
			if reporting_month not in nomination_avenue:
				frappe.throw("You cannot Nominate {0} - {1} for Quarter {2} as it was reported in the month of {3}"
					.format(nomination.project, nomination.project_name, self.quarter, reporting_month))
						
			if nomination.nominate_for == "Joint":
				self.validate_joint_project(nomination.project)
				avenue_list.update({"Joint": avenue_list.get("Joint", 0) +1})
				if avenue_list.get("Joint")>joint_limit:
						frappe.throw("You cannot nominate more than 2 Joint Projects in a quarter")
			else:
				nomination.avenue = frappe.db.get_value("Project", nomination.project, frappe.scrub(nomination.nominate_for))
				if frappe.db.get_value("Project", nomination.project, "joint_project"):
					frappe.throw("You cannot Nominate {0} - {1} since its a Joint Project".format(nomination.project, nomination.project_name))
				
				avenue_list.update({nomination.avenue: avenue_list.get(nomination.avenue, 0) +1})
				if avenue_list.get(nomination.avenue)>limits.get(nomination.avenue):
					frappe.throw("You cannot nominate more that {0} Projects under Avenue {1} for Quarter {2}".format(limits.get(nomination.avenue), nomination.avenue, self.quarter))					

		for nomination in self.yearly_nomination:
			self.validate_reporting_status(nomination)
			avenue_list.update({nomination.nomination_category: avenue_list.get(nomination.nomination_category, 0) +1})
			if avenue_list.get(nomination.nomination_category)>yearly_limits.get(nomination.nomination_category):
				frappe.throw("You cannot nominate more that {0} Projects under Nomination Category {1}".format(yearly_limits.get(nomination.nomination_category), nomination.nomination_category))
	
	def before_submit(self):
		rotaract_year = frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")
		existing_nomination = frappe.get_all("AARA Nomination", filters={"Club": self.club, "Quarter": self.quarter, "docstatus": 1, "rotaract_year": rotaract_year})
		if existing_nomination:
			frappe.throw("You have already submitted a Nomination for Quarter {0}. Please cancel {1} to proceed".format(self.quarter, existing_nomination[0].name))

	def validate_reporting_status(self, nomination):
		if frappe.db.get_value("Project", nomination.project, "project_status")== "Late":
				frappe.throw("You cannot nominate project {0} - {1} as it was reported late".format(nomination.project, nomination.project_name))

	def validate_joint_project(self, project):
		if not frappe.db.get_value("Project", project, "joint_project"):
				frappe.throw("You cannot nominate project {0} under 'Joint' as it was not reported as a Joint Project".format(project))

def get_avenue_limit():
	limits = {}
	for avenue in frappe.get_all("Avenue", fields=["name", "nominations_per_quarter"]):
		limits[avenue.get('name')] = avenue.get('nominations_per_quarter')
	return limits

def get_yearly_limit():
	limits = {}
	for category in frappe.get_all("Nomination Category", fields=["name", "nominations_per_year"]):
		limits[category.get('name')] = category.get('nominations_per_year')
	return limits

@frappe.whitelist()
def get_nomination_avenue(project=None, avenue=None):
	if avenue:
		return frappe.db.get_value("Project", project, frappe.scrub(avenue))