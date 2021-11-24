frappe.listview_settings['Event Ticket'] = {
    add_fields: ["paid"],
    get_indicator: function(doc) {
        if (doc.paid) {
            return [__("Paid"), "green", "paid,=,1"];
        } else {
            return [__("Unpaid"), "orange", "paid,!=,1"];
        }
    }
};