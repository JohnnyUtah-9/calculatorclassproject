"""Test"""
import unittest
from CsvReader.CsvReader import CsvReader
from Stats.Statistics import Statistics
from pprint import pprint


class MyTestCase(unittest.TestCase):
    test_data = CsvReader('Tests/Data/TestData').data
    column1 = [int(row['value1']) for row in test_data]
    column2 = [int(row['value2']) for row in test_data]
    p_answers = CsvReader('Tests/Data/Test_Proportional.csv').data
    z_answers = CsvReader('Tests/Data/Test_ZScores.csv').data
    column_proportion = [float(row['Proportion']) for row in p_answers]
    column_zscore = [float(row['Z-Score']) for row in z_answers]
    test_answer = CsvReader('Tests/Data/TestStatAnswers.csv').data
    sample_data = CsvReader('Tests/Data/DataSampleTest.csv').data
    column3 = [int(row['sample1']) for row in sample_data]
    sample_answer = CsvReader('Tests/Data/TestStatAnswers.csv').data

    def setUp(self) -> None:
        """Test"""
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_population_mean_statistics(self):
        for row in self.test_answer:
            pprint(row["mean"])
        self.assertEqual(self.statistics.population_mean(self.column1), float(self.row['mean']))
        self.assertEqual(self.statistics.result, float(self.row['mean']))

    def test_median_statistics(self):
        for row in self.test_answer:
            pprint(row["median"])
        self.assertEqual(self.statistics.median(self.column1), float(self.row['median']))
        self.assertEqual(self.statistics.result, float(self.row['median']))

    def test_mode_statistics(self):
        for row in self.test_answer:
            pprint(row["mode"])
        self.assertEqual(self.statistics.mode(self.column1), float(self.row['mode']))
        self.assertEqual(self.statistics.result, float(self.row['mode']))

    def test_standard_deviation_statistics(self):
        for row in self.test_answer:
            pprint(row["stddev"])
        self.assertEqual(self.statistics.stddev(self.column1), float(self.row['stddev']))
        self.assertEqual(self.statistics.result, float(self.row['stddev']))

    def test_proportion_variance_statistics(self):
        for row in self.test_answer:
            pprint(row['proportion_variance'])
        self.assertEqual(self.statistics.population_proportion_variance(self.column1),
                         float(self.row['proportion_variance']))
        self.assertEqual(self.statistics.result, float(self.row['proportion_variance']))

    def test_variance_statistics(self):
        for row in self.test_answer:
            pprint(row['variance'])
        self.assertEqual(self.statistics.variance(self.column1), float(self.row['variance']))
        self.assertEqual(self.statistics.result, float(self.row['variance']))

    def test_correlation_statistics(self):
        for row in self.test_answer:
            pprint(row['correlation'])
        self.assertEqual(self.statistics.correlation_coefficient(self.column1, self.column2),
                         float(self.row['correlation']))
        self.assertEqual(self.statistics.result, float(self.row['correlation']))

    def test_zscore_statistics(self):
        self.assertEqual(self.statistics.zscore(self.column1), self.column_zscore)
        self.assertEqual(self.statistics.result, self.column_zscore)

    def test_pvalue_statistics(self):
        self.assertEqual(self.statistics.p_value(self.column1), self.column_zscore)
        self.assertEqual(self.statistics.result, self.column_zscore)

    def test_proportion_statistics(self):
        self.assertEqual(self.statistics.proportion(self.column1), self.column_proportion)
        self.assertEqual(self.statistics.result, self.column_proportion)

    def test_confidence_interval(self):
        for row in self.test_answer:
            pprint(row['ci_top'])
            pprint(row['ci_bottom'])
        self.assertEqual(self.statistics.confidence_interval_top(self.column1), float(self.row['ci_top']))
        self.assertEqual(self.statistics.confidence_interval_bottom(self.column1), float(self.row['ci_bottom']))

    def test_sample_mean_statistics(self):
        for row in self.sample_answer:
            pprint(row["mean"])
        self.assertEqual(self.statistics.sample_mean(self.column3), float(self.row['mean']))
        self.assertEqual(self.statistics.result, float(self.row['mean']))

    def test_sample_standard_deviation_statistics(self):
        for row in self.sample_answer:
            pprint(row["stddev"])
        self.assertEqual(self.statistics.sample_stddev(self.column3), float(self.row['stddev']))
        self.assertEqual(self.statistics.result, float(self.row['stddev']))

    def test_sample_variance_statistics(self):
        for row in self.sample_answer:
            pprint(row['variance'])
        self.assertEqual(self.statistics.sample_variance(self.column3), float(self.row['variance']))
        self.assertEqual(self.statistics.result, float(self.row['variance']))


if __name__ == '__main__':
    unittest.main()
