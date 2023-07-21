import random
import sys


class TileWithoutHeuristic:
    coordinate = None
    cost = None
    pathToTile = None

    def __init__(self, point, pathToTile, cost):
        self.coordinate = point
        self.pathToTile = list()
        self.pathToTile.append((point))
        self.pathToTile.extend(pathToTile)
        self.cost = cost

    def __str__(self):
        return "{Coordinate: " + str(self.coordinate) + " path to tile: " + str(self.pathToTile) + " cost is " + str(
            self.cost) + "}"


class TileWithHeuristic:
    coordinate = None
    cost = None
    pathToTile = None
    heuristic = None
    heuristicFunction = None

    def __init__(self, point, pathToTile, cost, admissibleFlag):
        self.coordinate = point
        self.pathToTile = list()
        self.pathToTile.append((point))
        self.pathToTile.extend(pathToTile)
        self.cost = cost
        self.heuristicFunction = 0
        if admissibleFlag:
            self.heuristic = 1
        else:
            self.heuristic = random.randint(sys.maxsize, sys.maxsize + 10000)

    def __str__(self):
        return "{Coordinate: " + str(self.coordinate) + " path to tile: " + str(self.pathToTile) + " cost is " + str(
            self.cost) + " heuristic is " + str(self.heuristic) + "}"
