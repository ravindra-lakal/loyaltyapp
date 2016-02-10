# -*- coding: utf-8 -*-
# Copyright (c) 2015, New Indictrans Technologies PVT LTD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class Customer(Document):
	def validate(self):
		points_gained=0
		points_consumed=0
		total_points=0
		for raw in self.get("points_details"):
			points_gained+=int(raw.points_gained)
			points_consumed+=int(raw.points_consumed)
		self.total_points=points_gained - points_consumed
		self.pos_customer_id=self.name
	def checkusername(self):
		frappe.db.get_value("Customer",self.username,"username")
