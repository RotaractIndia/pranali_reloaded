import frappe 

def execute():
    for meeting in frappe.get_all("Meeting"):
        doc = frappe.get_doc("Meeting", meeting.name)
        total_members = frappe.db.get_value("Club", doc.club, "members_registered")
        frappe.db.set_value("Meeting", doc.name, "total_registered_members", total_members)
        if total_members>0:
            per_att = (doc.home_club / total_members) * 100
            frappe.db.set_value("Meeting", doc.name, "percentage_attendance", per_att)
