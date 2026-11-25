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

@pytest.mark.parametrize("celsius, expected_fahrenheit", [
    (-273.15, -459.67),
    (-40.0, -40.0),
    (0.0, 32.0),
    (37.0, 98.6),
    (100.0, 212.0)
])
def test_celsius_to_fahrenheit(celsius: float, expected_fahrenheit: float) -> None:
    """Test conversion from Celsius to Fahrenheit."""
    temperature = Temperature(celsius, "C")
    result = temperature.to_fahrenheit()
    assert result == pytest.approx(expected_fahrenheit, abs=1e-9, rel=0)

@pytest.mark.parametrize("celsius, expected_kelvin", [
    (-273.15, 0.0),
    (-40.0, 233.15),
    (0.0, 273.15),
    (37.0, 310.15),
    (100.0, 373.15)
])
def test_celsius_to_kelvin(celsius: float, expected_kelvin: float) -> None:
    """Test conversion from Celsius to Kelvin."""
    temperature = Temperature(celsius, "C")
    result = temperature.to_kelvin()
    assert result == pytest.approx(expected_kelvin, abs=1e-9, rel=0)

@pytest.mark.parametrize("fahrenheit, expected_celsius", [
    (-459.67, -273.15),
    (-40.0, -40.0),
    (32.0, 0.0),
    (98.6, 37.0),
    (212.0, 100.0)
])
def test_fahrenheit_to_celsius(fahrenheit: float, expected_celsius: float) -> None:
    """Test conversion from Fahrenheit to Celsius."""
    temperature = Temperature(fahrenheit, "F")
    result = temperature.to_celsius()
    assert result == pytest.approx(expected_celsius, abs=1e-9, rel=0)

@pytest.mark.parametrize("fahrenheit, expected_kelvin", [
    (-459.67, 0.0),
    (-40.0, 233.15),
    (32.0, 273.15),
    (98.6, 310.15),
    (212.0, 373.15)
])
def test_fahrenheit_to_kelvin(fahrenheit: float, expected_kelvin: float) -> None:
    """Test conversion from Fahrenheit to Kelvin."""
    temperature = Temperature(fahrenheit, "F")
    result = temperature.to_kelvin()
    assert result == pytest.approx(expected_kelvin, abs=1e-9, rel=0)

@pytest.mark.parametrize("kelvin, expected_celsius", [
    (0.0, -273.15),
    (233.15, -40.0),
    (273.15, 0.0),
    (310.15, 37.0),
    (373.15, 100.0)
])
def test_kelvin_to_celsius(kelvin: float, expected_celsius: float) -> None:
    """Test conversion from Kelvin to Celsius."""
    temperature = Temperature(kelvin, "K")
    result = temperature.to_celsius()
    assert result == pytest.approx(expected_celsius, abs=1e-9, rel=0)

@pytest.mark.parametrize("kelvin, expected_fahrenheit", [
    (0.0, -459.67),
    (233.15, -40.0),
    (273.15, 32.0),
    (310.15, 98.6),
    (373.15, 212.0)
])
def test_kelvin_to_fahrenheit(kelvin: float, expected_fahrenheit: float) -> None:
    """Test conversion from Kelvin to Fahrenheit."""
    temperature = Temperature(kelvin, "K")
    result = temperature.to_fahrenheit()
    assert result == pytest.approx(expected_fahrenheit, abs=1e-9, rel=0)

@pytest.mark.parametrize("celsius", [
    -273.15, -40.0, 0.0, 37.0, 100.0
])
def test_round_trip(celsius: float) -> None:
    """Test round-trip conversion from Celsius to Fahrenheit to Kelvin and back to Celsius."""
    original = Temperature(celsius, "C")
    fahrenheit = original.convert_to("F")
    kelvin = fahrenheit.convert_to("K")
    result = kelvin.convert_to("C")
    assert result.unit == "C"
    assert result.value == pytest.approx(celsius, abs=1e-9, rel=0)
    assert result == original


def test_cross_unit_equality() -> None:
    """Test that temperatures in different units but representing the same physical temperature are equal."""
    temp_c = Temperature(0, "C")
    temp_f = Temperature(32, "F")
    temp_k = Temperature(273.15, "K")
    assert temp_c == temp_f
    assert temp_c == temp_k
    assert temp_f == temp_k
    assert not (temp_c != temp_f)
    assert not (temp_c != temp_k)
    assert not (temp_f != temp_k)

def test_cross_unit_ordering() -> None:
    """Test that temperatures in different units can be compared correctly."""
    temp_c = Temperature(0, "C")
    temp_f = Temperature(212, "F")
    assert temp_c < temp_f
    assert temp_c <= temp_f
    assert temp_f > temp_c
    assert temp_f >= temp_c
    assert temp_c != temp_f
