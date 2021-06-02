from employee import Employee
import unittest
from unittest.mock import patch


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.test_data = Employee("Mariia", "Horbova", 2200)

    def test_email(self):
        self.assertEqual(self.test_data.email, "Mariia.Horbova@email.com")

    def test_full_name(self):
        self.assertEqual(self.test_data.fullname, "Mariia Horbova")

    def test_pay(self):
        self.test_data.apply_raise()
        self.assertEqual(self.test_data.pay, 2310)

    @patch("employee.requests.get")
    def test_monthly_schedule(self, mock_get):
        mock_get.return_value.ok = True
        mock_get.return_value.text = "ok = true"
        response = self.test_data.monthly_schedule("April")
        print(response)
        self.assertEqual(response, "ok = true")
        mock_get.return_value.ok = False
        response = self.test_data.monthly_schedule("April")
        print(response)
        self.assertEqual(response, "Bad Response!")


if __name__ == "__main__":
    unittest.main()
