from frappe import _

def get_data():
	return {
		"Pranali Reloaded": {
			"color": "#ff0080",
			"icon": "octicon octicon-cloud-upload",
			"type": "module",
			"label": _("Pranali Reloaded")
		},
		
		"Member": {
			"color": "#0080ff",
			"icon": "octicon octicon-organization",
			"label": _("Member"),
			"link": "List/Member",
			"doctype": "Member",
			"type": "list"
		},
		
		"Project": {
			"color": "#00ff80",
			"icon": "octicon octicon-rocket",
			"label": _("Project"),
			"link": "List/Project",
			"doctype": "Project",
			"type": "list"
		},
		
		"Club": {
			"color": "#f94a32",
			"icon": "octicon octicon-home",
			"label": _("Club"),
			"link": "List/Club",
			"doctype": "Club",
			"type": "list"
		},
		
		"Meeting": {
			"color": "#f94a32",
			"icon": "octicon octicon-gist-secret",
			"label": _("Meeting"),
			"link": "List/Meeting",
			"doctype": "Meeting",
			"type": "list"
		}
	}
