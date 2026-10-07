"""
Calculator library containing basic math operations
"""
"""
Calculator library containing basic math operations.
"""

def add(first_term, second_term):
    return first_term + second_term

def subtract(first_term, second_term):
    return first_term - second_term

def multiply(first_term, second_term):
    return first_term * second_term

__all__ = ["add", "subtract", "multiply"]

if __name__ == "__main__":
    # Example usage
    result = add(1, 2)
    print(f"The sum is {result}.")
    result = subtract(10, 2)
    print(f"The difference is {result}.")
    result = multiply(3, 4)
    print(f"The product is {result}.")