# MIT 6.00.2x Pset1-2

def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_copy = cows.copy()
    cows_list = sorted(cows, key=cows.get)
    pset = get_partitions(cows_list)

    bestcombo = cows_list
    shortest = len(cows_list)
        
    for combos in pset:
        journeys = 0 # number of journeys made
        weights = [] # list of weights per journey
        
        for cowset in combos:
            journeys += 1
            totalweight = 0
            for cow in cowset:
                totalweight += cows_copy[cow]
            weights.append(totalweight) # append weight of each journey
        
        for weight in weights:
            if weight > limit:
                break
        else: # no break
            if totalweight <= limit and journeys <= shortest:
                bestcombo = combos
                shortest = journeys
        
    return bestcombo