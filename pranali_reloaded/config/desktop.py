from frappe import _

def get_data():
	return {
		"Ambassadorial Report": {
			"color": "#9b59b6",
			"icon": "icon-globe",
			"icon": "octicon octicon-globe",
			"link": "List/Ambassadorial Report",
			"doctype": "Ambassadorial Report",
			"type": "list"
		},
		
		"Member": {
			"color": "#ff9a00",
			"icon": "octicon octicon-organization",
			"label": _("Member"),
			"link": "List/Member",
			"doctype": "Member",
			"type": "list"
		},
		
		"Project": {
			"color": "#c23c59",
			"icon": "octicon octicon-rocket",
			"label": _("Project"),
			"link": "List/Project",
			"doctype": "Project",
			"type": "list"
		},
		
		"Club": {
			"color": "#53b436",
			"icon": "octicon octicon-home",
			"label": _("Club"),
			"link": "List/Club",
			"doctype": "Club",
			"type": "list"
		},
		
		"Meeting": {
			"color": "#0cb4d8",
			"icon": "octicon octicon-gist-secret",
			"label": _("Meeting"),
			"link": "List/Meeting",
			"doctype": "Meeting",
			"type": "list"
		},
		
		"Directory": {
			"color": "#dd004e",
			"icon": "octicon octicon-gist-secret",
			"label": _("Directory"),
			"link": "query-report/Directory",
			"type": "query-report"
		},
		
		"Messages": {
			"color": "#9b59b6",
			"icon": "icon-comments",
			"label": _("Messages"),
			"link": "messages",
			"type": "page"
		},
		
		"Receipt": {
			"color": "#0cb408",
			"icon": "octicon octicon-gist-secret",
			"label": _("Receipt"),
			"link": "List/Receipt",
			"doctype": "Receipt",
			"type": "list"
		},
	}
