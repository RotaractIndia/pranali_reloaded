frappe.listview_settings['RED Registration'] = {
	add_fields: ["status"],
	get_indicator: function(doc) {
		if (doc.status=="Unpaid") {
			return [__("Unpaid"), "orange", "satus,=,Unpaid"];
		}
		else if (doc.status=="Paid") {
			return [__("Paid"), "green", "satus,=,Paid"];
		}
	}
};