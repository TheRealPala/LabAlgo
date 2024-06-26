from mainBundle.booleanBst import BBSNode
from mainBundle.bst.BSTree import BSTree


class BBSTree(BSTree):
    def __init__(self):
        super().__init__()

    def insert(self, key):
        node = BBSNode.BBSNode(key)
        father = None
        current = self._root
        isNextToDuplicate = False
        while current is not None:
            isNextToDuplicate = False
            father = current
            if node.__eq__(current):
                current.setBooleanFlag(not current.getBooleanFlag())
                isNextToDuplicate = True
                if not current.getBooleanFlag():
                    current = current.getLeft()
                else:
                    current = current.getRight()
            elif node.getKey() < current.getKey():
                current = current.getLeft()
            else:
                current = current.getRight()
        node.father = father
        if father is None:
            self._root = node
        else:
            if not isNextToDuplicate:
                if node.getKey() < father.getKey():
                    father.setLeft(node)
                else:
                    father.setRight(node)
            else:
                if not father.getBooleanFlag():
                    father.setLeft(node)
                else:
                    father.setRight(node)


    def __multipleFind(self, key, node, nodeFoundList):
        if node is not None:
            if node.getKey() == key:
                nodeFoundList.append(node)
                # ci potrebbero essere altri nodi nel sottoalbero sinistro e nel sottoalbero destro
                leftNode = node.getLeft()
                if leftNode is not None:
                    self.__multipleFind(key, leftNode, nodeFoundList)
                rightNode = node.getRight()
                if rightNode is not None:
                    self.__multipleFind(key, rightNode, nodeFoundList)
            elif key < node.getKey():
                self.__multipleFind(key, node.getLeft(), nodeFoundList)
            else:
                self.__multipleFind(key, node.getRight(), nodeFoundList)
        else:
            return
    def find(self, key):
        list = []
        self.__multipleFind(key, self._root, list)
        return list
    def inorderTreeWalk(self, node):
        if node is not None:
            self.inorderTreeWalk(node.getLeft())
            print(node)
            self.inorderTreeWalk(node.getRight())
