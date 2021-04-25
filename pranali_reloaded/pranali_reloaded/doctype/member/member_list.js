frappe.listview_settings['Member'] = {
    add_fields: ["dues_paid"],

    get_indicator: function(doc) {
        if (doc.dues_paid==0) {
            return [__("Dues Not Paid"), "red", "dues_paid,=,0"];
        }
    }
};