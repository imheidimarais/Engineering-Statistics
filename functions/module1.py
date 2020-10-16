# This file should contain a copy of each function defined in the tutorial file
# which can be imported and used in a students own work.


def get_confidence_interval(data, confidence=0.95, sigma_known=False):
    """Determines the confidence interval for a given set of data, 
    assuming the population standard deviation is not known."""
    
    n = len(data) # determines the sample size
    m = numpy.mean(data) # obtains mean of the sample
    if sigma_known == False:
        se = sstats.sem(data) # obtains standard error of the sample
    elif sigma_known == True:
        se = numpy.std(data)
    else:
      raise ValueError(
                "Invalid value given for parameter 'sigma_known'"
            )
    c_interval = sstats.t.interval(confidence, n-1, m, se) # determines the confidence interval
    return c_interval # which is in the form (lower bound, upper bound)