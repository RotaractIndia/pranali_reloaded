from __future__ import unicode_literals

import frappe

def get_context(context):
	# make form read-only if paid
	if context.doc and context.doc.paid:
		context.read_only = 1
