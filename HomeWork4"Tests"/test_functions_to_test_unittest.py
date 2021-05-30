from functions_to_test import Calculator
import unittest


class TestCalculator(unittest.TestCase):
    def test_add(self):
        i = 0
        self.assertEqual(Calculator.add(i, i), 0)
        self.assertEqual(Calculator.add(20, i), 20)
        self.assertEqual(Calculator.add(5, 5), 10)
        self.assertEqual(Calculator.add(-2, 4), 2)
        self.assertEqual(Calculator.add(0.5, 0.5), 1)
        self.assertRaises(TypeError, Calculator.add, 'maks', 3)

    def test_sub(self):
        self.assertEqual(Calculator.subtract(5, 4), 1)
        self.assertEqual(Calculator.subtract(3.1, 0.1), 3)
        self.assertEqual(Calculator.subtract(-1, 1), -2)

    def test_mul(self):
        self.assertEqual(Calculator.multiply(3, 5), 15)
        self.assertEqual(Calculator.multiply(3, 0.33), 0.99)
        self.assertEqual(Calculator.multiply('Maks', 3), 'MaksMaksMaks')

    def test_div(self):
        self.assertEqual(Calculator.divide(25, 5), 5)
        self.assertEqual(Calculator.divide(-24, 4), -6)
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)
            Calculator.divide(1.3, 0)
            Calculator.divide(-10, 0)


if __name__ == '__main__':
    unittest.main()
