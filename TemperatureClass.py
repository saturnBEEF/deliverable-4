class Temperature:
    """Represents a temperature value."""

    _valid_units = ("C", "F", "K")

    def __init__(self, value: float, unit: str = "C", tolerance: float = 1e-9):
        """Initializes a temperature object."""
        self._value = value
        self._unit = unit.upper()
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

    def convert_to(self, target_unit: str) -> Temperature:
        """ """
        target_unit = target_unit.upper()
        if target_unit not in self._valid_units:
            raise ValueError(F"Invalid target unit: {target_unit}. Valid units are: {self._valid_units}")

        if target_unit == "C":
            new_value = self.to_celsius
        elif target_unit == "F":
            new_value = self.to_fahrenheit
        elif target_unit == "K":
            new_value = self.to_kelvin
        return Temperature(new_value(), target_unit, self.tolerance)

    def __repr__(self) -> str:
        """Returns a representation of the temperature."""
        return f"Temperature({self.value}, '{self.unit}')"

    def __str__(self) -> str:
        """ returns a readable string representation of the temperature."""
        return f"{self.value} °{self.unit}" if self.unit in ("C", "F") else f"{self.value} K"


t = Temperature(25, "C")
print(t.convert_to("f"))   # 77.0 °F
print(t.convert_to("k"))   # 298.15 K
print(t.convert_to("C"))
print(t.convert_to("X"))   # 25.0 °C

print(repr(t))  # 25.0 °C