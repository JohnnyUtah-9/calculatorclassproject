"""Test"""
import unittest
from CsvReader.CsvReader import CsvReader, classFactory


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        """Test"""
        abc = 2
        self.csv_reader = CsvReader('./Data/Addition.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_object('Value 1')
        self.assertIsInstance(people, list)
        test_class = classFactory('Value 1', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__)


if __name__ == '__main__':
    unittest.main()
