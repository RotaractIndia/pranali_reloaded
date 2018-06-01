// Copyright (c) 2016, Rtr.Neil Trini Lasrado and contributors
// For license information, please see license.txt

frappe.ui.form.on('AARA Nomination Project', {
    nominate_for: function(frm, cdn, cdt) {
        var local = locals[cdn][cdt];
        if (local.nominate_for == "Joint") {
            local.avenue = "Joint Project";
            frm.refresh_fields("projects");
        } else if (local.nominate_for == "Ongoing") {
            local.avenue = "Ongoing";
            frm.refresh_fields("projects");
        } else if (local.nominate_for == "Flagship") {
            local.avenue = "Flagship";
            frm.refresh_fields("projects");
        } else {
            frappe.call({
                method: "pranali_reloaded.pranali_reloaded.doctype.aara_nomination.aara_nomination.get_nomination_avenue",
                args: {
                    "project": local.project,
                    "avenue": local.nominate_for
                },
                callback: function(r) {
                    local.avenue = r.message;
                    frm.refresh_fields("projects");
                }
            })
        }
    }
});

frappe.ui.form.on('AARA Nomination', {
    onload: function(frm) {
        frm.set_query("project", "projects", function() {
            return {
                filters: {
                    "docstatus": 1,
                    "quarter": frm.doc.quarter,
                    "project_status": ["in", ["On Time", "Early"]]
                }
            }
        });
    }
});
