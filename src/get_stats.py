"""
Log all of the metrics that exist in the Tesla API
"""
import asyncio
from tesla_api import TeslaApiClient
import statsd
import os
import sys


def is_metric(metric):
    """
    Determines if a metric is a valid object type for logging into
    influxDB (int, float, bool).

    Inputs: metric (the value to be tested for type)
    """
    if isinstance(metric, int) or isinstance(metric, float) or isinstance(metric, bool):
        return True
    else:
        return False


def log_metric(statsd, car, metric, value):
    """
    Logs the metrics to statsd (influxdb)

    Inputs: statsd - a Statsd connection
            car - Care name
            metric - The name of the metric to be logged
            value - value to be logged for the metric
    """
    if metric == "timestamp":
        return None
    if is_metric(value):
        if value is True:
            value = 1
        if value is False:
            value = 0

        influx_measure = metric + ",device=tesla,car=" + car
        statsd.gauge(influx_measure, value)
        print(influx_measure, ": ", str(value))


async def main():
    """
    Main program loop for looping through all of the cars and metrics
    """
    # Connect to Statsd
    statsd_server = "statsd-service.metrics.svc.cluster.local"
    # statsd_server = "metrics.thesniderpad.com"
    statsd_connection = statsd.StatsClient(statsd_server, 8125)

    # Which metrics collections are we interested in
    metrics_collections = [
        "charge_state",
        "climate_state",
        "drive_state",
        "gui_settings",
        "vehicle_config",
        "vehicle_state",
    ]

    # Connect to the tesla api
    username = os.environ["SECRET_USERNAME"]
    password = os.environ["SECRET_PASSWORD"]
    client = TeslaApiClient(username, password)

    # Grab all of the vehicles
    vehicles = await client.list_vehicles()

    # loop through all the vehicls found
    for v in vehicles:

        # Get python data representation of api objects
        if v.state == "offline":
            print("Vehicle is not available")
            continue  # Vehicle is offline, go to the next one (should we ever have one)
        else:
            data = await v.get_data()

        # Log all of the metrics for each collection
        for collection in metrics_collections:
            for item in data[collection]:
                log_metric(
                    statsd_connection,
                    data["display_name"],
                    item,
                    data[collection][item],
                )

    await client.close()


# Run the main program
asyncio.run(main())
