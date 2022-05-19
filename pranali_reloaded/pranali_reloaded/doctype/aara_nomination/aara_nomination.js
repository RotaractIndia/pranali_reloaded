// Copyright (c) 2016, Rtr.Neil Trini Lasrado and contributors
// For license information, please see license.txt

frappe.ui.form.on('AARA Nomination Project', {
    nominate_for: function(frm, cdn, cdt) {
        var local = locals[cdn][cdt];
        if (local.nominate_for == "Joint") {
            local.avenue = "Joint Project";
            frm.refresh_fields("projects");
        } 
        else {
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
        frm.set_query("project", "yearly_nomination", function() {
            return {
                filters: {
                    "docstatus": 1,
                    "project_status": ["in", ["On Time", "Early"]]
                }
            }
        });
        frm.set_query("nomination_category", "yearly_nomination", function() {
            return {
                filters: {
                    "member_nomination_category": 0
                }
            }
        });
        frm.set_query("member", "member_nomination", () => {
			return {
				filters: {
					dues_paid: true
				}
			}
		});
        frm.set_query("nomination_category", "member_nomination", function() {
            return {
                filters: {
                    "member_nomination_category": 1
                }
            }
        });
    }
});
