from frappe import _

def get_data():
	return {
		'heatmap': False,
		'fieldname': 'member',
		'transactions': [
			{
				'label': 'Activities',
				'items': ['Membership']
			}
		]
	}