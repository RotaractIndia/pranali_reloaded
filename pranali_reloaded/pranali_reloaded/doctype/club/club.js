// Copyright (c) 2016, Rtr.Neil Trini Lasrado and contributors
// For license information, please see license.txt

frappe.ui.form.on('Club', {
    refresh: function(frm) {
        frm.add_custom_button(__('Pay District'), function () {
            frm.trigger("pay_district");;
        }).addClass('btn-primary');
    },

    pay_district: function(frm) {
        frappe.model.open_mapped_doc({
            method: "pranali_reloaded.pranali_reloaded.doctype.club.club.pay_district",
            frm: frm,
        })
    }
});