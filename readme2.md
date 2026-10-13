## Assignment 5.2 — Sensor Integration

### Project Overview

For Assignment 5.2, I updated my Module 2 engineering unit converter to work with data from a virtual temperature sensor instead of relying only on manually entered values.

I used my Arduino temperature sensor simulation from Velxio. The sensor produces temperature readings in Celsius, which are saved in a CSV file. My Python program reads these values, validates them, filters suspicious readings, and sends accepted temperatures to the unit converter.

I kept the original Module 2 conversion functions and added a Celsius-to-Fahrenheit function to support the temperature sensor.

### Sensor-to-Tool Workflow

Velxio Temperature Sensor → CSV File → Python Validation → Spike Filtering → Unit Converter → Result

### Files Added or Updated

| File | Purpose |
|---|---|
| `src/units.py` | Original unit converter with an added Celsius-to-Fahrenheit function |
| `src/sensor_data.csv` | Temperature readings collected from Velxio |
| `src/sensor_integration.py` | Reads, validates, filters, and processes sensor data |
| `src/sensor_log.csv` | Records accepted and rejected readings and conversion results |

### Validation and Filtering Rules

My Python program checks sensor readings before performing calculations.

- **Missing or invalid readings:** Rejected.
- **Temperature range:** Only temperatures between 0°C and 50°C are accepted.
- **Sensor status:** Readings must have an `OK` status.
- **Unit:** The temperature must be in Celsius (`C`).
- **Suspicious spikes:** A reading is rejected if it differs by more than 5°C from the last accepted temperature.
- **Rejected readings:** No Fahrenheit conversion is performed, and the rejection reason is recorded.

The 5°C threshold is the filtering rule currently implemented in my integration. A limitation is that a legitimate large temperature change may also be rejected until the readings return close enough to the last accepted value.

### Example Results

These results were produced when I ran the sensor integration program.

| Sample | Sensor Temperature | Decision | Fahrenheit Result |
|---|---|---|---|
| 3 | 29.99°C | Accepted | 85.98°F |
| 6 | 23.03°C | Rejected — Spike | N/A |
| 14 | 26.99°C | Accepted | 80.58°F |
| 20 | 42.01°C | Accepted | 107.62°F |
| 22 | 48.97°C | Accepted | 120.15°F |
| 23 | 52.06°C | Rejected — Invalid sensor status | N/A |

### Assumptions Broken by Sensor Input

| Original Assumption | What the Sensor Did | Software Change |
|---|---|---|
| Input is entered manually | Sensor automatically generated readings | Added CSV replay |
| Input is always valid | Some temperatures exceeded 50°C | Added range and status validation |
| Input remains stable | Sensor temperature changed between samples | Added spike filtering |
| Input always exists | Sensor data may be missing | Added missing-value handling |
| Input uses the expected unit | CSV data could contain an unexpected unit | Added unit validation |
| Every input can be calculated | Invalid readings cannot safely be used | Rejected invalid readings before conversion |

### How to Run

Open the repository in GitHub Codespaces.

From the repository root, run:

```bash
cd src
python sensor_integration.py
```

The program reads `sensor_data.csv`, processes the readings, displays the results in the terminal, and generates `sensor_log.csv`.

### Original Engineering Logic

The original Module 2 unit conversions for length, volume, and pressure were preserved.

A new Celsius-to-Fahrenheit conversion was added:

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
```

Only accepted sensor readings are passed into this function.

### Virtual Sensor Source

Simulator: Velxio

Sensor: 10k NTC thermistor connected to Arduino A0

Temperature unit: Celsius

Valid range: 0°C to 50°C

Simulation link: [Add your Velxio project link here]

### Testing

The integration has been run successfully using CSV sensor readings. The observed output includes accepted readings, spike rejections, and invalid sensor-status rejections.

Automated tests for all required normal and failure conditions are still to be added.
