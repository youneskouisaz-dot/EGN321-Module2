# EGN321 Module 2 - Unit Conversion and Pump Performance Tool

## Project Overview

This repository contains the work for both Assignment 2.1 and Assignment 2.2 of EGN321 Module 2.

Assignment 2.1 created and tested a reusable unit-conversion module in `src/units.py`.

Assignment 2.2 builds on that work by reusing the conversion module inside a complete pump-performance calculation.

The main engineering rule used throughout the project is:

Convert once at the boundary, then keep the internal calculation in one consistent unit system.

## Assignment 2.1 - Unit Conversion Module

### Purpose

Assignment 2.1 created a reusable Python unit-conversion module that can be imported by later engineering tools.

### Supported Conversions

The unit module includes functions for:

- inches to feet
- feet to inches
- cubic feet to U.S. gallons
- U.S. gallons to cubic feet
- kPa to psi
- psi to kPa

### Assignment 2.1 Testing

The original unit tests include:

- known-value conversion tests
- reverse conversion tests
- round-trip testing
- zero-value testing

The Assignment 2.1 conversion module is located in:

`src/units.py`

The Assignment 2.1 tests are located in:

`tests/test_units.py`

## Assignment 2.2 - Pump Performance Tool

### Purpose

Assignment 2.2 extends the Assignment 2.1 work by rebuilding the inherited `PUMP_HEAD_rev6.xlsx` workbook as a Python engineering tool.

The Python version:

- validates raw inputs
- reuses the Assignment 2.1 conversion module
- converts pressure once at the input boundary
- performs the pump calculation using named intermediate values
- returns useful intermediate results
- rejects invalid or impossible system states
- uses automated tests for both calculations and refusals

## External Inputs

The pump calculation accepts:

- `suction_pressure_kpa` - suction pressure in kPa
- `discharge_pressure_kpa` - discharge pressure in kPa
- `flow_rate_gpm` - requested flow in gallons per minute
- `rated_flow_gpm` - rated flow in gallons per minute
- `specific_gravity` - fluid specific gravity
- `pump_efficiency_pct` - pump efficiency as a percentage

## Unit Conversion

Pressure enters the pump calculation in kPa.

The calculation reuses `kpa_to_psi()` from `src/units.py`.

Suction and discharge pressure are converted to psi once at the input boundary.

After conversion, pressure-related calculations remain in psi.

## Calculation Chain

The pump calculation follows this order:

1. Validate the raw external inputs.
2. Convert suction pressure from kPa to psi.
3. Convert discharge pressure from kPa to psi.
4. Calculate differential pressure in psi.
5. Calculate pump head in feet.
6. Calculate hydraulic horsepower.
7. Convert pump efficiency from percentage to decimal form.
8. Calculate brake horsepower.
9. Calculate flow margin.
10. Return the final results and useful intermediate values.

## Important Formulas

Differential pressure:

```text
discharge pressure psi - suction pressure psi

Pump head:

differential pressure psi × 2.31 / specific gravity

Hydraulic horsepower:

flow rate gpm × pump head ft × specific gravity / 3960

Efficiency fraction:

pump efficiency percent / 100

Brake horsepower:

hydraulic horsepower / efficiency fraction

Flow margin:

rated flow gpm - requested flow gpm
Validation Rules

The program rejects:

suction pressure below 0 kPa
discharge pressure below 0 kPa
flow rate less than or equal to 0 gpm
rated flow less than or equal to 0 gpm
specific gravity less than or equal to 0
pump efficiency less than or equal to 0%
pump efficiency greater than 100%

The program also rejects invalid combinations where:

discharge pressure is less than or equal to suction pressure
requested flow is greater than rated flow

Invalid inputs raise ValueError with a message identifying the problem.

Reference Cases
RC-1
Suction pressure: 110 kPa
Discharge pressure: 420 kPa
Flow rate: 145 gpm
Rated flow: 180 gpm
Specific gravity: 1.00
Efficiency: 72%
Expected pump head: 103.861 ft
Expected brake horsepower: 5.282 hp
RC-2
Suction pressure: 95 kPa
Discharge pressure: 360 kPa
Flow rate: 120 gpm
Rated flow: 160 gpm
Specific gravity: 0.92
Efficiency: 75%
Expected pump head: 96.505 ft
Expected brake horsepower: 3.587 hp
Testing Strategy

The repository contains tests for both assignments.

Assignment 2.1

tests/test_units.py

Tests unit conversions using:

known values
reverse conversions
round-trip conversions
zero values
Assignment 2.2

tests/test_validation.py

Tests:

individual rejection rules
combination rejection rules
boundary behavior

tests/test_calculation.py

Tests:

known-correct reference cases
unit conversion integration
pump calculation results
flow margin and intermediate values
How to Run the Tests

Install the required package:

pip install -r requirements.txt

Run all tests:

pytest

Running pytest checks both the Assignment 2.1 unit tests and the Assignment 2.2 pump-performance tests.

Project Structure
EGN321-Module2/
├── README.md
├── AI_LOG.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── units.py
│   ├── validation.py
│   └── calculation.py
└── tests/
    ├── test_units.py
    ├── test_validation.py
    └── test_calculation.py
Assumptions and Limitations

This project follows the equations, conversion factors, operating limits, and reference cases provided by the EGN321 assignments and workbook.

The pump-performance tool is intended for this engineering exercise and is not a replacement for manufacturer data or a complete real-world pump design model.

Development History

This repository was developed incrementally.

Earlier Git commits contain the Assignment 2.1 conversion module and tests.

Later commits extend the same repository with Assignment 2.2 validation, pump calculations, integration testing, and updated documentation.

AI Use

AI assistance used during both assignments is documented in AI_LOG.md.
