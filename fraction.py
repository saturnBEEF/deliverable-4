import math


class Fraction:
    """Represents a mathematical fraction with an integer numerator and denominator.

    Attributes:
        numerator (int): The numerator (top number) of the fraction.
        denominator (int): The strictly positive (> 0) denominator (bottom number).
    """

    def __init__(self, numerator: int, denominator: int = 1) -> None:
        """Initializes a Fraction object and simplifies it to lowest terms.

        Args:
            numerator (int): The numerator of the fraction.
            denominator (int, optional): The denominator (> 0). Defaults to 1.

        Raises:
            TypeError: If numerator or denominator are not integers.
            ValueError: If the denominator is less than or equal to 0.
        """
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Both numerator and denominator must be integers.")

        if denominator <= 0:
            raise ValueError("Denominator must be strictly positive (> 0).")

        # Simplify fraction using greatest common divisor
        common_divisor = math.gcd(abs(numerator), denominator)
        self._numerator = numerator // common_divisor
        self._denominator = denominator // common_divisor

    @property
    def numerator(self) -> int:
        """Returns the simplified numerator."""
        return self._numerator
    
    @property
    def denominator(self) -> int:
        """Returns the simplified strictly positive denominator."""
        return self._denominator

    # --- String & Conversion Dunder Methods ---
    def __repr__(self) -> str:
        """Returns an unambiguous string representatino of the Fraction."""
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self) -> str:
        """Returns a readable string representation of the Fraction."""
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"

    def __float__(self) -> float:
        """Converts the Fraction to a floating-point number."""
        return self.numerator / self.denominator

    def __abs__(self) -> "Fraction":
        """Returns a new Fraction with the absolute value."""
        return Fraction(abs(self.numerator), self.denominator)

    def __neg__(self) -> "Fraction":
        """Returns a new Fraction with negated sign."""
        return Fraction(-self.numerator, self.denominator)

    # --- Arithmetic Dunder Methods ---
    def __add__(self, other: object) -> "Fraction":
        """Adds another Fraction or int to this fraction."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        num = (
            self.numerator * other.denominator + other.numerator * self.denominator
        )
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __radd__(self, other: object) -> "Fraction":
        """Handles reverse addition (e.g., int + Fraction)."""
        return self.__add__(other)

    def __sub__(self, other: object) -> "Fraction":
        """Subtracts another Fraction or int from this fraction."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        num = (
            self.numerator * other.denominator - other.numerator * self.denominator
        )
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __rsub__(self, other: object) -> "Fraction":
        """Handles reverse subtraction (e.g., int - Fraction)."""
        if isinstance(other, int):
            return Fraction(other, 1) - self
        return NotImplemented

    def __mul__(self, other: object) -> "Fraction":
        """Multiplies this Fraction or int with this fraction."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(
            self.numerator * other.numerator, self.denominator * other.denominator
        )

    def __rmul__(self, other: object) -> "Fraction":
        """Handles reverse multiplication (e.g., int * Fraction)."""
        return self.__mul__(other)

    def __truediv__(self, other: object) -> "Fraction":
        """Divides this fraction by another Fraction or int."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a fraction equal to zero.")

        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        if den <= 0:
            num = -num
            den = -den
        return Fraction(num, den)

    # --- All 6 Comparison Dunder Methods ---
    def __eq__(self, other: object) -> bool:
        """Checks equality (==)."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        return (
            self.numerator == other.numerator
            and self.denominator == other.denominator
        )

    def __ne__(self, other: object) -> bool:
        """Checks inequality (!=)."""
        eq = self.__eq__(other)
        if eq is NotImplemented:
            return NotImplemented
        return not eq

    def __lt__(self, other: object) -> bool:
        """Checks less than (<)."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other: object) -> bool:
        """Checks less than or equal to (<=)."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        return (
            self.numerator * other.denominator <= other.numerator * self.denominator
        )

    def __gt__(self, other: object) -> bool:
        """Checks greater than (>)."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other: object) -> bool:
        """Checks greater than or equal to (>=)."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        return (
            self.numerator * other.denominator >= other.numerator * self.denominator
        )