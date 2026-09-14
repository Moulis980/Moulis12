import frappe

def get_context(context):
    context.articles = frappe.get_all(
        "Help Article",
        filters={"published": 1},
        fields=["name", "title"]
    )
