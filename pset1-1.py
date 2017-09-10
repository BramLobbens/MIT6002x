# MIT 6.00.2x Pset1-1

def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_list = sorted(cows, key=cows.get, reverse=True)
    cows_copy = cows.copy()
    result = []
    taken = []
    def greedy_helper(list_of_cows, limit=10):
        '''Return list of cows taken each journey'''
        current_journey = []
        total_weight = 0

        for cow in list_of_cows:
            if (total_weight + cows_copy[cow] <= limit) \
            and cow not in taken:
                current_journey.append(cow)
                total_weight += cows_copy[cow]
                taken.append(cow)
        return [current_journey]

    result = [greedy_helper(cows_list, limit) for x in cows_list]

    return result