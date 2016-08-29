cur_frm.add_fetch("club", "club_email", "receivers_email_id")

frappe.ui.form.on("Receipt", {
	club: function(frm) {
		frm.set_value("receivers_name", frm.doc.club);
	}
});