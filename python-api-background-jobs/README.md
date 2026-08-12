# Frappe Python API Background Jobs Assignment

## Daily Driver Income Scheduler

This assignment demonstrates a Frappe scheduler event that automatically adds a daily income amount to every Driver record.

### Driver fields used

- `name1` — driver's display name
- `salary` — accumulated salary/income value

### `tasks.py`

The `daily_maintenance()` function:

1. Fetches all Driver documents.
2. Reads each driver's current `salary`.
3. Adds ₹1000 to the salary.
4. Uses `frappe.db.set_value()` to save the updated salary.
5. Uses `frappe.log_error()` as a simple execution log so the background job can be verified from Error Log.

### Scheduler configuration

Add this to the application's `hooks.py`:

```python
scheduler_events = {
    "daily": [
        "practice_app.tasks.daily_maintenance"
    ]
}
```

The module path means:

```text
practice_app
    -> tasks.py
        -> daily_maintenance()
```

### Apply the scheduler configuration

From the Frappe bench directory:

```bash
bench migrate
bench start
```

Then open the local Frappe site and search for **Scheduled Job Type**. Verify that `practice_app.tasks.daily_maintenance` is registered with a daily frequency.

### Verify execution

After the scheduler executes, open **Error Log** and search for **Daily Driver Income Job**. The log message reports the daily amount, number of drivers updated, and execution date.

> The `tasks.py` file in this repository is the assignment implementation. In the actual Frappe app, place it at the application package root, alongside `hooks.py`, for example `apps/practice_app/practice_app/tasks.py`. Add the scheduler dictionary to the real application's `hooks.py` rather than importing `hooks_scheduler_events.py` from this repository.
