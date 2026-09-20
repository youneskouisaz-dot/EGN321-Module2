INCHES_PER_FOOT = 12.0
CUBIC_FEET_TO_GALLONS = 7.48052


def inches_to_feet(inches):
    """Convert inches to feet."""
    return inches / INCHES_PER_FOOT


def feet_to_inches(feet):
    """Convert feet to inches."""
    return feet * INCHES_PER_FOOT


def cubic_feet_to_gallons(cubic_feet):
    """Convert cubic feet to U.S. gallons."""
    return cubic_feet * CUBIC_FEET_TO_GALLONS


def gallons_to_cubic_feet(gallons):
    """Convert U.S. gallons to cubic feet."""
    return gallons / CUBIC_FEET_TO_GALLONS
KPA_TO_PSI = 0.1450377377


def kpa_to_psi(kpa):
    """Convert pressure from kilopascals to pounds per square inch."""
    return kpa * KPA_TO_PSI


def psi_to_kpa(psi):
    """Convert pressure from pounds per square inch to kilopascals."""
    return psi / KPA_TO_PSI
