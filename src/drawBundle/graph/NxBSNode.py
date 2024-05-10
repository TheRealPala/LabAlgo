from src.mainBundle.bst import BSNode


class NxBSNode(BSNode):
    def __init__(self, key):
        super().__init__(key)
        self.__nxNode = None
        self.__duplicatedValue = 0

    def getNxNode(self):
        return self.__nxNode

    def setNxNode(self, nxNode):
        self.__nxNode = nxNode
