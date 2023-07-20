class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def returnStackAsString(self):
        stack_str = ""
        for eachItem in self.items:
            stack_str += str(eachItem) + " "

        return stack_str



    def isStackContainsElement(self, tile):
        if tile in self.items:
            return True
        return False

