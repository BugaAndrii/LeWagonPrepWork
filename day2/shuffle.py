import random


def manual_shuffle(array):
    """
    Shuffle a list and return a new list with all the items of the original list in a new, randomized order.

    Parameters:
    lst (list): The original list.

    Returns:
    list: The shuffled list.
    """
    # Copy the original list to avoid altering it
    original_array = array.copy()
    shuffled_array = []

    # Loop until the original list is empty
    while original_array:
        # Randomly select an index
        idx = random.randrange(len(original_array))

        # Append the element at that index to the shuffled list
        shuffled_array.append(original_array[idx])

        # Delete the element at that index from the original list
        original_array.pop(idx)

    return shuffled_array


if __name__ == "__main__":
    # Testing manual_shuffle function
    print(manual_shuffle(list(range(101))))
