app_name = "pranali_reloaded"
app_title = "Pranali Reloaded"
app_publisher = "Rtr.Neil Trini Lasrado"
app_description = "a reporting system for Rotaract District Organization"
app_icon = "octicon .octicon-organization"
app_color = "grey"
app_email = "neil@rotaractsuncity.in"
error_report_email = "neil@rotaract3142.org"
app_version = "0.0.1"

welcome_email = "pranali_reloaded.utils.welcome_email"
boot_session = "pranali_reloaded.boot.set_rotaract_year"

app_include_js = [
	"/assets/pranali_reloaded/js/desk_common.js",
	"/assets/js/pranali_desk.js"
]

app_include_css = [
	"/assets/pranali_reloaded/css/pranali_reloaded.css",
	"/assets/pranali_reloaded/css/desk.css"
]

app_logo_url = "/assets/pranali_reloaded/images/rotary-wheel.png"
brand_html = "Pranali"

website_context = {
	"favicon": "/assets/pranali_reloaded/images/rotary-wheel.png",
	"splash_image": "/assets/pranali_reloaded/images/rotary-wheel.png",
}

override_whitelisted_methods = {
 	"frappe.desk.moduleview.get_desktop_settings": "pranali_reloaded.desk.set_desktop_icons"
}

doc_events = {
 	"User": {
 		"validate": "pranali_reloaded.hook_events.user.set_user_permissions_for_dcm",
		 "after_insert": "pranali_reloaded.hook_events.user.set_user_permissions_for_dcm"
	}
}

doctype_js = {
	"User": "public/js/user.js",
	"Event": "public/js/event.js"
}

scheduler_events = {
 	"daily": [
 		"pranali_reloaded.scheduler.check_membership"
 	]
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_js = "/assets/pranali_reloaded/js/pranali_reloaded.js"

# include js, css files in header of web template
# web_include_css = "/assets/pranali_reloaded/css/pranali_reloaded.css"
# web_include_js = "/assets/pranali_reloaded/js/pranali_reloaded.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "pranali_reloaded.install.before_install"
# after_install = "pranali_reloaded.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pranali_reloaded.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pranali_reloaded.tasks.all"
# 	],
# 	"daily": [
# 		"pranali_reloaded.tasks.daily"
# 	],
# 	"hourly": [
# 		"pranali_reloaded.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pranali_reloaded.tasks.weekly"
# 	]
# 	"monthly": [
# 		"pranali_reloaded.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "pranali_reloaded.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
