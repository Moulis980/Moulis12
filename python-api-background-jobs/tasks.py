import frappe
from frappe.utils import nowdate


def daily_maintenance():
    drivers = frappe.get_all(
        "Driver",
        fields=["name", "name1", "salary"]
    )

    daily_income = 1000

    for driver in drivers:
        current_salary = driver.salary or 0
        new_salary = current_salary + daily_income

        frappe.db.set_value(
            "Driver",
            driver.name,
            "salary",
            new_salary
        )

    frappe.log_error(
        title="Daily Driver Income Job",
        message=(
            f"Successfully added ₹{daily_income} "
            f"to {len(drivers)} drivers on {nowdate()}."
        )
    )
