def roman_to_int(s):
    """
    Convert a Roman numeral to an integer.

    Parameters:
    s (str): The Roman numeral.

    Returns:
    int: The integer corresponding to the Roman numeral.
    """

    # Define the conversion mapping from Roman numerals to integers
    roman_to_int_dict = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "VI": 6,
        "VII": 7,
        "VIII": 8,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "D": 500,
        "M": 1000,
        "CD": 400,
        "CM": 900
    }

    # Initialize the result
    result = 0
    i = 0

    while i < len(s):
        # Try to match two-character Roman numerals
        if i + 1 < len(s) and s[i:i + 2] in roman_to_int_dict:
            result += roman_to_int_dict[s[i:i + 2]]
            i += 2
        # Fallback to single-character Roman numerals
        else:
            result += roman_to_int_dict[s[i]]
            i += 1

    return result


if __name__ == "__main__":
    # Testing for roman_to_int function
    print(roman_to_int("VI"))
    print(roman_to_int("XI"))
