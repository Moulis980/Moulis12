# Frappe Custom Whitelisted API Assignment

This assignment demonstrates three Frappe APIs in one custom endpoint:

1. **Query Builder** (`frappe.qb`) — joins the `Transport` and `Driver` DocTypes and returns a limited set of records.
2. **Document API** (`frappe.get_doc`) — fetches the first returned Transport document, updates its status, and saves it.
3. **Database API** (`frappe.db.set_value`) — updates the status field for every Transport returned by the query.

## API method

The implementation is in:

`frappe_api_assignment/transport_api.py`

```python
@frappe.whitelist()
def get_vehicle_data():
    ...
```

## Important field relationship

The `Transport.driver_name` Link field is joined with the Frappe internal `Driver.name` value:

```python
.on(Vehicle.driver_name == Driver.name)
```

The custom Driver field `name1` is selected only for displaying the driver's name:

```python
Driver.name1
```

Every Frappe DocType also has an internal `name` property, even when a `name` field is not visible in Form Builder. That internal name is used by `frappe.get_doc()` and `frappe.db.set_value()`.

## Endpoint

For the Frappe app where the method is installed at the corresponding Python module path, the endpoint follows this format:

```text
/api/method/practice_app.practice_app.doctype.transport.transport.get_vehicle_data
```

Example local URL:

```text
http://127.0.0.1:8001/api/method/practice_app.practice_app.doctype.transport.transport.get_vehicle_data
```

Because the method changes database records, use **POST** when testing the endpoint.

## Postman authentication

Use Frappe token authentication:

```text
Authorization: token API_KEY:API_SECRET
```

Then send a POST request to the endpoint.

## Expected flow

```text
Postman
   |
   v
@frappe.whitelist()
   |
   +--> Query Builder
   |      Transport JOIN Driver
   |
   +--> Document API
   |      get_doc() -> update -> save()
   |
   +--> Database API
   |      set_value() for returned records
   |
   v
return records
```

> **Note:** The Python file in this repository is the assignment implementation. In the actual Frappe app, place the method in the Python module path used by the API URL, such as the `transport.py` file inside the Transport DocType directory.
