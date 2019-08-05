frappe.listview_settings['Registrations'] = {
    add_fields: ["enabled"],

    get_indicator: function(doc) {
        if (doc.enabled) {
            return [__("Active User"), "green", "enabled,=,1"];
        } else {
            return [__("User Disabled"), "orange", "enabled,=,0"];
        }
    }
};