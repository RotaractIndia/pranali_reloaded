from frappe import _

def get_data():
	return {
		'heatmap': True,
		'fieldname': 'club',
		'heatmap_message': _('This is based on the events of the Club'),
		'transactions': [
			{
				'items': ['Meeting', 'Project', 'Ambassadorial Report']
			},
			{
				'items': ['Receipt', 'Member']
			}
		]
	}