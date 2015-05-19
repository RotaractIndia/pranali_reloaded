frappe.ui.form.on("ambassadorial member", "member_id", function(frm, cdt, cdn) {
	var d = locals[cdt][cdn];
	if (d.member_id) {
		return frappe.call({
			method: "pranali_reloaded.pranali_reloaded.doctype.ambassadorial_report.ambassadorial_report.get_member_name",
			args: {
				"id": d.member_id
			},
			callback: function (data) {
				frappe.model.set_value(d.doctype, d.name, "member_name", data.message);
			}
		})
	}
});