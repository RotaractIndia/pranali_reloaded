from frappe import _

def get_data():
	return {
		'heatmap': True,
		'fieldname': 'club',
		'transactions': [
			{
				'items': ['Meeting', 'Project', 'Ambassadorial Report']
			},
			{
				'items': ['Receipt', 'Member']
			}
		]
	}