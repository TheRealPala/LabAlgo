class BSNode:
    def __init__(self, key):
        self._key = key
        self._left = None
        self._right = None
        self._father = None

    def getKey(self):
        return self._key

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def getFather(self):
        return self._father

    def setKey(self, key):
        self._key = key

    def setLeft(self, left):
        self._left = left

    def setRight(self, right):
        self._right = right

    def setFather(self, father):
        self._father = father

    def __str__(self) -> str:
        ret = 'Node: ' + str(self._key)
        return ret

    def __eq__(self, _o: object) -> bool:
        return self._key == _o._key
