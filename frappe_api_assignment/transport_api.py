import frappe


@frappe.whitelist()
def get_vehicle_data():
    """Return Transport records joined with Driver data.

    Demonstrates Frappe Query Builder, Document API, and Database API.
    """

    # --------------------------------
    # 1. Query Builder
    # --------------------------------

    Vehicle = frappe.qb.DocType("Transport")
    Driver = frappe.qb.DocType("Driver")

    records = (
        frappe.qb.from_(Vehicle)
        .join(Driver)
        .on(Vehicle.driver_name == Driver.name)
        .select(
            Vehicle.name,
            Vehicle.vehicle_name,
            Vehicle.vehicle_number,
            Vehicle.status,
            Driver.name1,
        )
        .limit(10)
        .run(as_dict=True)
    )

    if not records:
        return []

    # --------------------------------
    # 2. Document API
    # --------------------------------

    doc = frappe.get_doc("Transport", records[0]["name"])
    doc.status = "Under Maintenance"
    doc.save()

    # --------------------------------
    # 3. Database API
    # --------------------------------

    for row in records:
        frappe.db.set_value(
            "Transport",
            row["name"],
            "status",
            "Selected",
        )

    # --------------------------------
    # 4. Return results
    # --------------------------------

    return records
