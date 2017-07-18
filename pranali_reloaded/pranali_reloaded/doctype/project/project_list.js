frappe.listview_settings['Project'] = {
    onload: function(listview) {
        if (!frappe.route_options) { //remove this condition if not required
            frappe.route_options = {
                "rotaract_year": ["=", "2017-18"]
            };
        }
    },
    add_fields: ["project_status", "rotaract_year"],
    filters: [
        ["rotaract_year", "=", "2017-18"]
    ],
    get_indicator: function(doc) {
        if (doc.project_status == "Late") {
            return [__("Late"), "orange", "status,=,Late"];
        } else if (doc.project_status == "On Time") {
            return [__("On Time"), "green", "status,=,On Time"];
        } else if (doc.project_status == "Early") {
            return [__("Early"), "blue", "status,=,Early"];
        }
    }
};