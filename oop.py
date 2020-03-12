# Python Object-Oriented Programming

# Class variables are variables that are shared among all instances of a class
# So, class variables should be the same for each instance
# A class is a blueprint for creating instances
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1 # Every employee created will be iterated when a new employee is created

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # @classmethod # Class method will apply to entire class, not just one instance
    # def set_raise_amt(cls, amount):
    #     cls.raise_amt = amount
    #
    # @classmethod
    # def from_string(cls, emp_str):
    #     first, last, pay = emp_str.split('-')
    #     return cls(first, last, pay)
    #
    # @staticmethod # Don't take instance or class as first arg, a good indicator that a method should be static is if you don't access the instance/class within the function
    # def is_workday(day):
    #     if day.weekday() == 5 or day.weekday() == 6:
    #         return False
    #     return True

class Developer(Employee): # Inheriting from employee class
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # super().__init__ brings in the attributes from employee class
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())



dev_1 = Developer('Corey', 'Schaeffer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(issubclass(Manager, Developer))
print(issubclass(Developer, Employee))
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))
