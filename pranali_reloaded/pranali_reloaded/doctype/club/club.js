frappe.ui.form.on("Club", {
	refresh: function(frm) {
		if(!frm.doc.__islocal) {
			cur_frm.cscript.update_statistics(frm);
			
			frm.add_custom_button(__("Members"), function() {
				frappe.route_options = {
					club: frm.doc.name
				}
				frappe.set_route("List", "Member");
			});
		
			frm.add_custom_button(__("Projects"), function() {
				frappe.route_options = {
					club: frm.doc.name
				}
				frappe.set_route("List", "Project");
			});
		
			frm.add_custom_button(__("Meetings"), function() {
				frappe.route_options = {
					club: frm.doc.name
				}
				frappe.set_route("List", "Meeting");
			});
		
			frm.add_custom_button(__("Ambassadorial Reports"), function() {
				frappe.route_options = {
					club: frm.doc.name
				}
				frappe.set_route("List", "Ambassadorial Report");
			});
			
			frm.add_custom_button(__("Receipts"), function() {
				frappe.route_options = {
					club: frm.doc.name
				}
				frappe.set_route("List", "Receipt");
			});
		}
	}
});


cur_frm.cscript.update_statistics= function(frm) {
	frappe.call({
		method: "pranali_reloaded.pranali_reloaded.doctype.club.club.update_statistics",
		args: {
			"club": frm.doc.name
		},
		callback: function(r) {
			if(!r.exc) frm.refresh_fields();
		}
	});
}
