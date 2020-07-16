from __future__ import unicode_literals
import frappe

def welcome_email():
	return "Welcome to Pranali"

@frappe.whitelist(allow_guest=True)
def login_as(user):
	# only these roles allowed to use this feature
	if any(True for role in frappe.get_roles() if role in ('Can Login As', 'System Manager', 'Administrator')):

		user_doc = frappe.get_doc("User", user)

		# only administrator can login as a system user
		if not("Administrator" in frappe.get_roles()) and user_doc and user_doc.user_type == "System User":
			return False

		frappe.local.login_manager.login_as(user)
		frappe.set_user(user)

		frappe.db.commit()
		frappe.local.response["redirect_to"] = '/';
		return True

	return False

def set_energy_points(user, points, reference_doctype, reference_name):
	log = frappe.new_doc("Energy Point Log")
	log.update({
		"user": user,
		"points": points,
		"reference_doctype": reference_doctype,
		"reference_name": reference_name
	})