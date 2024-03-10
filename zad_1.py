from Studnet import Student


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50

if __name__ == '__main__':

    student1 = Student("Jan Kowalski", [60, 70, 80, 90, 95])
    student2 = Student("Anna Nowak", [40, 30, 45, 55, 48])

    result1 = student1.is_passed()
    result2 = student2.is_passed()

    print(f"{student1.name}: Zaliczenie {result1}")
    print(f"{student2.name}: Zaliczenie {result2}")
