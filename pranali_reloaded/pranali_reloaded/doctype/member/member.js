// Copyright (c) 2016, Rtr.Neil Trini Lasrado and contributors
// For license information, please see license.txt

frappe.ui.form.on('Member', {
    refresh: function(frm) {
        frm.set_df_property("member_name", "read_only", frm.doc.__islocal ? 0 : 1);
        if (frm.doc.dues_paid ==0) {
            frm.add_custom_button(__('Pay Dues'), function () {
                frm.trigger("pay_dues");;
            }).addClass('btn-primary');
        }
    },

    pay_dues: function(frm) {
        frappe.call({
            method: "pranali_reloaded.pranali_reloaded.doctype.member.member.pay_dues",
            args: {
                member_id: frm.doc.name,
            },
            callback: function(r) {
                frm.reload_doc();
            }
        });
    }
});