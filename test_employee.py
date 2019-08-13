import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        first_name = 'max'
        last_name = 'sallam'
        annual_salary = 36000
        self.employee_number_14386 = Employee(first_name, last_name, annual_salary)
        self.ultimate_raise = 39000

    def test_give_default_raise(self):
        self.employee_number_14386.give_raise()
        self.assertEqual('41000', self.employee_number_14386.show_salary())

    def test_give_custom_raise(self):
        self.employee_number_14386.give_raise(self.ultimate_raise)
        self.assertEqual('75000', self.employee_number_14386.show_salary())

unittest.main()