import frappe

def set_user_permissions_for_dcm(doc, method):
    for r in doc.roles:
        if r.role =="DCM":
            if not frappe.get_all("User Permission",filters={"user":doc.name}):
                perm = frappe.new_doc("User Permission")
                perm.user = doc.name
                perm.allow = "Document Status"
                perm.for_value = "submitted"
                perm.apply_to_all_doctypes=True
                perm.save()
