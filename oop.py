# Python Object-Oriented Programming

# Class variables are variables that are shared among all instances of a class
# So, class variables should be the same for each instance
# A class is a blueprint for creating instances
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1 # Every employee created will be iterated when a new employee is created

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# Instances of Employee
# Instance variables can be unique for each instance

print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schaeffer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)

# print(employee.__dict__)

# emp_1.raise_amount = 1.05
#
# print(emp_1.__dict__)
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)



# emp_1.raise_amount
# Employee.raise_amount
