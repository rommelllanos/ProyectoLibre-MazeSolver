class PriorityQueueImpl:
    heuristicFlag = None

    def __init__(self, heuristicFlag):
        self.items = []
        self.heuristicFlag = heuristicFlag

    def isEmpty(self):
        return self.items == []

    def sortComparatorByCost(self, item):
        return item.cost

    def sortComparatorByHeuristic(self, item):
        return item.heuristicFunction

    def enqueue(self, item):
        self.items.append(item)
        if self.heuristicFlag:
            self.items.sort(key=self.sortComparatorByHeuristic)
        else:
            self.items.sort(key=self.sortComparatorByCost)

    def dequeue(self):
        return self.items.pop(0)

    def returnQueueAsString(self):
        queue_str = ""
        for eachItem in self.items:
            queue_str += str(eachItem) + " "
        return queue_str

    def isQueueContainsElement(self, element):
        for eachElement in self.items:
            if eachElement[0] == element:
                return True
        return False


