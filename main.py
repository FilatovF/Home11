"""Task 1"""

class Person:
    def __init__(self, name, lastname, age, phonenumber):
        self.phonenumber = phonenumber
        self.age = age
        self.lastname = lastname
        self.name = name

    def info(self):
        print(f'name: {self.name}\n'
              f'lasname: {self.lastname}\n'
              f'age: {self.age}\n'
              f'phonenumber: {self.phonenumber}\n')


class Teacher(Person):
    def __init__(self, name, lastname, age, phonenumber, payment):
        super().__init__(name, lastname, age, phonenumber)
        self.payment = payment

    def full_info(self):
        self.info()
        print(f'payment:{self.payment}\n')


class Student(Person):
    def __init__(self, name, lastname, age, phonenumber, prof):
        super().__init__(name, lastname, age, phonenumber)
        self.prof = prof

    def full_info(self):
        self.info()
        print(f"prof: {self.prof}")


filatov = Student("Fedor", "Filatov", 21, "0679800700", "engineer")
gura = Teacher("Tetyana", "Gura", 33, "0678600700", 1000)
gura.info()
gura.full_info()
filatov.info()
filatov.full_info()

"""Task2"""


class Mathematician:
    def __init__(self):
        pass

    def square_nums(self, some_list):
        self.some_list = some_list
        squar_list = [num * num for num in self.some_list]
        return squar_list

    def remove_positives(self, some_list):
        self.some_list = some_list
        new_list = [num for num in self.some_list if num < 0]
        return new_list

    def filter_leaps(self, some_list):
        self.some_list = some_list
        new_list = [num for num in self.some_list if num % 4 == 0 and num % 100 != 0 or num % 400 == 0 and num % 4 == 0]
        return new_list


m = Mathematician()
print(m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16])
print(m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90])
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020])

"""Task4"""

class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open(file="myfile.txt", mode="w") as file:
            file.write(msg)

error = CustomException("OMG WHAT ARE YOU DOING???")
raise error
