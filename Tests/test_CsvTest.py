import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.addition(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)
        test_data = CsvReader('Tests/Data/Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.addition(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtraction(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)
        test_data = CsvReader('Tests/Data/Subtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtraction(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiplication(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)
        test_data = CsvReader('Tests/Data/Multiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiplication(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.division(2, 2), 1)
        self.assertEqual(self.calculator.result, 1)
        test_data = CsvReader('Tests/Data/Division.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.division(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(2), 4)
        self.assertEqual(self.calculator.result, 4)
        test_data = CsvReader('Tests/Data/Square.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_root_method_calculator(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.result, 2)
        test_data = CsvReader('Tests/Data/SquareRoot.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.sqrt(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)


if __name__ == '__main__':
    unittest.main()
