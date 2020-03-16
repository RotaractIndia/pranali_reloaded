from datetime import timedelta

import frappe
import datetime

@frappe.whitelist()
def get_dashboards(club):
	if not club:
		return None 
		
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
	
	current_month = datetime.datetime.now().strftime("%B")
	reporting_months = []
	for month in ['July', 'August', 'September', 'October', 'November',
		'December','January','Febuary','March', 'April', 'May']:
			reporting_months.append(month)
			if month == current_month:
				break;
	club_service = com_service = isd = pd = sports = ed = pr = editorial = web_com = pis = hrd = 0 
	
	club_service_count, com_service_count, isd_count, pd_count, hrd_count = [],[],[],[], []
	sports_count, ed_count, pr_count, editorial_count, web_com_count, pis_count = [],[],[],[],[],[]

	for month in reporting_months:
		club_service = com_service = isd = pd = sports = ed = pr = editorial = web_com = pis = hrd = 0 
		projects = get_club_projects(club, month)
		if projects:
			for project in projects:
				avenue = [project.avenue_1, project.avenue_2]
				if "Club Service" in avenue:
					club_service+=1
				if  "Community Service" in avenue:
					com_service+=1
				if "International Service" in avenue:
					isd+=1
				if "Professional Development" in avenue:
					pd+=1
				if "Sports" in avenue:
					sports+=1
				if "ED" in avenue:
					ed+=1
				if "PR" in avenue:
					pr+=1
				if "Editorial" in avenue:
					editorial+=1
				if "Web Communications" in avenue:
					web_com+=1
				if "PIS" in avenue:
					pis+=1
				if avenue == "HRD":
					hrd+=1

		club_service_count.append(club_service)
		com_service_count.append(com_service)
		isd_count.append(isd)
		pd_count.append(pd)
		sports_count.append(sports)
		ed_count.append(ed)
		pr_count.append(pr)
		editorial_count.append(editorial)
		web_com_count.append(web_com)
		pis_count.append(pis)
		hrd_count.append(hrd)

	projects_per_month = {
		'Club Service' : club_service_count,
		'Community Service' : com_service_count,
		'International Service' : isd_count,
		'Professional Development' : pd_count,
		'Sports' : sports_count,
		'ED' : ed_count,
		'PR' : pr_count,
		'Editorial' : editorial_count,
		'Web Communications' : web_com_count,
		'PIS' : pis_count,
		'HRD' : hrd_count
	}

	if values:
		return {
			"total_income": values[0].income,
			"total_expenses": values[0].expense,
			"net_profit": values[0].income - values[0].expense,
			"total_footfall": values[0].footfall,
			"top_projects": top_projects,
			"reporting_status": reporting_status,
			"projects_per_month": projects_per_month,
			"reporting_months": reporting_months
		}
	else:
		return {
			"total_income": 0,
			"total_expenses": 0,
			"net_profit": 0,
			"total_footfall": 0,
		}


def get_club_projects(club, month):
	projects = frappe.get_all("Project",
		filters={"club": club, "reporting_month": month, "docstatus": 1},
		fields=["avenue_1", "avenue_2"])
	return projects

