# Python Object-Oriented Programming

# methods - a fn associated with a class 
# attributes - variables in the class 

# classes are blueprints for Instances

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first.lower() + "." + last.lower() + "@company.com"
        Employee.num_of_emps += 1

    def get_full_name(self):
        return self.first + " " + self.last

    def apply_raise(self): 
        sel.pay = int(self.pay * self.raise_amount)

    @classmethod
    # sometimes can be used as alternative constructor methods
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    # for functions that have logical connections to the clas,
    # but dont access the class or instance data
    def is_workday(day): 
        if day.weekday() == 5 or day.weekday() == 6: 
            return False
        return True

emp1 = Employee("Ilia", "Valkov", 600000)

# print(emp1.get_full_name())
# print(Employee.get_full_name(emp1))

# print(emp1.raise_amount) 
# print(Employee.raise_amount)

# Accessing the namespace of the instance and the class
# print(emp1.__dict__)
# print(Employee.__dict__)

# print(Employee.num_of_emps)

print(emp1.raise_amount) 

Employee.set_raise_amount(1.05)

print(emp1.raise_amount) 

import datetime 
my_date = datetime.date(2020, 1, 31)

print(emp1.is_workday(my_date))