# ToDo REST API Assignment

This assignment demonstrates Frappe Python API and database utility concepts by creating a secure, optimized REST endpoint for the `ToDo` DocType.

## Requirements

The API method:

- Uses `@frappe.whitelist()` to expose the method through the Frappe REST API.
- Uses `frappe.get_list()` to fetch the 5 most recently created `ToDo` records.
- Retrieves only the required `name`, `description`, and `owner` fields.
- Uses `frappe.db.get_value()` to fetch the owner's email from the `User` DocType.
- Uses `frappe.utils.now()` to return the current server timestamp.
- Returns a dictionary containing `timestamp` and `records`.

## API Method

```text
get_recent_todos
```

## Example Endpoint

Replace `practice_app.todo_api` with the actual Python module path in your Frappe app:

```text
/api/method/practice_app.todo_api.get_recent_todos
```

For a local development site, for example:

```text
http://127.0.0.1:8001/api/method/practice_app.todo_api.get_recent_todos
```

The endpoint should be tested while logged in to the Frappe site.

## Expected Response

```json
{
  "message": {
    "timestamp": "2026-08-14 11:00:00",
    "records": [
      {
        "name": "TODO-00005",
        "description": "Complete REST API assignment",
        "owner": "Administrator",
        "owner_email": "admin@example.com"
      }
    ]
  }
}
```

## Concepts Demonstrated

- Whitelisted Frappe API methods
- Secure record fetching with `frappe.get_list()`
- Optimized single-value retrieval with `frappe.db.get_value()`
- Server-side timestamps with `frappe.utils.now()`
- REST API testing through `/api/method/...`
