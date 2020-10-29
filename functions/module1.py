# This file should contain a copy of each function defined in the tutorial file
# which can be imported and used in a students own work.


import numpy
from scipy import stats
import pandas


def get_confidence_interval(data, confidence=0.95):
    """ Determines the confidence interval for a given set of data, 
        assuming the population standard deviation is not known.

    Args:  # 'arguments', or inputs to the function
        data (single-column or list): The data
        confidence (float): The confidence level on which to produce the interval.

    Returns:
        c_interval (tuple): The confidence interval on the given data (lower, upper).
    """

    n = len(data)  # determines the sample size
    m = numpy.mean(data)  # obtains mean of the sample

    se = stats.sem(data)  # obtains standard error of the sample

    c_interval = stats.t.interval(confidence, n-1, m, se)  # determines the confidence interval
    return c_interval  # which is of the form (lower bound, upper bound)