import frappe
from frappe.utils import cint
from frappe.social.doctype.post.post import get_viewed_posts

@frappe.whitelist()
def recalculate_balance_amount(club=None):
	for c in frappe.get_list("Club"):
		club = frappe.get_doc("Club", c)
		club.members_registered = cint(frappe.db.sql("select count(name) from tabMember where club=%s", c.name)[0][0])
		club.total_amount_credited_in_wallet = cint(frappe.db.sql("""select sum(amount) from tabReceipt
			where club=%s and credit_amount=1""", c.name)[0][0])
		club.amount_spent_from_wallet = club.members_registered * 50
		club.balance_amount = club.total_amount_credited_in_wallet - club.amount_spent_from_wallet
		club.save()

@frappe.whitelist()
def get_posts(filters=None, limit_start=0):
	filters = frappe.utils.get_safe_filters(filters)
	posts = frappe.get_all('Post',
		fields= ['name', 'content', 'owner', 'creation', 'liked_by', 'is_pinned', 'is_globally_pinned'],
		filters=filters,
		limit_start=limit_start,
		limit=20,
		order_by= 'is_globally_pinned desc, creation desc')
	viewed_posts = get_viewed_posts()
	for post in posts:
		post['seen'] = post.name in viewed_posts
	return posts

@frappe.whitelist()
def get_birthdays(start_date):
	birthdays = frappe.get_all("Member", fields=['member_name', 'dob'],
		filters={"dob": [">=", start_date]}, order_by="dob ASC", limit=5)
	print(birthdays)
	return birthdays