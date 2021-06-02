import unittest
from functions_to_test import Calculator


class UnitTestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Calculator.add(7, 7), 14)
        self.assertEqual(Calculator.add(0, 0), 0)
        self.assertEqual(Calculator.add(5.3, 7.7), 13)
        self.assertRaises(TypeError, Calculator.add, "7", 5)
        self.assertRaises(TypeError, Calculator.add, [3], {1})

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(7, 7), 0)
        self.assertEqual(Calculator.subtract(-1, 0), -1)
        self.assertEqual(Calculator.subtract(63.5, 7.7), 55.8)
        self.assertRaises(TypeError, Calculator.subtract, "7", -7)
        self.assertRaises(TypeError, Calculator.subtract, [8], {5})

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(7, 7), 49)
        self.assertEqual(Calculator.multiply(-1, 0), 0)
        self.assertEqual(Calculator.multiply(9, 7.7), 69.3)
        self.assertEqual(Calculator.multiply("7", 7), "7777777")
        self.assertRaises(TypeError, Calculator.multiply, [8], {5})

    def test_divide(self):
        self.assertEqual(Calculator.divide(7, 7), 1)
        self.assertEqual(Calculator.divide(-1, -1), 1)
        self.assertEqual(Calculator.divide(49, 7), 7)
        self.assertEqual(Calculator.divide(14, 7), 2)
        self.assertRaises(TypeError, Calculator.divide, [8], {5})
        self.assertRaises(TypeError, Calculator.divide, "77", 2)
        self.assertRaises(ValueError, Calculator.divide, 3, 0)


if __name__ == '__main__':
    unittest.main()
