frappe.ui.form.on("User", "refresh", function(frm) {
	jhaudio_customizations.add_login_as_button(frm,
		__("Login As ") + frm.doc.first_name + (frm.doc.last_name?" " + frm.doc.last_name:""),
		frm.doc.name);
});
