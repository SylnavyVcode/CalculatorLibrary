"""
Unit tests for the calculator library
"""

import calculator

print(calculator.add(1, 2))
data = {
    "addition": [
        {
        "inputs": (2, 2),
        "expected": 4
        },
        {
        "inputs": (3, 5),
        "expected": 8
        },
        {
        "inputs": (12, 1),
        "expected": 13
        }

    ],
    "subtraction": [
        {
        "inputs": (4, 2),
        "expected": 2
    },
    {
        "inputs": (10, 2),
        "expected": 8
    },
    {
        "inputs": (3, 8),
        "expected": -5
    }
    ],
    "multiplication": [
        {
        "inputs": (2, 2),
        "expected": 4
    },
    {
        "inputs": (3, 5),
        "expected": 15
    },
    {
        "inputs": (12, 1),
        "expected": 12
    }
    ]
}

class TestCalculator:

    def test_addition(self):
        for i, case in enumerate(data["addition"]):
            assert case["expected"] == calculator.add(*case["inputs"])

    def test_subtraction(self):
        for i, case in enumerate(data["subtraction"]):
            assert case["expected"] == calculator.subtract(*case["inputs"])

    def test_multiplication(self):
        for i, case in enumerate(data["multiplication"]):
            assert case["expected"] == calculator.multiply(*case["inputs"])