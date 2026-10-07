"""
Calculator library containing basic math operations
"""

def add(*terms: int|float) -> int | float:
    """
    Adds a list of numbers together.

    Args:
        terms (tuple): A tuple of numbers to add.

    Returns:
        int|float: The sum of the numbers.
    """
    return sum(terms)

def substract(*terms: int|float) -> int | float:
    """
    Subtracts a list of numbers from the first number.

    Args:
        terms (tuple): A tuple of numbers to subtract.

    Returns:
        int|float: The result of the subtraction.
    """
    if not terms:
        return 0
    result = terms[0]
    for term in terms[1:]:
        result -= term
    return result

if __name__ == "__main__":
    # Example usage
    result = add(1, 2, 3, 4, 5)
    print(f"The sum is {result}.")
    result = substract(10, 2, 3)
    print(f"The difference is {result}.")