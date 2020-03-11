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
        self.pay = int(self.pay * self.raise_amount)

    @classmethod # Class method will apply to entire class, not just one instance
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod # Don't take instance or class as first arg, a good indicator that a method should be static is if you don't access the instance/class within the function
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Corey', 'Schaeffer', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2020, 3, 10)

print(Employee.is_workday(my_date))
