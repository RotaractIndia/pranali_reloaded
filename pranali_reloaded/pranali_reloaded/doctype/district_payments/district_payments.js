// Copyright (c) 2021, Rtr.Neil Trini Lasrado and contributors
// For license information, please see license.txt

cur_frm.cscript.quantity = function(doc) {
	doc.grand_total = cint(doc.amount) * cint(doc.quantity) 
	refresh_field('grand_total');
};

cur_frm.cscript.payment_category = cur_frm.cscript.quantity;