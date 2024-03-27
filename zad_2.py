class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

        def __str__(self):
            return f"Library: {self.city}, {self.street}, {self.zip_code}\nOpen Hours: {self.open_hours}\nPhone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

        def __str__(self):
            return f"Employee: {self.first_name} {self.last_name}\nHire Date: {self.hire_date}\nBirth Date: {self.birth_date}\nAddress: {self.city}, {self.street}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

        def __str__(self):
            return f"Book:\n{self.library}\nPublication Date: {self.publication_date}\nAuthor: {self.author_name} {self.author_surname}\nNumber of Pages: {self.number_of_pages}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

        def __str__(self):
            books_info = "\n".join([f"  {book}" for book in self.books])
            return f"Order:\n{self.employee}\n{self.student}\nBooks:{books_info}\nOrder Date: {self.order_date}"


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

    biblioteka1 = Library('Warszawa', '1 Maja', '22-240', '10', '11111111')
    biblioteka2 = Library('Katowice', 'Wolnosci', '22-240', '8', '11111111')

    ksiazka1 = Book(biblioteka1, '2000-09-11', 'Adam', 'Mickiewicz', 30)
    ksiazka2 = Book(biblioteka1, '1900-09-11', 'Adam', 'Mickiewicz', 800)
    ksiazka3 = Book(biblioteka2, '2010-11-13', 'Adam', 'Agata', 340)
    ksiazka4 = Book(biblioteka2, '2020-05-15', 'Adam', 'Juszcyk', 267)
    ksiazka5 = Book(biblioteka2, '2000-08-16', 'Adam', 'Krawiec', 890)

    prac1 = Employee('Dawid', 'Krakus', '2020-11-09', '2000-11-09', 'Katowice', 'Mickiewicza', '22-000', '111111111')
    prac2 = Employee('Dawid2', 'Krakus2', '2020-11-09', '2000-11-09', 'Katowice', 'Mickiewicza', '22-000', '111111111')
    prac3 = Employee('Dawid3', 'Krakus3', '2020-11-09', '2000-11-09', 'Katowice', 'Mickiewicza', '22-000', '111111111')

    order1 = Order(prac1, student1, [ksiazka5, ksiazka2, ksiazka1], '2024-01-05')
    order2 = Order(prac3, student2, [ksiazka3, ksiazka4, ksiazka1], '2024-01-05')

    print(order1)
    print(order2)
