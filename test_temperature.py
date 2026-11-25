import pytest

from TemperatureClass import Temperature


def test_default_unit() -> None:
    """Test that the default unit is Celsius."""
    temperature = Temperature(25)
    assert temperature.value == 25, "Default value should be 25"
    assert temperature.unit == 'C', "Default unit should be Celsius"

@pytest.mark.parametrize("unit, expected_unit", [
    ("C", "C"), ("c", "C"), 
    ("F", "F"), ("f", "F"),
    ("K", "K"), ("k", "K")
])
def test_case_insensitive_unit(unit: str, expected_unit: str) -> None:
    temperature = Temperature(25, unit=unit)
    assert temperature.unit == expected_unit, f"Expected unit {expected_unit}, but got {temperature.unit}"  

def test_value_is_read_only() -> None:
    """Test that the value attribute is read-only."""
    temperature = Temperature(25, "C")
    with pytest.raises(AttributeError):
        temperature.value = 30

def test_unit_is_read_only() -> None:
    """Test that the unit attribute is read-only."""
    temperature = Temperature(25, "C")
    with pytest.raises(AttributeError):
        temperature.unit = "F"

@pytest.mark.parametrize("unit", ["X", "Celsius", "", " C", "F "])
def test_invalid_unit(unit: str) -> None:
    """Test that an invalid unit raises a ValueError."""
    with pytest.raises(ValueError):
        Temperature(25, unit=unit)

@pytest.mark.parametrize("value, unit", [
    (-300, "C"),
    (-460, "F"),
    (-1, "K")
])
def test_below_absolute_zero(value: int, unit: str) -> None:
    """Test that a temperature below absolute zero raises a ValueError."""
    with pytest.raises(ValueError):
        Temperature(value, unit=unit)
