cur_frm.cscript.guest = function(doc) {
	doc.total = cint(doc.home_club) + cint(doc.other_club) + cint(doc.dcm) 
			+ cint(doc.alumini) + cint(doc.rotarians) + cint(doc.pis) + cint(doc.guest)
	refresh_field('total');
};

cur_frm.cscript.home_club = cur_frm.cscript.other_club = cur_frm.cscript.dcm = cur_frm.cscript.alumini =
	cur_frm.cscript.rotarians = cur_frm.cscript.pis = cur_frm.cscript.guest;
