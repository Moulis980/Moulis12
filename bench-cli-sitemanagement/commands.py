import os

import click
import requests


@click.command("vehicle-summary")
@click.argument("vehicle")
def vehicle_summary(vehicle):
    """Get vehicle summary from the Fleet Management API."""

    url = "http://127.0.0.1:8000/api/method/practice_app.api.get_vehicle_summary"
    api_token = os.getenv("FRAPPE_API_TOKEN")

    if not api_token:
        click.echo(
            "FRAPPE_API_TOKEN is not set. "
            "Set it as 'API_KEY:API_SECRET' before running the command.",
            err=True,
        )
        raise click.Abort()

    headers = {
        "Authorization": f"token {api_token}"
    }

    try:
        response = requests.get(
            url,
            params={"vehicle": vehicle},
            headers=headers,
            timeout=10,
        )

        response.raise_for_status()

        result = response.json()

        click.echo(f"\nVehicle: {vehicle}")
        click.echo("Vehicle Summary:")
        click.echo(result)

    except requests.RequestException as e:
        click.echo(f"API request failed: {e}", err=True)


commands = [vehicle_summary]
