import pytest
from fraction import Fraction


def test_initialization_and_simplification():
  """Tests initialization, default denominator, and fraction simplification."""
  f = Fraction(2, 4)
  assert f.numerator == 1
  assert f.denominator == 2

  f_neg = Fraction(-3, 6)
  assert f_neg.numerator == -1
  assert f_neg.denominator == 2

  f_default = Fraction(5)
  assert f_default.numerator == 5
  assert f_default.denominator == 1

def test_invalid_initialization():
  """Tests that invalid inputs raise appropriate exceptions."""
  with pytest.raises(ValueError):
    Fraction(1, 0)
  with pytest.raises(ValueError):
    Fraction(1, -2)
  with pytest.raises(TypeError):
    Fraction(1.5, 2)  # type: ignore
  with pytest.raises(TypeError):
    Fraction(1, "2")  # type: ignore

def test_comparisons():
  """Tests all 6 comparison operators across fractions and integers."""
  f1 = Fraction(1, 2)
  f2 = Fraction(2, 4)
  f3 = Fraction(3, 4)

  assert f1 == f2
  assert f1 != f3
  assert f1 < f3
  assert f1 <= f2
  assert f3 > f1
  assert f3 >= f1

  # Comparison with int
  assert f1 == Fraction(1, 2)
  assert f3 > 0

def test_arithmetic_operations():
  """Tests addition, subtraction, multiplication, and division."""
  f1 = Fraction(1, 3)
  f2 = Fraction(1, 6)

  # Addition
  assert f1 + f2 == Fraction(1, 2)
  assert f1 + 1 == Fraction(4, 3)
  assert 1 + f1 == Fraction(4, 3)

  # Subtraction
  assert f1 - f2 == Fraction(1, 6)
  assert f1 - 1 == Fraction(-2, 3)

  # Multiplication
  assert f1 * f2 == Fraction(1, 18)
  assert f1 * 3 == Fraction(1, 1)

  # Division
  assert f1 / f2 == Fraction(2, 1)
  with pytest.raises(ZeroDivisionError):
    _ = f1 / Fraction(0, 1)

def test_other_dunder_methods():
  """Tests __str__, __repr__, __float__, __abs__, and __neg__."""
  f = Fraction(3, 4)
  f_neg = Fraction(-3, 4)

  assert str(f) == "3/4"
  assert str(Fraction(5, 1)) == "5"
  assert repr(f) == "Fraction(3, 4)"
  assert float(f) == 0.75
  assert abs(f_neg) == Fraction(3, 4)
  assert -f == Fraction(-3, 4)
