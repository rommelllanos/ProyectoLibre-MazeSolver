class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def returnQueueAsString(self):
        queue_str = ""
        for eachItem in self.items:
            queue_str += str(eachItem) + " "
        return queue_str

    def isQueueContainsElement(self, element):
        if element in self.items:
            return True
        return False
