class Employee:
    raise_amount = 1.04

    def __init__(self, first, last): 
        self.first = first
        self.last = last 
        
    @property
    def fullname(self):
        return self.first + " " + self.last
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @fullname.deleter
    def fullname(self):
        print("Delete name!")
        self.first = None
        self.last = None


emp_1 = Employee("John", "Smith")

emp_1.first = "Ilia"

emp_1.fullname = "Sam Bilbo"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname