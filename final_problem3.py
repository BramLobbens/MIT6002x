# MIT 6.00.2x Final Exam Problem 3

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    equal_taken = 0

    for trial in range(numTrials):
        balls = [1, 1, 1, 1, 2, 2, 2, 2]
        hand = []
        for game in range(3):
            taken = random.choice(balls)
            hand += [taken]
            balls.remove(taken)
        if hand.count(hand[0]) == len(hand):
            equal_taken += 1

    return equal_taken / numTrials