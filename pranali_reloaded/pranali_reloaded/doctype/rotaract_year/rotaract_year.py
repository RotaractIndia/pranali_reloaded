# -*- coding: utf-8 -*-
# Copyright (c) 2021, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class RotaractYear(Document):
	def validate(self):
		for dcm in self.district_council:
			if frappe.db.exists('User', dcm.email):
				self.update_user(dcm)
			else:
				self.make_user(dcm)

		for core in self.district_core_team:
			if frappe.db.exists('User', core.email):
				self.update_user(core, True)
			else:
				self.make_user(core, True)
		
	def make_user(self, dcm, core=False):
		user = frappe.new_doc("User")
		user.update({
			"first_name": dcm.full_name,
			"email": dcm.email,
			"send_welcome_email": 1
		})
		user.save(ignore_permissions=True)
		user.update({
			"bio": dcm.designation + ', District Council Member',
			"roles": [
				{"role": "District Council Member"}
			]
		})
		if core:
			user.update({
			"bio": dcm.designation + ', District Core Team',
			"roles": [
				{"role": "District Council Member"},
				{"role": "System Manager"}
			]
		})
		user.save(ignore_permissions=True)
		self.restrict_user(user.name)

	def update_user(self, dcm, core=False):
		existing_member = frappe.get_all("Member", filters={
			"email": dcm.email,
			"enable_pranali_access": 1
		})
		user=frappe.get_doc("User", dcm.email)
		if not existing_member:
			user.enabled= dcm.active
		user.update({
			"bio": dcm.designation + ', District Council Member',
			"roles": [
				{"role": "District Council Member"}
			]
		})
		if core:
			user.update({
			"bio": dcm.designation + ', District Core Team',
			"roles": [
				{"role": "District Council Member"},
				{"role": "System Manager"}
			]
		})
		user.save(ignore_permissions=True)
		if dcm.active:
			self.restrict_user(dcm.email)
		else:
			self.remove_user_restriction(dcm.email)

	def restrict_user(self, user):
		user_permissions = frappe.get_all("User Permission", filters={
			"user": user, 
			"allow": "Document Status"
		})
		if not user_permissions:
			permission = frappe.new_doc("User Permission")
			permission.user = user
			permission.allow = "Document Status"
			permission.for_value = "submitted"
			permission.save(ignore_permissions=True)
	
	def remove_user_restriction(self, user):
		user_permissions = frappe.get_all("User Permission", filters={
			"user": user, 
			"allow": "Document Status"
		})
		if user_permissions:
			frappe.delete_doc("User Permission", user_permissions[0].name)
