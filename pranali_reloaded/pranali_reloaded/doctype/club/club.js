frappe.ui.form.on("Club", {
	refresh: function(frm) {
		if(!frm.doc.__islocal) {
			cur_frm.cscript.update_statistics(frm);
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