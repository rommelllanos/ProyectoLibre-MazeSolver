from PriorityQueueImpl import PriorityQueueImpl
from queue import PriorityQueue
from PlotMaze import plot_maze_with_path

from Tile import TileWithoutHeuristic

class MazeSolverWithUniformCost:

    startingPoint = None
    goalPoint = None
    frontier = None
    explored = None
    actionCost = None
    heuristicFlag = False

    def __init__(self, maze, startPoint, endPoint):
        """
                Before start the process algorithm, take these inputs from user:
                :param maze:  which representation of maze graph
                :param startPoint:  which is tuple to represent starting tile coordination
                :param endPoint: which is tuple to represent goal tile coordination
                """
        self.maze = maze
        self.startingPoint = startPoint
        self.goalPoint = endPoint


    def __getElementFromPairs(self, point):
        """
        gets tile extra cost from point(x, y)
        :param point: represents coordinate value (x and y)
        :return: tile's extra cost
        """
        return self.maze[point[0]][point[1]]

    def __isTileGoalState(self, point):
        """
        is tile at point "point" is the goal point?
        :param point: represents coordinate value that will be checked
                      whether it is goal point or not
        :return: true if point is goal point
                 false if not
        """
        return point == self.goalPoint

    def __isTileInExplored(self, tile):
        """
        is tile is in the explored set?
        :param tile: is the tile that will be checked
                     whether it is in explored state or not
        :return: true if tile is in explored state
                 false if not
        """
        for eachTile in self.explored:
            if eachTile.coordinate == tile.coordinate:
                return True
        return False

    def __isTileWall(self, point):
        """
        is tile at point "point" wall?
        :param point: is the tile's point that will be checked
                      whether it is wall state or not
        :return: true if it is wall
                 false  if not
        """
        return self.__getElementFromPairs(point) == "-"

    def __isTileInFrontier(self, tile):
        """
        is tile in the stack?
        :param tile: is the tile that will be checked
                     whether it is in stack or not
        :return: true if it is in stack
                 false if not
        """
        return self.frontier.isQueueContainsElement(tile)

    def __findAdjacentsToThisPoint(self, point):
        """
        Find the adjacent points of that point
        Here is the priority that I have defined:
                |(4)
        (3)--  point -- (1)
                |(2)

        that's means, first if it exists, add right point to the list
                      second if it exists, add below point to the list
                      third if it exists, add left point to the list
                      fourth if it exists, add upper point to the list
        :param point: is the point that will be found its adjacent pairs
        :return: adjacent pairs as a list
        """
        x = point[0]
        y = point[1]
        adjacentPointPairs = list()
        for eachRow in range(len(self.maze)):
            for eachColumn in range(len(self.maze[eachRow])):
                if eachRow == x and eachColumn == y:
                    if y + 1 < len(self.maze[eachRow]):
                        adjacentPointPairs.append(((x, y + 1)))
                    if x + 1 < len(self.maze):
                        adjacentPointPairs.append(((x + 1, y)))
                    if x - 1 >= 0:
                        adjacentPointPairs.append(((x - 1, y)))
                    if y - 1 >= 0:
                        adjacentPointPairs.append(((x, y - 1)))
                    return adjacentPointPairs

    def uniformCost(self):
        """
        UCS algorithm with extra move point cost
        Create PriorityQueue with heuristicFlag(if flag is true then priority by heuristic function, otherwise
                                                priority by cost)
        Create explored set
        If the starting point is also goal point print it and return
        Else
            Create new tile with starting point, its cost and path that brings us to that path
            Loop until frontier is empty
                Dequeue tile T1 from frontier
                If T1 is goal tile, print path & cost and return
                Else
                    add T1 to explored
                    find adjacent point to T1
                    for each Point do:
                        if point is not wall:
                            create new tile(T2) with that point, its cost and path(which is T1.path)
                                            that brings us to that path
                            If T2 is not in explored:
                                assign T2.cost = its.cost + T1.cost + 1(extra move cost)
                                and add T2 to the frontier

        :return:
        """
        self.frontier = PriorityQueueImpl(self.heuristicFlag)
        self.explored = set()

        if self.__isTileGoalState(self.startingPoint):
            print("Path is found: " + str(self.startingPoint) + " with 0 cost")
            return

        self.frontier.enqueue(TileWithoutHeuristic(self.startingPoint, [], 0))


        while self.frontier.isEmpty() != True:
            tile = self.frontier.dequeue()
            tileCoordinate = tile.coordinate
            tileCost = tile.cost

            if self.__isTileGoalState(tileCoordinate):
                self.__printThePath(tile)
                return

            self.explored.add(tile)

            adjacentList = self.__findAdjacentsToThisPoint(tileCoordinate)
            for eachPoint in adjacentList:
                if not self.__isTileWall(eachPoint):
                    eachTile = TileWithoutHeuristic(eachPoint, tile.pathToTile, self.__getElementFromPairs(eachPoint))
                    if not self.__isTileInExplored(eachTile):
                        eachTile.cost = self.__getElementFromPairs(eachPoint) + tileCost + 1
                        self.frontier.enqueue(eachTile)

    def __printThePath(self, tile):
        """
        Print the path from initial tile to goal tile
        :param tile: is the goal tile which includes the path
        :return:
        """
        print()
        print("Path is found. Initial tile: " + str(self.startingPoint) + ", Goal tile: " + str(self.goalPoint))
        print("Here is the path cost: " + str(tile.cost) + " and path is:")
        print(tile.pathToTile[::-1])
        plot_maze_with_path(self.maze, tile.pathToTile[::-1])
        print()
