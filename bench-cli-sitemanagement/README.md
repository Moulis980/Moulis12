# Bench CLI – Vehicle Summary Command

This assignment extends the Frappe Bench CLI with a custom command named `vehicle-summary`.

## Command

The custom command accepts a vehicle name and calls the Fleet Management API:

```bash
bench vehicle-summary Vehicle-002
```

It sends a request to:

```text
http://127.0.0.1:8000/api/method/practice_app.api.get_vehicle_summary?vehicle=Vehicle-002
```

## Authentication

The command expects the Frappe API credentials through the `FRAPPE_API_TOKEN` environment variable in this format:

```text
API_KEY:API_SECRET
```

Set it before running the command:

```bash
export FRAPPE_API_TOKEN="API_KEY:API_SECRET"
```

Then run:

```bash
bench vehicle-summary Vehicle-002
```

## Implementation

The command is defined using Click:

```python
@click.command("vehicle-summary")
@click.argument("vehicle")
def vehicle_summary(vehicle):
    ...

commands = [vehicle_summary]
```

The `commands` list exports the command so Bench can discover and register it.

## Notes

The API token is intentionally not stored in this repository. Keep API keys and secrets outside source control and use environment variables or another secure secret-management mechanism.
