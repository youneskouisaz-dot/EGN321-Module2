# EGN321 Module 2 - Unit Conversion Module

## Purpose

This project creates a reusable Python unit-conversion module for later EGN321 assignments.

The goal is to make unit conversions clear, testable, and reusable.

## Core Engineering Principle

Convert once at the input boundary, then keep the internal calculation in one consistent unit system.

## Supported Conversions

The conversion functions in `src/units.py` are based on the requirements provided in the Module 2 conversion workbook.

The module uses clear function names that identify both the source unit and destination unit.

## Conversion Factors

Conversion factors are stored as named constants instead of unexplained numbers inside the functions.

The factors are verified using the reference workbook and authoritative unit-conversion sources.

Recommended reference:

NIST Unit Conversion  
https://www.nist.gov/pml/owm/metric-si/unit-conversion

## Design

Each conversion function:

- receives a value through a parameter
- returns the converted result
- does not use `input()`
- does not print results
- uses clear source-to-destination naming
- includes a short docstring

## Testing Strategy

The project includes at least 8 meaningful tests:

- 4 known-value conversion tests
- 2 reverse conversion tests
- 1 round-trip test
- 1 zero-value test

Expected test values come from independent reference data rather than from the function being tested.

`pytest.approx()` is used when floating-point comparison is appropriate.

## How to Run the Tests

Install the required package:

```bash
pip install -r requirements.txt
