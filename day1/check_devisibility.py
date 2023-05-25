def check_divisibility(num, a, b):
    """
    Check if a number is divisible by both a and b.

    Args:
        num (int): The number to be checked for divisibility.
        a (int): The first divisor.
        b (int): The second divisor.

    Returns:
        bool: True if num is divisible by both a and b, False otherwise.
    """
    return num % a == 0 and num % b == 0


if __name__ == "__main__":
    # Test the check_divisibility function
    print(check_divisibility(12, 3, 4))
