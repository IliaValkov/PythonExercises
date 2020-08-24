# Python Object-Oriented Programming

# methods - a fn associated with a class 
# attributes - variables in the class 

# classes are blueprints for Instances

# dunder - double underscore

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first.lower() + "." + last.lower() + "@company.com"
    
    def get_full_name(self):
        return self.first + " " + self.last

    def apply_raise(self): 
        sel.pay = int(self.pay * self.raise_amount)

    def __repr__(self): 
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.get_full_name(), self.email)

    def __add__(self, other): 
        return self.pay + other.pay

    def __len__(self): 
        return len(self.get_full_name())


emp_1 = Employee("Ilia", "Valkov", 90000)
emp_2 = Employee("Marin", "Valkov", 89999)

# print(repr(emp_1))
# print(str(emp_1))
    
# print(1 + 2)

# print(int.__add__(1,2))

# print(str.__add__("a","b"))

# print(emp_1 + emp_2)

print(len("test"))

print("test".__len__())

print(len(emp_1))

