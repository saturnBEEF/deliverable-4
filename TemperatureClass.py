class Temperature:
    """Represents a temperature value."""
    _tolerance = 1e-9
    _valid_units = ("C", "F", "K")

    def __init__(self, value: float, unit: str = "C"):
        """Initializes a temperature object."""
        unit = unit.upper()
        if unit not in self._valid_units:
            raise ValueError(F"Invalid unit: {unit}. Valid units are: {self._valid_units}")

        value = float(value)
        kelvin = self._to_kelvin(value, unit)
        if kelvin < self._tolerance:
            raise ValueError("Temperature in Kelvin cannot be negative.")

        self._value = value
        self._unit = unit

    def _to_kelvin(self, value: float, unit: str) -> float:
        """Check for negative kelvin value."""
        if unit == "K":
            return value
        elif unit == "C":
            return value + 273.15
        elif unit == "F":
            return (value - 32) * (5 / 9) + 273.15

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
        return self._to_kelvin(self.value, self.unit)

    def convert_to(self, target_unit: str) -> Temperature:
        """Converts the temperature to the target unit."""

        target_unit = target_unit.upper()
        if target_unit not in self._valid_units:
            raise ValueError(F"Invalid target unit: {target_unit}. Valid units are: {self._valid_units}")

        conversion = {
            "C": self.to_celsius,
            "F": self.to_fahrenheit,
            "K": self.to_kelvin
        }
        return Temperature(conversion[target_unit](), target_unit)

    def __repr__(self) -> str:
        """Returns a representation of the temperature."""
        return f"Temperature({self.value:.1f}, '{self.unit}')"

    def __str__(self) -> str:
        """ returns a readable string representation of the temperature."""
        return f"{self.value:.2f}°{self.unit}" if self.unit in ("C", "F") else f"{self.value:.2f} K"


t = Temperature(-25, "c")
print(t.convert_to("f"))
print(t.convert_to("k"))   
print(t.convert_to("C"))
#print(t.convert_to("X"))   

print(repr(t))  
print(str(t))

