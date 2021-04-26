frappe.listview_settings['Member'] = {
    add_fields: ["dues_paid", "status"],

    get_indicator: function(doc) {
        if (doc.dues_paid==0 && doc.status=="Active Rotaractor") {
            return [__("Dues Not Paid"), "red", "dues_paid,=,0"];
        }
    }
};