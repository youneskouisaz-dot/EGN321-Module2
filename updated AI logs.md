# AI Usage Log

## AI Tool Used

ChatGPT

## Assignment 2.1 - Unit Conversion Module

### Use 1 - Repository Structure

#### Prompt

I asked for help creating the required GitHub repository structure for EGN321 Module 2 Assignment 2.1.

#### AI Response

The AI suggested the required files and folders including `README.md`, `AI_LOG.md`, `requirements.txt`, `src/units.py`, `src/__init__.py`, and `tests/test_units.py`.

#### What I Changed

I created the repository structure in GitHub and reviewed it against the assignment requirements.

#### Verification

I compared the repository structure with the assignment instructions.

### Use 2 - Conversion Functions

#### Prompt

I asked for help creating reusable unit-conversion functions with clear names and named constants.

#### AI Response

The AI suggested small functions that receive values through parameters, return converted values, use descriptive source-to-destination names, and avoid `input()` and `print()`.

#### What I Changed

I used the required conversion functions and reviewed the conversion factors before adding them to `src/units.py`.

#### Verification

I checked the conversions using known values and automated tests.

### Use 3 - Assignment 2.1 Tests

#### Prompt

I asked for help creating pytest tests that meet the Assignment 2.1 requirements.

#### AI Response

The AI suggested known-value tests, reverse conversion tests, a round-trip test, and a zero-value test using `pytest.approx()`.

#### What I Changed

I reviewed the expected values before adding the tests to `tests/test_units.py`.

#### Verification

I used independently known conversion relationships and ran the test suite.

---

## Assignment 2.2 - Pump Performance Tool

### Use 4 - Workbook Analysis

#### Prompt

I asked for help understanding the pump workbook inputs, calculation chain, operating limits, and reference cases.

#### AI Response

The AI helped organize the workbook information into external inputs, internal units, calculation steps, validation rules, and reference test cases.

#### What I Changed

I used the values and rules directly from the provided workbook rather than relying only on AI-generated assumptions.

#### Verification

I compared the suggested structure against the workbook sheets including Inputs, Calculation Chain, Operating Limits, and Reference Cases.

### Use 5 - Pressure Conversion Integration

#### Prompt

I asked for help extending the Assignment 2.1 conversion module so the pump calculation could convert pressure from kPa to psi.

#### AI Response

The AI suggested adding `kpa_to_psi()` and `psi_to_kpa()` functions to `src/units.py`.

#### What I Changed

I added the pressure conversion functions to the existing unit-conversion module.

#### Verification

I compared the converted pressure values with the workbook reference values.

### Use 6 - Validation Layer

#### Prompt

I asked for help implementing the workbook operating limits in `src/validation.py`.

#### AI Response

The AI suggested validation for negative pressures, non-positive flow, non-positive rated flow, non-positive specific gravity, invalid efficiency, discharge pressure not exceeding suction pressure, and requested flow exceeding rated flow.

#### What I Changed

I used the workbook's Operating Limits sheet as the source for the validation rules.

#### Verification

I created automated rejection and boundary tests in `tests/test_validation.py`.

### Use 7 - Pump Calculation

#### Prompt

I asked for help converting the workbook calculation chain into Python.

#### AI Response

The AI suggested a calculation function that validates inputs, converts pressure once at the input boundary, calculates differential pressure, pump head, hydraulic horsepower, efficiency fraction, brake horsepower, and flow margin, and returns intermediate values.

#### What I Changed

I used named intermediate variables and reused `kpa_to_psi()` from the existing unit module rather than rewriting the conversion formula.

#### Verification

I compared the Python calculation with the workbook reference cases.

### Use 8 - Assignment 2.2 Tests

#### Prompt

I asked for help creating tests for the pump calculation and validation behavior.

#### AI Response

The AI suggested known-correct reference tests, individual rejection tests, combination rejection tests, a boundary test, and a unit-integration test.

#### What I Changed

I used the workbook's reference cases and operating limits as the expected evidence.

#### Verification

I ran the complete pytest suite, including the original Assignment 2.1 unit tests and the new Assignment 2.2 tests.

## Final Verification

I reviewed the generated code and documentation against the assignment requirements and workbook data before submission.
