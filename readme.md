# EGN321 Module 2 - Unit Conversion and Pump Performance Tool

## Project Overview

This repository contains the work for both Assignment 2.1 and Assignment 2.2 of EGN321 Module 2.

Assignment 2.1 created and tested a reusable unit-conversion module in `src/units.py`.

Assignment 2.2 builds on that work by reusing the conversion module inside a complete pump-performance calculation.

The main engineering rule used throughout the project is:

Convert once at the boundary, then keep the internal calculation in one consistent unit system.

---

## Assignment 2.1 - Unit Conversion Module

### Purpose

Assignment 2.1 created a reusable Python unit-conversion module that can be imported by later engineering tools.

### Supported Conversions

The unit module includes functions such as:

- inches to feet
- feet to inches
- cubic feet to U.S. gallons
- U.S. gallons to cubic feet
- kPa to psi
- psi to kPa

### Design

The conversion functions:

- receive values through parameters
- return converted values
- do not use `input()`
- do not print results
- use descriptive source-to-destination names
- use named conversion constants
- include short docstrings

### Assignment 2.1 Testing

The original unit tests include:

- known-value conversion tests
- reverse conversion tests
- round-trip testing
- zero-value testing

The original Assignment 2.1 tests remain in:

`tests/test_units.py`

The conversion module remains in:

`src/units.py`

---

## Assignment 2.2 - Pump Performance Tool

### Purpose

Assignment 2.2 extends the Assignment 2.1 work by rebuilding the inherited `PUMP_HEAD_rev6.xlsx` workbook as a Python engineering tool.

The Python version:

- validates raw inputs
- reuses the Assignment 2.1 conversion module
- converts pressure once at the input boundary
- performs the calculation with named intermediate values
- returns useful intermediate results
- rejects invalid or impossible system states
- uses automated tests for both calculations and refusals

## Inherited Artifact

The original pump calculation came from:

`PUMP_HEAD_rev6.xlsx`

The workbook contains:

- external inputs
- a multi-step calculation chain
- operating limits
- reference cases

## External Inputs

The pump calculation accepts:

- `suction_pressure_kpa` - suction pressure in kPa
- `discharge_pressure_kpa` - discharge pressure in kPa
- `flow_rate_gpm` - requested flow in gallons per minute
- `rated_flow_gpm` - rated flow in gallons per minute
- `specific_gravity` - fluid specific gravity
- `pump_efficiency_pct` - pump efficiency as a percentage

## Internal Units

Suction and discharge pressure enter the public calculation in kPa.

The calculation reuses `kpa_to_psi()` from `src/units.py` and converts both pressures to psi once at the input boundary.

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

Install the required package:

```bash
pip install -r requirements.txt
