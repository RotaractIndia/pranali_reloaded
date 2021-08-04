cur_frm.add_fetch("member_id", "member_name", "member_name")


frappe.ui.form.on('Ambassadorial Report', {
    onload: (frm) => {
		frm.set_query("member_id", "members", () => {
			return {
				filters: {
					dues_paid: true
				}
			}
		});
	}
});