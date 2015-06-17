cur_frm.cscript.code = function(doc) {
	cur_frm.set_value("member_name", "");
	cur_frm.set_value("club", "");
	cur_frm.set_value("zone", "");
}

frappe.ui.form.on("Check In", {
	refresh: function(frm) {
		frm.disable_save();
	}
});