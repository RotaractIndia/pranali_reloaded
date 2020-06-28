frappe.listview_settings['Project'] = {
    add_fields: ["project_status"],

    get_indicator: function(doc) {
        if (doc.project_status == "Late") {
            return [__("Late"), "orange", "project_status,=,Late"];
        } else if (doc.project_status == "On Time") {
            return [__("On Time"), "green", "project_status,=,On Time"];
        } else if (doc.project_status == "Early") {
            return [__("Early"), "blue", "project_status,=,Early"];
        }
    }
};