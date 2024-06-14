from src.mainBundle.bst.BSNode import BSNode


class BSTree:
    def __init__(self):
        self._root = None

    def getRoot(self):
        return self._root

    def insert(self, key):
        node = BSNode(key)
        father = None
        current = self._root
        while current is not None:
            father = current
            if node.getKey() <= current.getKey():
                current = current.getLeft()
            else:
                current = current.getRight()
        node.setFather(father)
        if father is None:
            self._root = node
        elif node.getKey() <= father.getKey():
            father.setLeft(node)
        else:
            father.setRight(node)

    def __multipleFind(self, key, node, nodeFoundList):
        if node is not None:
            if node.getKey() == key:
                nodeFoundList.append(node)
                # ci potrebbero essere altri nodi nel sottoalbero sinistro
                leftNode = node.getLeft()
                if leftNode is not None:
                    self.__multipleFind(key, leftNode, nodeFoundList)
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
