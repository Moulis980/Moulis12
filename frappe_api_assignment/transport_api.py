import frappe

@frappe.whitelist()
def get_vehicle_data():

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


    doc = frappe.get_doc("Transport", records[0]["name"])
    doc.status = "Under Maintenance"
    doc.save()

    for row in records:
        frappe.db.set_value(
            "Transport",
            row["name"],
            "status",
            "Selected",
        )

    return records
