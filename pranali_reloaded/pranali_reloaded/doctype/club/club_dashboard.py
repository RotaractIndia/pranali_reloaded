from frappe import _

def get_data():
	return {
		'heatmap': True,
		'fieldname': 'club',
		'transactions': [
			{
				'label': 'Activities',
				'items': ['Meeting', 'Project', 'Ambassadorial Report']
			},
			{
				'label': 'Entity',
				'items': ['Receipt', 'Member', 'Membership']
			}
		]
	}