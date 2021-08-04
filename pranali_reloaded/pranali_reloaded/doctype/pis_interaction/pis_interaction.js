// Copyright (c) 2021, Rtr.Neil Trini Lasrado and contributors
// For license information, please see license.txt

frappe.ui.form.on('PIS Interaction', {
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
