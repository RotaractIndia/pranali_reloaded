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
		"Club Administration": [
			{
				"label": _('Club'),
				"icon": "octicon octicon-home",
				"type": 'doctype',
				"name": 'Club',
				"link": '#List/Club/List'
			},
			{
				"label": _('Member'),
				"icon": "octicon octicon-organization",
				"type": 'doctype',
				"name": 'Member',
				"link": '#List/Member/List'
			},
			{
				"label": _('Receipt'),
				"icon": "octicon octicon-clippy",
				"type": 'doctype',
				"name": 'Receipt',
				"link": '#List/Receipt/List'
			},
			{
				"label": _('OCV'),
				"icon": "octicon octicon-book",
				"type": 'doctype',
				"name": 'OCV',
				"link": '#List/OCV/List'
			},
			{
				"category": "Administration",
				"label": _('AARA Nomination'),
				"icon": "octicon octicon-gift",
				"type": 'doctype',
				"name": 'AARA Nomination',
				"link": '#List/AARA Nomination/List'
			}
		],
		"Reporting": [
			{
				"label": _('Project'),
				"icon": "octicon octicon-checklist",
				"type": 'doctype',
				"name": 'Project',
				"link": '#List/Project/List'
			},
			{
				"label": _('Meeting'),
				"icon": "octicon octicon-briefcase",
				"type": 'doctype',
				"name": 'Meeting',
				"link": '#List/Meeting/List'
			},
			{
				"label": _('Ambassadorial Report'),
				"icon": "octicon octicon-globe",
				"type": 'doctype',
				"name": 'Ambassadorial Report',
				"link": '#List/Ambassadorial Report/List'
			}
		],
		"Tools": [
			{
				"label": _('District E-Directory'),
				"icon": "octicon octicon-file-submodule",
				"type": 'query-report',
				"name": 'Directory',
				"link": '#query-report/Directory'
			},
			{
				"label": _('Insight Engine'),
				"icon": "octicon octicon-light-bulb",
				"type": 'page',
				"name": 'Insight Engine',
				"link": '#insight-engine'
			},
			{
				"label": _('Dashboard'),
				"name": 'Dashboard',
				"icon": "octicon octicon-graph",
				"type": "link",
				"link": "#dashboard",
			},
			{
				"label": _('Event Calendar'),
				"icon": "octicon octicon-calendar",
				"type": 'doctype',
				"name": 'Event Calendar',
				"link": '#List/Event/Calendar/Default'
			},
			{
				"label": _('Leaderboard'),
				"icon": "octicon octicon-star",
				"type": 'page',
				"name": 'Leaderboard',
				"link": '#social/users'
			},
			{
				"label": _('Social Wall'),
				"icon": "octicon octicon-thumbsup",
				"type": 'page',
				"name": 'Social',
				"link": '#social/home'
			}	
		]
	}
	hook_icons = frappe.get_hooks("icons")
	for icon in hook_icons:
		 desktop.get(icon.get('module')).append(icon)

	return desktop