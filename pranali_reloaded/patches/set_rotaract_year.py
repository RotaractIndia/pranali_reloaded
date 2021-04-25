import frappe

def execute():
    frappe.reload_doc('pranali_reloaded', 'doctype', 'Receipt', force=True)
    frappe.reload_doc('pranali_reloaded', 'doctype', 'OCV', force=True)
    frappe.reload_doc('pranali_reloaded', 'doctype', 'AARA Nomination', force=True)
    frappe.reload_doc('pranali_reloaded', 'doctype', 'Project', force=True)
    frappe.reload_doc('pranali_reloaded', 'doctype', 'Meeting', force=True)
    frappe.reload_doc('pranali_reloaded', 'doctype', 'Ambassadorial Report', force=True)


    frappe.db.sql("update `tabReceipt` set rotaract_year='2020-21'")
    frappe.db.sql("update `tabOCV` set rotaract_year='2020-21'")
    frappe.db.sql("update `tabAARA Nomination` set rotaract_year='2020-21'")
    frappe.db.sql("update `tabProject` set rotaract_year='2020-21'")
    frappe.db.sql("update `tabMeeting` set rotaract_year='2020-21'")
    frappe.db.sql("update `tabAmbassadorial Report` set rotaract_year='2020-21'")