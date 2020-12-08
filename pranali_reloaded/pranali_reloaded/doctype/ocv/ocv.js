// Copyright (c) 2020, Rtr.Neil Trini Lasrado and contributors
// For license information, please see license.txt

frappe.ui.form.on('OCV', {
	refresh: function(frm) {
		frm.trigger('show_progress_bar');
	},

	show_progress_bar: function(frm) {
		var bars = [];
		let progress_class = "progress-bar-danger"
		let progress_percentage = frm.doc.percentage_points_earned.toFixed(2)
		if (progress_percentage > 80) {
			progress_class = "progress-bar-success"
		} else if (progress_percentage > 40) {
			progress_class = "progress-bar-warning"
		}

		let message = progress_percentage + '% points earned.' ;
		let title = progress_percentage + '% points earned.';

		bars.push({
			'title': title,
			'width': progress_percentage + '%',
			'progress_class': progress_class
		});
		if (bars[0].width == '0%') {
			bars[0].width = '0.5%';
		}
		message = title;
		frm.dashboard.add_progress(__('Status'), bars, message);
	}
});
