


class Temperature:
    """Represents a temperature value."""

    def __init__(self, value: float, unit: str = "C", tolerance: float = 1e-9):
        """Initializes a temperature object."""
        self.value = value
        self.unit = unit.upper()
        self.tolerance = tolerance

    @property
    def value(self) -> float:
        """Returns the temperature value."""
        return self._value

    @property
    def unit(self) -> str:
        """Returns the temperature unit."""
        return self._unit

    def to_celsius(self) -> float:
        """Converts temperature to celsius."""
        if self.unit == "C":
            return self.value
        elif self.unit == "K":
            return self.value - 273.15
        elif self.unit == "F":
            return (self.value - 32) * (5 / 9)

    def to_fahrenheit(self) -> float:
        """Converts temperature to fahrenheit."""
        if self.unit == "F":
            return self.value
        elif self.unit == "C":
            return (self.value * (9 / 5) + 32)
        elif self.unit == "K":
            return (self.value - 273.15) * (9 / 5) + 32

    def to_kelvin(self) -> float:
        """Converts temperature to kelvin."""
        if self.unit == "K":
            return self.value
        elif self.unit == "C":
            return self.value + 273.15
        elif self.unit == "F":
            return (self.value - 32) * (5 / 9) + 273.15

    def converts_to(self, target_unit: str) -> Temperature:
  