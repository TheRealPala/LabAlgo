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
        elif node.getKey() < father.getKey():
            father.setLeft(node)
        else:
            father.setRight(node)

    def find(self, key):
        current = self._root
        while current is not None and current.getKey() != key:
            if key <= current.getKey():
                current = current.getLeft()
            else:
                current = current.getRight()
        return current

    def inorderTreeWalk(self, node):
        if node is not None:
            self.inorderTreeWalk(node.getLeft())
            print(node)
            self.inorderTreeWalk(node.getRight())
