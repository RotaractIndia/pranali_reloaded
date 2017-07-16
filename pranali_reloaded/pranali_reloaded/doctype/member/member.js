// Copyright (c) 2016, Rtr.Neil Trini Lasrado and contributors
// For license information, please see license.txt

frappe.ui.form.on('Member', {
    refresh: function(frm) {
        if (!frm.doc.dues_paid && !frm.is_new() && frm.perm[0].write) {
            frm.add_custom_button(__("Re-Register Member"), function() {
                frappe.call({
                    method: "pranali_reloaded.pranali_reloaded.doctype.member.member.register_member",
                    args: {
                        member_name: frm.doc.name
                    },
                    callback: function(r) {
                        if (r.message) {
                            frappe.msgprint("Member Registered.");
                            frm.reload_doc();
                        }
                    }
                });
            });
        }
    }
});