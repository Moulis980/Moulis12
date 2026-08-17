import frappe


@frappe.whitelist()
def create_task(task_subject):
    """Create a new Task with the supplied subject and return its name."""

    if not task_subject:
        frappe.throw("Task Subject is required")

    task = frappe.new_doc("Transport")
    task.subject = task_subject
    task.save()

    return task.name
