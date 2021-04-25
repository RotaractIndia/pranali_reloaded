import frappe
from frappe.utils import today

def check_membership():
    members = frappe.get_all("Member", filters={("membership_valid_till", "<", frappe.utils.today())})
    for member in members:
        frappe.db.set_value("Member", member.name, "dues_paid", False)