def fizz_buzz(n):
    """
    Generate a list of numbers from 1 to n with the following rules:
    - If the number is divisible by 3, replace it with 'Fizz'
    - If the number is divisible by 5, replace it with 'Buzz'
    - If the number is divisible by both 3 and 5, replace it with 'FizzBuzz'

    Parameters:
    n (int): The upper limit of the range.

    Returns:
    list: The list of numbers from 1 to n following the FizzBuzz rules.
    """

    # Initialize the result list
    result = []

    # Loop through numbers from 1 to n
    for i in range(1, n + 1):
        # Check divisibility by 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(i)

    return result


if __name__ == "__main__":
    # Test fizz_buzz function
    print(fizz_buzz(6))
