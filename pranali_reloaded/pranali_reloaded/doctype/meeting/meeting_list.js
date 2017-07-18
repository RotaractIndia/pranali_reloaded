frappe.listview_settings['Meeting'] = {
    add_fields: ["type_of_meeting", "rotaract_year"],
    onload: function(listview) {
        if (!frappe.route_options) { //remove this condition if not required
            frappe.route_options = {
                "rotaract_year": ["=", "2017-18"]
            };
        }
    },
    filters: [
        ["rotaract_year", "=", "2017-18"]
    ],
    get_indicator: function(doc) {
        if (doc.type_of_meeting == "GBM") {
            return [__("GBM"), "green", "type_of_meeting,=,GBM"];
        } else if (doc.type_of_meeting == "BOD Meet") {
            return [__("BOD Meet"), "orange", "type_of_meeting,=,BOD Meet"];
        } else if (doc.type_of_meeting == "Joint Meet") {
            return [__("Joint Meet"), "blue", "type_of_meeting,=,Joint Meet"];
        } else if (doc.type_of_meeting == "OCV") {
            return [__("OCV"), "red", "type_of_meeting,=,OCV"];
        } else if (doc.type_of_meeting == "Any Other") {
            return [__("Any Other"), "darkgrey", "type_of_meeting,=,Any Other"];
        }
    }
};