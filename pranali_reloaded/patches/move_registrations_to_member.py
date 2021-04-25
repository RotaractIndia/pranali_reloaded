import frappe 

def execute():
    frappe.reload_doc('pranali_reloaded', 'doctype', 'member', force=True)
    users = frappe.get_all("Registrations")
    for user in users:
        registration = frappe.get_doc("Registrations", user.name)
        member = frappe.get_all("Member", filters={"email": user.name})
        if member:
            frappe.db.set_value("Member", member[0].name, "user", registration.user)
            frappe.db.set_value("Member", member[0].name, "enable_pranali_access", registration.enabled)
            frappe.db.set_value("Member", member[0].name, "limited_access", registration.limited_access)
            
