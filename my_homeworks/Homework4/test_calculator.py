import unittest
from functions_to_test import Calculator


calculator = Calculator


class TestFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(5, 1), 6)
        self.assertEqual(calculator.add(2, 3.0), 5)
        self.assertNotEqual(calculator.add(3.5, 2), 5)
        self.assertEqual(calculator.add('54', '42'), '5442')
        self.assertEqual(calculator.add([1, 2, 3], [1, 4, 9]), [1, 2, 3, 1, 4, 9])
        with self.assertRaises(TypeError):
            calculator.add(4, '23')
            calculator.add(1, {2})
            calculator.add(1, [6])
            calculator.add(1, (1, 2))

    def test_subtract(self):
        self.assertEqual(calculator.subtract(1, 2), -1)
        self.assertEqual(calculator.subtract(2, 2.0), 0)
        self.assertEqual(calculator.subtract(1, 2), -1)
        with self.assertRaises(TypeError):
            assert calculator.subtract(4, '1')
            assert calculator.subtract([1, 2, 3, 4], [1, 2])

    def test_multiply(self):
        self.assertEqual(calculator.multiply(6, 7), 42)
        self.assertEqual(calculator.multiply(5, '4'), '44444')
        with self.assertRaises(TypeError):
            calculator.multiply(2, {2, 4, 7})

    def test_divide(self):
        self.assertTrue(calculator.divide(15, 1) == 15)
        self.assertEqual(calculator.divide(49, 7), 7)
        with self.assertRaises(ValueError):
            calculator.divide(15, 0)
        with self.assertRaises(TypeError):
            calculator.divide(4, '2')
            calculator.divide([1, 2, 3, 1, 2, 3], [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
