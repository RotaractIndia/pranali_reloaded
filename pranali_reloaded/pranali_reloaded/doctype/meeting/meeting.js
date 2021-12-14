// Copyright (c) 2020, Rtr.Neil Trini Lasrado and contributors
// For license information, please see license.txt

cur_frm.cscript.guest = function(doc) {
	doc.total = cint(doc.home_club) + cint(doc.other_club) + cint(doc.district_council_members) 
			+ cint(doc.alumini) + cint(doc.rotarians) + cint(doc.pis) + cint(doc.guest) + cint(doc.other_district) 
	refresh_field('total');
};

cur_frm.cscript.home_club = cur_frm.cscript.other_club = cur_frm.cscript.district_council_members = cur_frm.cscript.alumini =
	cur_frm.cscript.rotarians = cur_frm.cscript.pis = cur_frm.cscript.other_district = cur_frm.cscript.guest;

frappe.ui.form.on('Meeting', {
	refresh: function(frm) {
		frm.trigger('show_progress_bar');
	},

	show_progress_bar: function(frm) {
		var bars = [];
		let progress_class = "progress-bar-danger"
		let progress_percentage = frm.doc.percentage_attendance.toFixed(2)
		if (progress_percentage > 50) {
			progress_class = "progress-bar-success"
		} else if (progress_percentage > 40) {
			progress_class = "progress-bar-warning"
		}
		
		let message = progress_percentage + '% Home Club members attended.' ;
		let title = progress_percentage + '% Home Club members attended.';

		if (frm.doc.type_of_meeting == "BOD Meet") {
			message = progress_percentage + '% Board of Directors attended.' ;
			title = progress_percentage + '% Board of Directors attended.';
		}

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
