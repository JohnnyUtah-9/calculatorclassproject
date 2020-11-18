from Calculator.Calculator import Calculator
from Stats.Median import median
from Stats.Mode import mode
from Stats.sdP import stddev
from Stats.VarP import variance
from Stats.MeanPopu import populationmean
from Stats.Proportional import proportion
from Stats.zScore import zscore
from Stats.CorrCoeff import correlation
from Stats.questionProblem import variance_of_population_proportion
from Stats.ConfidenceInt2 import confidence_interval_top
from Stats.ConfidenceInt import confidence_interval_bottom
from Stats.MeanS import samplemean
from Stats.sdS import samplestddev
from Stats.VarS import samplevariance
from Stats.pValue import pvalue
from CsvReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def population_mean(self, data):
        self.result = populationmean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def stddev(self, data):
        self.result = stddev(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def proportion(self, data):
        self.result = proportion(data)
        return self.result

    def zscore(self, data):
        self.result = zscore(data)
        return self.result

    def correlation_coefficient(self, data, data1):
        self.result = correlation(data, data1)
        return self.result

    def population_proportion_variance(self, data):
        self.result = variance_of_population_proportion(data)
        return self.result

    def confidence_interval_top(self, data):
        self.result = confidence_interval_top(data)
        return self.result

    def confidence_interval_bottom(self, data):
        self.result = confidence_interval_bottom(data)
        return self.result

    def sample_mean(self, data):
        self.result = samplemean(data)
        return self.result

    def p_value(self, data):
        self.result = pvalue(data)
        return self.result

    def sample_stddev(self, data):
        self.result = samplestddev(data)
        return self.result

    def sample_variance(self, data):
        self.result = samplevariance(data)
        return self.result

    pass