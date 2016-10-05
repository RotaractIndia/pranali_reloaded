import frappe
from frappe.utils import cint

@frappe.whitelist()
def recalculate_balance_amount(club=None):
	for c in frappe.get_list("Club"):
		club = frappe.get_doc("Club", c)
		if club.total_amount:
			club.members_registered = cint(frappe.db.sql("select count(name) from tabMember where club=%s", c.name)[0][0])
			club.total_amount_credited_in_wallet = frappe.db.sql("""select sum(amount) from tabReceipt 
				where club=%s and credit_amount=1""", c.name)[0][0]	
			club.amount_spent_from_wallet = club.members_registered * 50
			club.balance_amount = club.total_amount_credited_in_wallet - club.amount_spent_from_wallet
			club.save()