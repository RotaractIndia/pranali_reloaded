import frappe
from frappe.utils import cint

def execute():
    projects = frappe.get_all("Project")
    for project in projects:
        doc = frappe.get_doc("Project", project)
        total = cint(doc.home_club) + cint(doc.other_club) + cint(doc.dcm) + cint(doc.alumini) + cint(doc.rotarians) + cint(doc.pis) + cint(doc.guest) + cint(doc.other_district) 
        if not doc.total == total:
            frappe.db.set_value("Project", project, "total", total)

    meetings = frappe.get_all("Meeting")
    for meeting in meetings:
        doc = frappe.get_doc("Meeting", meeting)
        total = cint(doc.home_club) + cint(doc.other_club) + cint(doc.district_council_members) + cint(doc.alumini) + cint(doc.rotarians) + cint(doc.pis) + cint(doc.guest) + cint(doc.other_district) 
        if not doc.total == total:
            frappe.db.set_value("Meeting", meeting, "total", total)