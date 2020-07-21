import frappe
from frappe.utils import cint, getdate
from frappe.social.doctype.post.post import get_viewed_posts


@frappe.whitelist()
def recalculate_balance_amount(club=None):
    for c in frappe.get_list("Club"):
        club = frappe.get_doc("Club", c)
        club.members_registered = cint(frappe.db.sql(
            "select count(name) from tabMember where club=%s", c.name)[0][0])
        club.total_amount_credited_in_wallet = cint(frappe.db.sql("""select sum(amount) from tabReceipt
			where club=%s and credit_amount=1""", c.name)[0][0])
        club.amount_spent_from_wallet = club.members_registered * 50
        club.balance_amount = club.total_amount_credited_in_wallet - \
            club.amount_spent_from_wallet
        club.save()


@frappe.whitelist()
def get_posts(filters=None, limit_start=0):
    filters = frappe.utils.get_safe_filters(filters)
    posts = frappe.get_all('Post',
                           fields=['name', 'content', 'owner', 'creation',
                                   'liked_by', 'is_pinned', 'is_globally_pinned'],
                           filters=filters,
                           limit_start=limit_start,
                           limit=20,
                           order_by='is_globally_pinned desc, creation desc')
    viewed_posts = get_viewed_posts()
    for post in posts:
        post['seen'] = post.name in viewed_posts
    return posts


@frappe.whitelist()
def get_birthdays():
    current_date = getdate()
    month = current_date.month
    yesterday = current_date.day-1
    today = current_date.day
    tomorrow = current_date.day+1

    members_born_yesterday = []
    members_born_today = []
    members_born_tomorrow = []

    member_birthdays = frappe.get_all(
        "Member",  fields=['member_name', 'dob', 'club'])
    for member in member_birthdays:
        birthdate = getdate(member.dob)
        if birthdate.month == month and birthdate.day == yesterday:
            members_born_yesterday.append(member)
        if birthdate.month == month and birthdate.day == today:
            members_born_today.append(member)
        if birthdate.month == month and birthdate.day == tomorrow:
            members_born_tomorrow.append(member)

        all_birthdays = {
            "yesterday": members_born_yesterday,
            "today": members_born_today,
            "tomorrow": members_born_tomorrow
        }
    return all_birthdays

@frappe.whitelist(allow_guest=True)
def get_club_list():
    return frappe.get_all("Club")

@frappe.whitelist(allow_guest=True)
def register(first_name, last_name, email, club):
    registration = frappe.new_doc("Registrations")
    registration.update({
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "club": club
    })
    registration.save(ignore_permission=True)