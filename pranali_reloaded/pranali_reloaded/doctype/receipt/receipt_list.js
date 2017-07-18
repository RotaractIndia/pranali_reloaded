frappe.listview_settings['Receipt'] = {
    onload: function(listview) {
        if (!frappe.route_options) { //remove this condition if not required
            frappe.route_options = {
                "rotaract_year": ["=", "2017-18"]
            };
        }
    },
    add_fields: ["rotaract_year"],
    filters: [
        ["rotaract_year", "=", "2017-18"]
    ]
};