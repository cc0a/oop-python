# Python Object-Oriented Programming

# A class is a blueprint for creating instances
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# Instances of Employee
emp_1 = Employee('Corey', 'Schaeffer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_1.fullname()
print(Employee.fullname(emp_1))
