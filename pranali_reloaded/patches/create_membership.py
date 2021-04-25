import frappe 
from frappe.utils import getdate
from pranali_reloaded.pranali_reloaded.doctype.member.member import pay_dues

def execute():
    frappe.reload_doc('pranali_reloaded', 'doctype', 'member', force=True)
    frappe.reload_doc('pranali_reloaded', 'doctype', 'membership', force=True)
    frappe.reload_doc('pranali_reloaded', 'doctype', 'pranali_settings', force=True)
    frappe.reload_doc('pranali_reloaded', 'doctype', 'rotaract_year', force=True)

    for club in frappe.get_all("Club"):
        frappe.get_doc("Club", club.name).save()
    
    if not frappe.db.exists("Rotaract Year", "2020-21"):
        frappe.new_doc("Rotaract Year").update({
            "year": "2020-21",
            "start_date": getdate("01-07-2020"),
            "end_date": getdate("30-06-2021")
        }).save()
    frappe.db.set_value("Pranali Settings", "", "current_rotaract_year", "2020-21")
   
    for member in frappe.get_all("Member"):
        pay_dues(member.name)