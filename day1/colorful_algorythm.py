def is_colorful(number):
    """
    Check if a number is colorful.

    A colorful number is a number where all the products of subsets of its digits are different.

    Args:
        number (int): The number to be checked for colorfulness.

    Returns:
        bool: True if the number is colorful, False otherwise.
    """
    # Convert the number into a list of digits
    str_number = str(number)
    digits = [int(digit) for digit in str_number]

    # Initialize an empty set to store products of subsets
    products = set()

    # Generate all contiguous subsets of the digits
    for i, _ in enumerate(digits):
        for n, _ in enumerate(digits[i:], start=i):
            # Calculate the product of the current subset
            product = 1
            for digit in digits[i:n + 1]:
                product *= digit

            # If this product is already in the set, the number is not colorful
            if product in products:
                return False

            # Add the product to the set of products
            products.add(product)

    # If we haven't returned False by now, all products are different, so the number is colorful
    return True


if __name__ == "__main__":
    # Test the is_colorful function
    print(is_colorful(263))
