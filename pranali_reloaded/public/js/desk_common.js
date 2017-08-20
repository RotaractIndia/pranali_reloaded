
frappe.provide("pranali_reloaded");

pranali_reloaded.add_login_as_button = function(frm, label, user, submenu) {

	// only one of these roles is allowed to use these feature
	if ( frappe.user.has_role("Can Login As") || frappe.user.has_role("System Manager") || frappe.user.has_role("Administrator")) {
		frappe.call({
			method: "frappe.client.get",
			args: {
				doctype: "User",
				name: user,
			},
			callback: function(data) {
				var user_doc = data.message;
				// only administrator can login as system user
				if ( !frappe.user.has_role("Administrator") && user_doc && user_doc.user_type == "System User" ) {
					return;
				}

				if ( user_doc ) {
					frm.add_custom_button(label, function() {
						frappe.call({
							method: "pranali_reloaded.utils.login_as",
							args: { user: user },
							freeze: true,
							callback: function(data) {
								if ( data.redirect_to ) {
									window.location = data.redirect_to;
								}
							}
						})
					}, submenu);
				}
			}
		})
	}
}