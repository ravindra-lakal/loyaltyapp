# -*- coding: utf-8 -*-
# Copyright (c) 2015, New Indictrans Technologies PVT LTD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Order(Document):
	def before_submit(self):
		frappe.errprint(frappe.get_all("Rule Engine", fields=["amount","points "], filters={"status":"Active"}))
