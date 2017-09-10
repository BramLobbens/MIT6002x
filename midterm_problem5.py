# MIT 6.00.2x Midterm Problem 5

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """

    current_max = 0
    max_ending = 0

    for i in range(len(L)):
        max_ending += L[i]
        if max_ending < 0:
            max_ending = 0

        if current_max < max_ending:
            current_max = max_ending

    return current_max