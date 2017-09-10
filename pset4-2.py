# MIT 6.00.2x Pset4-2

import numpy as np

def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    
    estimateError = sum([(e-estimated[idx])**2 for idx,e in enumerate(y)])
    meanOfEstimated = estimateError/len(y)
    return 1 - (meanOfEstimated/np.var(y))