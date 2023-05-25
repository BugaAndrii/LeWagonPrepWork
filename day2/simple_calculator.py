def simple_calculator(array):
    """
    A simple calculator function that operates on an array with three elements: [operand1, operator, operand2].

    Parameters:
    array (list): A list containing two operands and an operator. Operands must be numbers or convertible to float.
                  Operator must be one of the following: "+", "-", "*", "/", "%".

    Returns:
    float: The result of the operation if successful.
    str: An error message if the calculation is unsuccessful (invalid input or zero division).
    """

    # Check if the input array has the correct format
    if len(array) != 3:
        return "Please enter valid format: [Operand, Operator, Operand]"

    # Unpack the array into operands and operator
    operand1, operator, operand2 = array

    # Define a dictionary mapping operators to their respective operations
    operations = {
        "+": float.__add__,  # Addition
        "-": float.__sub__,  # Subtraction
        "*": float.__mul__,  # Multiplication
        "/": float.__truediv__,  # Division
        "%": float.__mod__  # Modulus
    }

    try:
        # Convert operands to float
        operand1, operand2 = float(operand1), float(operand2)

        # Perform the operation
        result = operations[operator](operand1, operand2)
    except (ValueError, KeyError, ZeroDivisionError):
        # Return an error message for invalid input or zero division
        return "Please enter a valid operator [ +, -, /, *, % ]"

    # Return the result of the operation
    return result


if __name__ == "__main__":
    # Test simple_calculator function
    print(simple_calculator(['5', '+', '5']))
    print(simple_calculator(['10.5', '-', '5']))
    print(simple_calculator(['8', '*', '8']))
    print(simple_calculator(['1', '/', '4']))
    print(simple_calculator(['9', '%', '2']))
    print(simple_calculator(['1', '4']))
    print(simple_calculator(['1', '4', '5', '+']))
    print(simple_calculator(['1', '&', '5']))
