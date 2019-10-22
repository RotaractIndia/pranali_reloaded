from datetime import timedelta

import frappe

@frappe.whitelist()
def get_dashboards(club):
	user_club = frappe.db.get_all("User Permission",
	filters={"user": frappe.session.user, "allow": "Club"},
	fields=["for_value"])

	if user_club:
		club = user_club[0].for_value
	else:
		frappe.throw("No Club Assigned!")

	values = frappe.get_all("Project",
		filters={"club": club, "docstatus": 1},
		fields=["sum(incomes) as income, sum(expenditure) as expense, sum(total) as footfall"])

	top_projects = frappe.get_all("Project",
		filters={"club": club, "docstatus": 1},
		fields=["project_name", "avenue_1", "avenue_2", "(incomes - expenditure) as net_profit"],
		order_by="net_profit desc",
		limit=5)

	reporting_status = frappe.get_all("Project",
		filters={"club": club, "docstatus": 1},
		fields=["project_status as status", "count(name) as count"],
		group_by="status")

	projects_by_month = frappe.get_all("Project",
		filters={"club": club, "docstatus": 1},
		fields=["month(end_time) as month", "count(name) as count"],
		group_by="month", order_by="month")

	projects_per_month = [{
	    'x': 10,
	    'y': 20
}, {
    'x': 15,
    'y': 10
}]
	

	if values:
		return {
			"total_income": values[0].income,
			"total_expenses": values[0].expense,
			"net_profit": values[0].income - values[0].expense,
			"total_footfall": values[0].footfall,
			"top_projects": top_projects,
			"reporting_status": reporting_status,
			"projects_per_month": projects_per_month
		}
	else:
		return {
			"total_income": 0,
			"total_expenses": 0,
			"net_profit": 0,
			"total_footfall": 0,
		}

def get_club_projects(club):
	projects = frappe.get_all("Project",
		filters={"club": club, "docstatus": 1},
		fields=["avennue_1", "avenue_2"])