import pytest

from src.calculation import calculate_pump_performance


def test_reference_case_1():
    result = calculate_pump_performance(
        suction_pressure_kpa=110,
        discharge_pressure_kpa=420,
        flow_rate_gpm=145,
        rated_flow_gpm=180,
        specific_gravity=1.00,
        pump_efficiency_pct=72,
    )

    assert result["pump_head_ft"] == pytest.approx(103.861, rel=1e-3)
    assert result["brake_horsepower"] == pytest.approx(5.282, rel=1e-3)


def test_reference_case_2():
    result = calculate_pump_performance(
        suction_pressure_kpa=95,
        discharge_pressure_kpa=360,
        flow_rate_gpm=120,
        rated_flow_gpm=160,
        specific_gravity=0.92,
        pump_efficiency_pct=75,
    )

    assert result["pump_head_ft"] == pytest.approx(96.505, rel=1e-3)
    assert result["brake_horsepower"] == pytest.approx(3.587, rel=1e-3)


def test_unit_boundary_integration():
    result = calculate_pump_performance(
        suction_pressure_kpa=110,
        discharge_pressure_kpa=420,
        flow_rate_gpm=145,
        rated_flow_gpm=180,
        specific_gravity=1.00,
        pump_efficiency_pct=72,
    )

    assert result["suction_pressure_psi"] == pytest.approx(15.954, rel=1e-3)
    assert result["discharge_pressure_psi"] == pytest.approx(60.916, rel=1e-3)


def test_flow_margin():
    result = calculate_pump_performance(
        suction_pressure_kpa=110,
        discharge_pressure_kpa=420,
        flow_rate_gpm=145,
        rated_flow_gpm=180,
        specific_gravity=1.00,
        pump_efficiency_pct=72,
    )

    assert result["flow_margin_gpm"] == pytest.approx(35.0)
