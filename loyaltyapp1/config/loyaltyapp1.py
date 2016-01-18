from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
	{
		"label": _("Master"),
		"icon": "icon-wrench",
		"items": [
			{
				"type": "doctype",
				"name": "Brand",
				"description":_("Brand Details"),
			},
			{
				"type": "doctype",
				"name": "Catalog",
				"description":_("Catalog Details"),
			},
			{
				"type": "doctype",
				"name": "Color",
				"description": _("Color Details."),
			},
			{
				"type": "doctype",
				"name": "Department",
				"description": _("Department Details."),
			},
			{
				"type": "doctype",
				"name": "Family",
				"description": _("Family Details."),
			},
			{
				"type": "doctype",
				"name": "Product",
				"description": _("Product Details."),
			},
			{
				"type": "doctype",
				"name": "Season",
				"description": _("Season Details."),
			},
			{
				"type": "doctype",
				"name": "Size",
				"description": _("Size Details."),
			},
			{
				"type": "doctype",
				"name": "Store",
				"description": _("Store Details."),
			},
			{
				"type": "doctype",
				"name": "Style",
				"description": _("Style Details."),
			},
			{
				"type": "doctype",
				"name": "Sub Family",
				"description": _("Sub Family Details."),
			},







		]
	},

		{

			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Customer database."),
				},
				{
					"type": "doctype",
					"name": "Order",
					"description": _("Orders made by a customer."),
				},

			]
		},

	]
