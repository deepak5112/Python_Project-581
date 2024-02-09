import pytest
from math_utils import MathUtils  # Assuming MathUtils is in math_utils.py

class TestMathUtils:
    def test_add(self):
        assert MathUtils.add(2, 3) == 5
        assert MathUtils.add(-1, 1) == 0
        assert MathUtils.add(-1, -1) == -2

    def test_subtract(self):
        assert MathUtils.subtract(5, 3) == 2
        assert MathUtils.subtract(-1, 1) == -2
        assert MathUtils.subtract(-1, -1) == 0

    def test_multiply(self):
        assert MathUtils.multiply(2, 3) == 6
        assert MathUtils.multiply(-1, 1) == -1
        assert MathUtils.multiply(-1, -1) == 1
        assert MathUtils.multiply(0, 100) == 0

    def test_divide(self):
        assert MathUtils.divide(6, 3) == 2.0
        assert MathUtils.divide(-1, 1) == -1.0
        assert MathUtils.divide(-1, -1) == 1.0
        assert MathUtils.divide(5, 0) == -1.0  # Testing division by zero

# Optional: Use pytest fixtures for setup and teardown if necessary
