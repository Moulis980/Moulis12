import frappe


def execute(filters=None):
    columns = [
        {
            "label": "Vehicle",
            "fieldname": "vehicle",
            "fieldtype": "Link",
            "options": "Vehicle",
            "width": 150
        },
        {
            "label": "Vehicle Type",
            "fieldname": "vehicle_type",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": "Make",
            "fieldname": "make",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": "Model",
            "fieldname": "model",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": "Purchase Date",
            "fieldname": "purchase_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": "Driver",
            "fieldname": "driver",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Current Odometer",
            "fieldname": "current_odometer",
            "fieldtype": "Float",
            "width": 130
        },
        {
            "label": "Status",
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 100
        }
    ]

    data = frappe.db.sql(
        """
        SELECT
            name AS vehicle,
            vehicle_type,
            make,
            model,
            purchase_date,
            driver,
            current_odometer,
            status
        FROM `tabVehicle`
        """,
        as_dict=True
    )

    return columns, data
