calories = {
    "Hamburger": 250,
    "Cheese Burger": 300,
    "Big Mac": 540,
    "McChicken": 350,
    "French Fries": 230,
    "Salad": 15,
    "Coca Cola": 150,
    "Sprite": 150,
}


def poor_calories_counter(item1, item2, item3):
    """
    Calculate the total number of calories for three items of order from the McDonald's menu.

    Parameters:
    item1, item2, item3 (str): The names of the items in the order.

    Returns:
    int: The total number of calories if all items are found in the menu.
    str: An error message if any item is not found in the menu.
    """

    try:
        # Calculate the total number of calories
        total_calories = calories[item1] + calories[item2] + calories[item3]
    except KeyError as e:
        # Return an error message if an item is not found in the menu
        return f"{e.args[0]} not found"

    return total_calories


if __name__ == "__main__":
    # Testing for poor_calories_counter counter
    print(poor_calories_counter("Big Mac", "Salad", "Shrimp Po Boy"))
    print(poor_calories_counter("McChicken", "French Fries", "Sprite"))
    print(poor_calories_counter("Hamburger", "Cheese Burger", "Big Mac"))
