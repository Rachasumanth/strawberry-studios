import pytest
from calculator import Calculator


class TestCalculator:
    """Test cases for the Calculator class."""

    @pytest.fixture
    def calc(self):
        """Fixture to provide a Calculator instance."""
        return Calculator()

    def test_add(self, calc):
        """Test addition operation."""
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(0, 0) == 0

    def test_subtract(self, calc):
        """Test subtraction operation."""
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(0, 5) == -5
        assert calc.subtract(5, 5) == 0

    def test_multiply(self, calc):
        """Test multiplication operation."""
        assert calc.multiply(3, 4) == 12
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(0, 100) == 0

    def test_divide(self, calc):
        """Test division operation."""
        assert calc.divide(10, 2) == 5
        assert calc.divide(7, 2) == 3.5
        assert calc.divide(-10, 2) == -5

    def test_divide_by_zero(self, calc):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

