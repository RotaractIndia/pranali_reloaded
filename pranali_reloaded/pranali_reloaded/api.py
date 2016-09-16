import frappe
from frappe.utils import cint

def recalculate_balance_amount():
	for c in frappe.get_list("Club"):
		club = frappe.get_doc("Club", c)
		if club.total_amount:
			members = frappe.db.sql("select count(name) from tabMember where club=%s", c.name)[0][0]
			credit_amount = frappe.db.sql("select sum(amount) from tabReceipt where club=%s and credit_amount=1", c.name)[0][0]	
			club.balance_amount = cint(credit_amount) - ( cint(members)*50)
			club.save()