import unittest
from functions_to_test import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(1, 2), 3)
        self.assertEqual(Calculator.add(0, 0), 0)
        self.assertEqual(Calculator.add(-3, -2), -5)
        self.assertEqual(Calculator.add(0.0, -7.0), -7.0)
        self.assertEqual(Calculator.add(-3, 6.0), 3)
        self.assertEqual(Calculator.add("4", "5"), "45")
        self.assertNotEqual(Calculator.add(5, 5), 9)
        with self.assertRaises(TypeError):
            Calculator.add(4, "56")

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(6, 2), 4)
        self.assertEqual(Calculator.subtract(0, 0), 0)
        self.assertEqual(Calculator.subtract(-3, -4), 1)
        self.assertEqual(Calculator.subtract(6.25, 3.05), 3.20)
        self.assertEqual(Calculator.subtract(6, 5.5), 0.5)
        self.assertNotEqual(Calculator.subtract(5, -5), 1)
        with self.assertRaises(TypeError):
            Calculator.subtract("5", "2")
            Calculator.subtract("9", 7)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(0, 0), 0)
        self.assertEqual(Calculator.multiply(0, -3), 0)
        self.assertEqual(Calculator.multiply(-5, 6), -30)
        self.assertEqual(Calculator.multiply(8, 4), 32)
        self.assertEqual(Calculator.multiply(-9, -1), 9)
        self.assertEqual(Calculator.multiply("5", 4), "5555")
        self.assertEqual(Calculator.multiply(0.5, 8), 4)
        self.assertEqual(Calculator.multiply(0.5, 0.5), 0.25)
        self.assertNotEqual(Calculator.multiply(2, 7), 13)

    def test_divide(self):
        self.assertEqual(Calculator.divide(0, 6), 0)
        self.assertEqual(Calculator.divide(9, 3), 3)
        self.assertEqual(Calculator.divide(-35, -5), 7)
        self.assertEqual(Calculator.divide(9, -3), -3)
        self.assertEqual(Calculator.divide(5.5, 5), 1.1)
        self.assertNotEqual(Calculator.divide(4, 2), 8)
        with self.assertRaises(ValueError):
            Calculator.divide(2, 0)
            Calculator.divide(-3, 0)
            Calculator.divide(6.8, 0)
            Calculator.divide(5, 0.0)
        with self.assertRaises(TypeError):
            Calculator.divide("54", "k")
            Calculator.divide("4", 5)
            Calculator.divide(4, "5")
            Calculator.divide("2", 0)


if __name__ == "__main__":
    unittest.main()
