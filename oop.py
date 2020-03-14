class Employee:

    raise_amt = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # def apply_raise(self):
    #     self.pay = int(self.pay * self.raise_amt)
    #
    # def __repr__(self):
    #     return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    #
    # def __str__(self):
    #     return '{} - {}'.format(self.fullname(), self.email)
    #
    # def __add__(self, other):
    #     return self.pay + other.pay
    #
    # def __len__(self):
    #     return len(self.fullname())

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Corey Schaeffer'

# emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1 + emp_2)

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
# print(emp_1.fullname())
