from mainBundle.bst.BSNode import BSNode


class LLBSNode(BSNode):
    def __init__(self, key):
        super().__init__(key)
        self.__next = None
        self.__count = 1

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next

    def getCount(self):
        return self.__count

    def setCount(self, count):
        self.__count = count

    def showAllNextValues(self):
        current = self
        while current is not None:
            print(current)
            current = current.getNext()