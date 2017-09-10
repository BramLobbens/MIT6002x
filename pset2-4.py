# MIT 6.00.2x Pset2-4

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    test_chamber = RectangularRoom(width, height)
    robots = {}

    for i in range(num_robots):
        robots[i] = robot_type(test_chamber, speed)

    def run_test():
        steps = 0
        while True:
            steps += 1
            for i in range(num_robots):
                robots[i].updatePositionAndClean()
                if test_chamber.getNumCleanedTiles() >= test_chamber.getNumTiles() * min_coverage:
                    return steps
            
    results = []
    for i in range(num_trials):
        results.append(run_test())
        test_chamber.cleaned = []

    return sum(results) / num_trials
