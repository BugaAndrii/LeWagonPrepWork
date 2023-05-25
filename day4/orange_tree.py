import random


class OrangeTree:
    """This class represents an orange tree which can age, grow in height, bear fruits, and eventually die."""

    def __init__(self):
        """The constructor method initializes the orange tree with its basic attributes."""
        self.age = 0  # The tree is planted at age 0
        self.height = 0  # The tree starts with a height of 0 meters
        self.fruits = 0  # The tree has no fruits when it is planted
        self.dead = False  # The tree is initially alive

    def one_year_passes(self):
        """
        This method simulates the passing of one year in the life of the tree.
        It increases the age and height, updates the number of fruits and checks if the tree is dead.
        """
        if self.dead:
            # If the tree is dead, it cannot age, grow or bear fruits
            return

        # The tree ages by one year
        self.age += 1

        # The tree grows 1 meter each year until it is 10 years old
        if self.age <= 10:
            self.height += 1

        # The tree bears 100 fruits when it is between 6 and 9 years old (inclusive)
        if 5 < self.age < 10:
            self.fruits = 100
        # The tree bears 200 fruits when it is between 10 and 14 years old (inclusive)
        elif 10 <= self.age < 15:
            self.fruits = 200
        else:
            # The tree does not bear fruits outside these age ranges
            self.fruits = 0

        # The tree dies when it reaches 100 years
        if self.age == 100:
            self.dead = True
        # The tree has a chance to die when it is over 50 years old
        elif self.age > 50:
            self.dead = random.random() < 0.1

    def pick_a_fruit(self):
        """
        This method simulates picking a fruit from the tree.
        It decreases the number of fruits by one if there is at least one fruit.
        """
        if self.fruits > 0:
            self.fruits -= 1


if __name__ == "__main__":
    # Testing for OrangeTree class
    test_tree = OrangeTree()
    print(test_tree.age)
    print(test_tree.height)
    print(test_tree.fruits)
    print(test_tree.dead)

    test_tree.one_year_passes()

    print(test_tree.age)
    print(test_tree.height)
    print(test_tree.fruits)
    print(test_tree.dead)
    for _ in range(9):
        test_tree.one_year_passes()
    print(test_tree.age)
    print(test_tree.height)
    print(test_tree.fruits)
    print(test_tree.dead)
    test_tree.pick_a_fruit()
    print(test_tree.fruits)
    for _ in range(90):
        test_tree.one_year_passes()

    print(test_tree.age)
    print(test_tree.dead)
