# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import requests
from frappe.model.document import Document

class ClubEvent(Document):
	def on_submit(self):
		self.send_date()
		
	def send_date(self):
		event = {
			"event-title": self.event_name,
			"club-name": self.club,
			"image-url": self.image_url,
			"event-excerpt": self.event_summary,
			"event-venue": self.venue,
			"venue-url": self.venue_url,
			"event-start-time": self.start_time,
			"event-end-time": self.end_time
		}
		requests.post("http://api.rotaract3140.org/taskAddEntry.php?type=events", data=event)