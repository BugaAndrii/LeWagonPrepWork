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

# Defining the items for each meal
meals = {
    "Happy Meal": ["Cheese Burger", "French Fries", "Coca Cola"],
    "Best Of Big Mac": ["Big Mac", "French Fries", "Coca Cola"],
    "Best Of McChicken": ["McChicken", "Salad", "Sprite"],
}


def advanced_calories_counter(orders):
    """
    Calculate the total number of calories for a list of orders from the McDonald's menu.

    Parameters:
    orders (list): The list of meals and individual items in the order.

    Returns:
    int: The total number of calories if all items and meals are found in the menu.
    str: An error message if any item or meal is not found in the menu.
    """

    total_calories = 0

    for order in orders:
        if order in meals:
            # If the order is a meal, add the calories for each item in the meal
            for item in meals[order]:
                try:
                    total_calories += calories[item]
                except KeyError:
                    return f"{item} not found in meal {order}"
        else:
            # If the order is an individual item, add its calories
            try:
                total_calories += calories[order]
            except KeyError:
                return f"{order} not found"

    return total_calories


if __name__ == "__main__":
    # Testing for advanced_calories_counter function
    print(advanced_calories_counter(["Big Mac", "French Fries", "Happy Meal", "Coca Cola"]))
    print(advanced_calories_counter(["Fish and Chips", "Salad"]))
