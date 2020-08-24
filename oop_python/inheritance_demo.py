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
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee): 
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee): 

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None: 
            self.employees = []
        else: 
            self.employees = employees 

    def add_employee(self, emp):
        if emp not in self.employees: 
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees: 
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees: 
            print("-->", emp.get_full_name())

emp_1 = Employee("Ilia", "Valkov", 200000)

dev_2 = Developer("Tsvetan", "Valkov", 200000, "java")

# 1 

# print(dev_2.email)

# 2

# print(dev_2.pay)
# dev_2.apply_raise()
# print(dev_2.pay)

# print(dev_2.email)
# print(dev_2.prog_lang)

# 3

mgr_1 = Manager("Sue", "Smith", 90000,[emp_1])

# print(mgr_1.email)

# mgr_1.print_emps()

# mgr_1.add_employee(dev_2)

# mgr_1.print_emps() 

# mgr_1.remove_employee(emp_1)

# mgr_1.print_emps() 

# 4
print(isinstance(mgr_1, Employee))


print(isinstance(Manager, Employee))