from src.mainBundle.booleanBst import BBSNode
from src.mainBundle.bst.BSTree import BSTree


class BBSTree(BSTree):
    def __init__(self):
        super().__init__()

    def insert(self, key):
        node = BBSNode.BBSNode(key)
        father = None
        current = self._root
        while current is not None:
            father = current
            if node.__eq__(current):
                current.setBooleanFlag(not current.getBooleanFlag())
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
        elif node.getKey() <= father.getKey():
            father.setLeft(node)
        else:
            father.setRight(node)

    def find(self, key):
        current = self._root
        while current is not None and current.getKey() != key:
            currentKey = current.getKey()
            if key < currentKey:
                current = current.getLeft()
            elif key > currentKey:
                current = current.getRight()
            else:
                if current.getBooleanFlag():
                    current = current.getLeft()
                else:
                    current = current.getRight()
        return current

    def inorderTreeWalk(self, node):
        if node is not None:
            self.inorderTreeWalk(node.getLeft())
            print(node)
            self.inorderTreeWalk(node.getRight())