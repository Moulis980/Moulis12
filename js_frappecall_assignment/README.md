# JS - frappe.call Assignment

This assignment demonstrates communication between Frappe frontend JavaScript and a Python backend method.

## Files

- `task_api.py` - whitelisted Python method that creates a Task document.
- `task_dialog.js` - Frappe Dialog that collects a task subject and calls the backend with `frappe.call()`.

## Backend API

Python method:

```text
practice_app.task_api.create_task
```

The method:

1. Accepts `task_subject`.
2. Creates a new `Task` using `frappe.new_doc("Task")`.
3. Sets the `subject`.
4. Saves the document.
5. Returns the created Task name.

## Frontend Flow

```text
Dialog
  -> User enters Task Subject
  -> Create Task
  -> frappe.call()
  -> Python API
  -> Task saved
  -> Task name returned
  -> Dialog closes
  -> Green success message
```

## Testing

The JavaScript can be tested from the browser console or used in a Client Script.

The backend method can be called with:

```javascript
frappe.call({
    method: "practice_app.task_api.create_task",
    args: {
        task_subject: "Test Task"
    },
    callback(r) {
        console.log(r.message);
    }
});
```
