
import csv
import math
from pathlib import Path
from units import celsius_to_fahrenheit

DATA_FILE = Path(__file__).with_name("sensor_data.csv")
LOG_FILE = Path(__file__).with_name("sensor_log.csv")

MIN_TEMP = 0.0
MAX_TEMP = 50.0
MAX_CHANGE = 5.0  # Provisional spike threshold


def process_sensor_data():
    last_accepted = None

    with DATA_FILE.open(newline="") as source, \
         LOG_FILE.open("w", newline="") as output:

        reader = csv.DictReader(source)
        writer = csv.writer(output)

        writer.writerow([
            "sample", "raw_value", "temperature_c",
            "decision", "reason", "accepted_c",
            "result_f"
        ])

        for row in reader:
            sample = row["sample"]
            raw = row["raw_value"]
            value = row["temperature_c"].strip()
            reason = ""

            try:
                temp = float(value)
                if not math.isfinite(temp):
                    reason = "Invalid numeric value"
            except ValueError:
                temp = None
                reason = "Missing or invalid temperature"

            if not reason and row["unit"].strip() != "C":
                reason = "Unexpected unit"

            if not reason and row["status"].strip() != "OK":
                reason = "Sensor reported invalid reading"

            if not reason and not MIN_TEMP <= temp <= MAX_TEMP:
                reason = "Out of range"

            if not reason and last_accepted is not None:
                if abs(temp - last_accepted) > MAX_CHANGE:
                    reason = "Suspicious spike"

            if reason:
                decision = "REJECTED"
                accepted = ""
                result = ""
            else:
                decision = "ACCEPTED"
                accepted = temp
                result = celsius_to_fahrenheit(temp)
                last_accepted = temp

            writer.writerow([
                sample, raw, value, decision,
                reason, accepted, result
            ])

            print(
                f"Sample {sample}: {decision}"
                f" | Raw={raw}"
                f" | Temperature={value}"
                f" | Result={result if result != '' else 'N/A'}"
                f" | {reason}"
            )


if __name__ == "__main__":
    process_sensor_data()
