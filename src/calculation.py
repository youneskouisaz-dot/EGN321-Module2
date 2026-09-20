from src.units import kpa_to_psi
from src.validation import validate_pump_inputs


PSI_TO_FEET_OF_WATER = 2.31
HYDRAULIC_HP_CONSTANT = 3960.0


def calculate_pump_performance(
    suction_pressure_kpa,
    discharge_pressure_kpa,
    flow_rate_gpm,
    rated_flow_gpm,
    specific_gravity,
    pump_efficiency_pct,
):
    """Calculate pump head, horsepower, and useful intermediate values."""

    validate_pump_inputs(
        suction_pressure_kpa,
        discharge_pressure_kpa,
        flow_rate_gpm,
        rated_flow_gpm,
        specific_gravity,
        pump_efficiency_pct,
    )

    suction_pressure_psi = kpa_to_psi(suction_pressure_kpa)
    discharge_pressure_psi = kpa_to_psi(discharge_pressure_kpa)

    differential_pressure_psi = (
        discharge_pressure_psi - suction_pressure_psi
    )

    pump_head_ft = (
        differential_pressure_psi
        * PSI_TO_FEET_OF_WATER
        / specific_gravity
    )

    hydraulic_horsepower = (
        flow_rate_gpm
        * pump_head_ft
        * specific_gravity
        / HYDRAULIC_HP_CONSTANT
    )

    efficiency_fraction = pump_efficiency_pct / 100.0

    brake_horsepower = hydraulic_horsepower / efficiency_fraction

    flow_margin_gpm = rated_flow_gpm - flow_rate_gpm

    return {
        "suction_pressure_psi": suction_pressure_psi,
        "discharge_pressure_psi": discharge_pressure_psi,
        "differential_pressure_psi": differential_pressure_psi,
        "pump_head_ft": pump_head_ft,
        "hydraulic_horsepower": hydraulic_horsepower,
        "efficiency_fraction": efficiency_fraction,
        "brake_horsepower": brake_horsepower,
        "flow_margin_gpm": flow_margin_gpm,
    }
