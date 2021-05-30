from employee import Employee
import unittest
from unittest.mock import patch


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.test_employee1 = Employee('Maks', 'Sharko', 1010)
        self.test_employee2 = Employee("Vasya", "Vasov", 0)

    def test_email(self):
        self.assertEqual(self.test_employee1.email, 'Maks.Sharko@email.com')
        self.assertEqual(self.test_employee2.email, 'Vasya.Vasov@email.com')

    def test_fullname(self):
        self.assertEqual(self.test_employee1.fullname, 'Maks Sharko')
        self.assertEqual(self.test_employee2.fullname, 'Vasya Vasov')

    def test_apply_raise(self):
        self.test_employee1.apply_raise()
        self.assertEqual(self.test_employee1.pay, 1060)
        self.test_employee2.apply_raise()
        self.assertEqual(self.test_employee2.pay, 0)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mock1):
        mock1.return_value.ok = True
        self.assertEqual(self.test_employee1.monthly_schedule("April"), mock1().text)

        mock1.return_value.ok = False
        self.assertEqual(self.test_employee2.monthly_schedule("May"), "Bad Response!")


if __name__ == '__main__':
    unittest.main()
