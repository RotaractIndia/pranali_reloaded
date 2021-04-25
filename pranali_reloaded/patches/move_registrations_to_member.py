import frappe 

def execute():
    frappe.reload_doc('pranali_reloaded', 'doctype', 'member', force=True)
    users = registration = frappe.db.sql("select * from `tabRegistrations`", as_dict=True)
    for user in users:
        member = frappe.get_all("Member", filters={"email": user.get('name')})
        if member:
            frappe.db.set_value("Member", member[0].name, "user", user.get('name'))
            frappe.db.set_value("Member", member[0].name, "enable_pranali_access", user.get('enabled'))
            frappe.db.set_value("Member", member[0].name, "limited_access", user.get('limited_access'))
            
