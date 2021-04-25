import frappe

def set_rotaract_year(bootinfo):
    rotaract_year = frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")
    frappe.defaults.set_user_default('Rotaract Year', rotaract_year)