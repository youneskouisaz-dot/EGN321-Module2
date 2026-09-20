import pytest

from src.validation import validate_pump_inputs


def test_negative_suction_pressure_rejected():
    with pytest.raises(ValueError, match="suction_pressure_kpa"):
        validate_pump_inputs(
            suction_pressure_kpa=-1,
            discharge_pressure_kpa=420,
            flow_rate_gpm=145,
            rated_flow_gpm=180,
            specific_gravity=1.0,
            pump_efficiency_pct=72,
        )


def test_zero_flow_rate_rejected():
    with pytest.raises(ValueError, match="flow_rate_gpm"):
        validate_pump_inputs(
            suction_pressure_kpa=110,
            discharge_pressure_kpa=420,
            flow_rate_gpm=0,
            rated_flow_gpm=180,
            specific_gravity=1.0,
            pump_efficiency_pct=72,
        )


def test_efficiency_over_100_rejected():
    with pytest.raises(ValueError, match="pump_efficiency_pct"):
        validate_pump_inputs(
            suction_pressure_kpa=110,
            discharge_pressure_kpa=420,
            flow_rate_gpm=145,
            rated_flow_gpm=180,
            specific_gravity=1.0,
            pump_efficiency_pct=125,
        )


def test_discharge_must_be_greater_than_suction():
    with pytest.raises(ValueError, match="discharge_pressure_kpa"):
        validate_pump_inputs(
            suction_pressure_kpa=420,
            discharge_pressure_kpa=420,
            flow_rate_gpm=145,
            rated_flow_gpm=180,
            specific_gravity=1.0,
            pump_efficiency_pct=72,
        )


def test_flow_cannot_exceed_rated_flow():
    with pytest.raises(ValueError, match="flow_rate_gpm"):
        validate_pump_inputs(
            suction_pressure_kpa=110,
            discharge_pressure_kpa=420,
            flow_rate_gpm=200,
            rated_flow_gpm=180,
            specific_gravity=1.0,
            pump_efficiency_pct=72,
        )


def test_boundary_flow_equal_to_rated_flow_is_allowed():
    validate_pump_inputs(
        suction_pressure_kpa=110,
        discharge_pressure_kpa=420,
        flow_rate_gpm=180,
        rated_flow_gpm=180,
        specific_gravity=1.0,
        pump_efficiency_pct=72,
    )
