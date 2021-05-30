import unittest
from unittest.mock import patch
from employee import Employee


class MockTestTrue:
    text = 'response.ok = True'
    status_code = 200
    elapsed = 100
    ok = True

    def __init__(self, *args, **kwargs):
        pass


class MockTestFalse:
    text = 'response.ok = False'
    status_code = 400
    elapsed = 100
    ok = False

    def __init__(self, *args, **kwargs):
        pass


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee_1 = Employee('Tomas', 'Anderson', 120000)
        self.employee_2 = Employee('Morpheus', 'Nebuchadnezzar', 100000)
        self.employee_3 = Employee('Cypher', 'Reagan', 50000)
        self.employees = [self.employee_1, self.employee_2, self.employee_3]

    def test_email(self):

        for employee in self.employees:
            self.assertEqual(employee.email.lower(), f'{employee.first.lower()}.{employee.last.lower()}@email.com')

    def test_fullname(self):

        for employee in self.employees:
            self.assertEqual(employee.fullname.lower(), f'{employee.first.lower()} {employee.last.lower()}')

    def test_apply_raise(self):

        for employee in self.employees:
            employee_first_pay = employee.pay           # temporary variable to save the employee pay before raise
            employee.apply_raise()
            self.assertEqual(employee.pay, employee_first_pay*employee.raise_amt)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mocker):

        mocker.side_effect = MockTestTrue
        for employee in self.employees:
            self.assertEqual(employee.monthly_schedule('May'), 'response.ok = True')

        mocker.side_effect = MockTestFalse
        for employee in self.employees:
            self.assertEqual(employee.monthly_schedule('January'), 'Bad Response!')


if __name__ == '__main__':

    unittest.main()
