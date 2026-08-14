import frappe
from frappe.utils import now


@frappe.whitelist()
def get_recent_todos():
    """
    Fetch the 5 most recently created ToDo records,
    along with the email address of each record owner.
    """

    todos = frappe.get_list(
        "ToDo",
        fields=[
            "name",
            "description",
            "owner"
        ],
        order_by="creation desc",
        limit_page_length=5
    )

    for todo in todos:
        todo["owner_email"] = frappe.db.get_value(
            "User",
            todo["owner"],
            "email"
        )

    return {
        "timestamp": now(),
        "records": todos
    }
