import frappe 

def execute():
    frappe.reload_doc("Pranali Reloaded", "doctype", "Pranali Settings")
    
    for club in frappe.get_all("Club"):
        frappe.get_doc("Club", club.name).save()

    for meeting in frappe.get_all("Meeting", filters={"type_of_meeting":"BOD Meet" }):
        doc = frappe.get_doc("Meeting", meeting.name)
        total_members = frappe.db.get_value("Club", doc.club, "board_of_directors")
        frappe.db.set_value("Meeting", doc.name, "total_registered_board_of_directors", total_members)
        if total_members>0:
            per_att = (doc.home_club / total_members) * 100
            frappe.db.set_value("Meeting", doc.name, "percentage_attendance", per_att)
