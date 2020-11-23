"""CSV Reader"""
import csv
from Fileutilities.absolutepath import absolute_path


def classFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []
        try:
            with open(absolute_path(filepath)) as text_data:
                csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)

        except OSError:
            print('Unable to open', filepath)

    def return_data_as_object(self, class_name):
        """Test"""
        objects = []
        for row in self.data:
            objects.append(classFactory(class_name, row))
        return objects
