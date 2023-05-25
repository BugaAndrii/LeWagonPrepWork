class Student:
    def __init__(self, name, fives, tens, twenties):
        """Constructor for the Student class.

        Args:
        name (str): Name of the student.
        fives (int): Number of five euro bills.
        tens (int): Number of ten euro bills.
        twenties (int): Number of twenty euro bills.
        """
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def wealth(self):
        """Returns the total wealth of the student.

        Returns:
        int: The total wealth of the student.
        """
        return self.fives * 5 + self.tens * 10 + self.twenties * 20

    def compare(self, other_student):
        """Compares the wealth of two students.

        Args:
        other_student (Student): Another instance of a Student to compare with.

        Returns:
        str: The name of the student who has more wealth.
        """
        if self.wealth() > other_student.wealth():
            return self.name
        else:
            return other_student.name

    def advanced_compare(self, students_list):
        """Sorts a list of Students (including self) based on their wealth in descending order."""
        students_list.append(self)  # Append self to the list
        students_list.sort(key=lambda student: student.wealth(), reverse=True)
        return [student.name for student in students_list]


if __name__ == "__main__":
    # Testing for Student class
    student1 = Student("Alice", 3, 2, 1)
    student2 = Student("Bob", 2, 4, 3)
    student3 = Student("Charlie", 1, 3, 5)
    print(student1.compare(student2))
    student_list = [student1, student2, student3]
    print(student1.advanced_compare(student_list))
