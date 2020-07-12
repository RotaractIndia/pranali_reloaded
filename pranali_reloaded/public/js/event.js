
/* global frappe, erpnext, __ */

frappe.ui.form.on('Event', {
	refresh: (frm) => {
		frm.page.clear_inner_toolbar();
	}
});
