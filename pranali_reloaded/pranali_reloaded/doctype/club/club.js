// Copyright (c) 2016, Rtr.Neil Trini Lasrado and contributors
// For license information, please see license.txt

frappe.ui.form.on('Club', {
    refresh: function(frm) {
        frm.add_custom_button(__('Add Funds to Pranali Walllet'), function () {
            frm.trigger("add_funds");;
        }).addClass('btn-primary');
    },

    add_funds: function(frm) {
        window.open( '/pay?new=1', '_blank');
    }
});