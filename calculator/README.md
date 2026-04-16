# Calculator Project

A simple Python calculator with basic arithmetic operations.

## Features

- **Addition**: Add two numbers
- **Subtraction**: Subtract one number from another
- **Multiplication**: Multiply two numbers
- **Division**: Divide one number by another with zero-division error handling

## Usage

```python
from calculator import Calculator

calc = Calculator()
print(calc.add(5, 3))        # Output: 8
print(calc.subtract(10, 4))  # Output: 6
print(calc.multiply(3, 7))   # Output: 21
print(calc.divide(10, 2))    # Output: 5.0
```

## Error Handling

The `divide` method raises a `ValueError` when attempting to divide by zero:

```python
try:
    result = calc.divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Cannot divide by zero
```

## Testing

Run the test suite using pytest:

```bash
pytest test_calculator.py -v
```

## Installation

Install pytest if you haven't already:

```bash
pip install pytest
```
