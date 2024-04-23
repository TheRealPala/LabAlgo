from src.mainBundle.bst.BSNode import BSNode


class BBSNode(BSNode):
    def __init__(self, key):
        super().__init__(key)
        self.__booleanFlag = False  # true if last duplicated node went right, false if went false

    def getBooleanFlag(self):
        return self.__booleanFlag

    def setBooleanFlag(self, booleanFlag):
        self.__booleanFlag = booleanFlag
