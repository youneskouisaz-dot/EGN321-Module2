# AI Usage Log

## AI Tool Used

ChatGPT

## Use 1 - Repository Setup

### Prompt

I asked for help creating the required GitHub repository structure for EGN321 Module 2 Assignment 2.1.

### AI Response

The AI suggested the required files and folders:

- `README.md`
- `AI_LOG.md`
- `requirements.txt`
- `src/units.py`
- `src/__init__.py`
- `tests/test_units.py`

### What I Changed

I created the repository structure in GitHub and reviewed it against the assignment requirements.

### Verification

I compared the repository structure with the assignment instructions.

---

## Use 2 - Conversion Functions

### Prompt

I asked for help creating reusable unit-conversion functions with clear names and named constants.

### AI Response

The AI suggested using small functions that receive values as parameters, return converted values, use descriptive names, and avoid `input()` and `print()`.

### What I Changed

I used the conversion requirements and reference workbook to decide which conversions belong in `units.py`.

### Verification

I checked the conversion factors against the reference workbook and the NIST unit-conversion resources provided in the assignment.

---

## Use 3 - Automated Tests

### Prompt

I asked for help creating pytest tests that meet the assignment requirements.

### AI Response

The AI suggested:

- known-value tests
- reverse conversion tests
- a round-trip test
- a zero-value test
- `pytest.approx()` for floating-point comparisons

### What I Changed

I used independently known reference values rather than using the conversion functions to generate their own expected answers.

### Verification

I compared the expected values with the reference workbook and ran the pytest test suite.

---

## Use 4 - Documentation

### Prompt

I asked for help organizing the README and documenting the engineering rule, supported conversions, testing strategy, reuse, and limitations.

### AI Response

The AI suggested documenting the purpose of the module, conversion-factor sources, the boundary-conversion rule, test strategy, reuse expectations, and known limitations.

### What I Changed

I reviewed the documentation and adjusted it to match the assignment requirements.

### Verification

I compared the finished documentation with the assignment checklist before submission.
