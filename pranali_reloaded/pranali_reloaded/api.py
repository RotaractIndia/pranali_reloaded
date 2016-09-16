import frappe

def recalculate_balance_amount():
	for c in frappe.get_list("Club"):
		club = frappe.get_doc("Club", c)
		if club.total_amount:
			members = frappe.db.sql("select count(name) from tabMember where club=%s", c.name)[0][0]		
			club.balance_amount = club.total_amount - (members*50)
			club.save()