// Copyright (c) 2016, Rtr.Neil Trini Lasrado and contributors
// For license information, please see license.txt

frappe.ui.form.on('Member', {
    refresh: function(frm) {
        frm.set_df_property("member_name", "read_only", frm.doc.__islocal ? 0 : 1);
    }
});