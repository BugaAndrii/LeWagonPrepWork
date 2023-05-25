class Dessert:
    """
    Represents a dessert with a name and calorie information.
    """

    def __init__(self, name, calories):
        """
        Initialize a Dessert object.

        Args:
            name (str): The name of the dessert.
            calories (int): The calorie content of the dessert.
        """
        self.name = name
        self.calories = calories

    def healthy(self):
        """
        Check if the dessert is healthy based on its calorie content.

        Returns:
            bool: True if the dessert is healthy (calories < 200), False otherwise.
        """
        return self.calories < 200

    def delicious(self):
        """
        Check if the dessert is delicious.

        Returns:
            bool: Always returns True.
        """
        return True


class JellyBean(Dessert):
    """
    Represents a jelly bean, which is a type of dessert.
    """

    def __init__(self, name, calories, flavor):
        """
        Initialize a JellyBean object.

        Args:
            name (str): The name of the jelly bean.
            calories (int): The calorie content of the jelly bean.
            flavor (str): The flavor of the jelly bean.
        """
        super().__init__(name, calories)
        self.flavor = flavor

    def delicious(self):
        """
        Check if the jelly bean is delicious.

        Returns:
            bool: True if the flavor is not "black licorice", False otherwise.
        """
        if self.flavor == "black licorice":
            return False
        else:
            return super().delicious()


if __name__ == "__main__":
    # Testing for Dessert class
    print("Testing your Dessert methods")
    healthy_des = Dessert("cupcake", 100)
    print(healthy_des.healthy())
    unhealthy_des = Dessert("cake", 300)
    print(unhealthy_des.healthy())

    # Testing for JellyBean class
    print('Testing your JellyBean methods')
    delicious_des = JellyBean("yummy", 100, "cherry")
    print(delicious_des.delicious())
    gross_des = JellyBean("disgusting", 300, "black licorice")
    print(gross_des.delicious())
