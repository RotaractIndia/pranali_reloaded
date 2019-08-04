app_name = "pranali_reloaded"
app_title = "Pranali Reloaded"
app_publisher = "Rtr.Neil Trini Lasrado"
app_description = "a reporting system for Rotaract District Organization"
app_icon = "octicon .octicon-organization"
app_color = "grey"
app_email = "neil@rotaractsuncity.in"
app_version = "0.0.1"

import frappe
from frappe import _

@frappe.whitelist()
def set_desktop_icons():
	desktop = {
		"Administration": [
			{
				"category": "Administration",
				"label": _('Club'),
				"icon": "octicon octicon-home",
				"type": 'doctype',
				"name": 'Club',
				"link": '#List/Club/List'
			},
			{
				"category": "Administration",
				"label": _('Member'),
				"icon": "octicon octicon-organization",
				"type": 'doctype',
				"name": 'Member',
				"link": '#List/Member/List'
			},
			{
				"category": "Administration",
				"label": _('Receipt'),
				"icon": "octicon octicon-gist-secret",
				"type": 'doctype',
				"name": 'Receipt',
				"link": '#List/Receipt/List'
			},
			{
				"category": "Administration",
				"label": _('Project'),
				"icon": "octicon octicon-rocket",
				"type": 'doctype',
				"name": 'Project',
				"link": '#List/Project/List'
			},
			{
				"category": "Administration",
				"label": _('Meeting'),
				"icon": "octicon octicon-briefcase",
				"type": 'doctype',
				"name": 'Meeting',
				"link": '#List/Meeting/List'
			},
			{
				"category": "Administration",
				"label": _('Ambassadorial Report'),
				"icon": "octicon octicon-globe",
				"type": 'doctype',
				"name": 'Ambassadorial Report',
				"link": '#List/Ambassadorial Report/List'
			},
			{
				"category": "Administration",
				"label": _('Directory'),
				"icon": "octicon octicon-file-submodule",
				"type": 'query-report',
				"name": 'Directory',
				"link": '#query-report/Directory'
			},
			{
				"category": "Administration",
				"label": _('Pay Dues Online'),
				"icon": "octicon octicon-credit-card",
				"link": '/pay',
			},
			{
				"category": "Administration",
				"label": _('Pranali User Registration'),
				"icon": "octicon octicon-organization",
				"type": 'doctype',
				"name": 'Registrations',
				"link": '#List/Registrations/List'
			}
		]
	}
	return desktop