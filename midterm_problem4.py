# MIT 6.00.2x Midterm Problem 4

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """

    if not L:
        return 'no solution'

    mults = [0] * (len(L))  # create mults list of equal length to L

    if len(L) == 1:
        if s % L[0] == 0:
            return s // L[0]
        return 'no solution'

    remainder = s
    for idx, e in enumerate(L):
        m = remainder // e
        if m >= 1:
            mults[idx] = m
            remainder -= m * e
    
    # solve the equation: sum of the elements of both list multiplied
    sum_result = sum([e * m for idxe, e in enumerate(L)
                      for idxm, m in enumerate(mults) if idxe == idxm])

    if sum_result == s:
        return sum(mults)

    return 'no solution'