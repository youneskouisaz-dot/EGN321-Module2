import pytest

from src.units import (
    inches_to_feet,
    feet_to_inches,
    cubic_feet_to_gallons,
    gallons_to_cubic_feet,
)


def test_12_inches_equals_1_foot():
    assert inches_to_feet(12) == pytest.approx(1.0)


def test_24_inches_equals_2_feet():
    assert inches_to_feet(24) == pytest.approx(2.0)


def test_1_foot_equals_12_inches():
    assert feet_to_inches(1) == pytest.approx(12.0)


def test_1_cubic_foot_equals_7_48052_gallons():
    assert cubic_feet_to_gallons(1) == pytest.approx(7.48052)


def test_inches_to_feet_and_back():
    feet = inches_to_feet(36)
    restored = feet_to_inches(feet)
    assert restored == pytest.approx(36)


def test_cubic_feet_to_gallons_and_back():
    gallons = cubic_feet_to_gallons(5)
    restored = gallons_to_cubic_feet(gallons)
    assert restored == pytest.approx(5)


def test_length_round_trip():
    original = 42
    feet = inches_to_feet(original)
    restored = feet_to_inches(feet)
    assert restored == pytest.approx(original)


def test_zero_conversion():
    assert inches_to_feet(0) == pytest.approx(0)
    assert cubic_feet_to_gallons(0) == pytest.approx(0)
