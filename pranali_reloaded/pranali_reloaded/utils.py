import frappe
from frappe.utils import cint, flt

def calculate_wallet_amount(club):
	wallet_details= {}
	district_dues = flt(frappe.db.get_single_value("Pranali Settings", "membership_dues"))
	wallet_details.update(district_dues= district_dues)
	total_amount = flt(frappe.db.sql("select sum(amount) from tabReceipt where docstatus=1 and credit_amount=1 and club=%s", club)[0][0])
	wallet_details.update(total_amount = total_amount)
	total_members= flt(frappe.db.sql("select count(name) from tabMember where club=%s and dues_paid=1", club)[0][0])
	wallet_details.update(total_members = total_members)
	membership_dues = flt(frappe.db.sql("select sum(membership_amount) from tabMembership where docstatus=1 and club=%s", club)[0][0])
	district_payments = flt(frappe.db.sql("select sum(grand_total) from `tabDistrict Payments` where docstatus=1 and club=%s", club)[0][0])
	amount_spent = membership_dues + district_payments
	wallet_details.update(amount_spent = amount_spent)
	wallet_details.update(balance_amount = total_amount - amount_spent)
	return wallet_details