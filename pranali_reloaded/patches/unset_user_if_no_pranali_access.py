import frappe

def execute():
    frappe.db.sql("update tabMember set user='' where enable_pranali_access=False")