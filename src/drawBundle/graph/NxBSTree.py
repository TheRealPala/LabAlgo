import networkx as nx
from mainBundle.bst.BSNode import BSNode
from mainBundle.bst.BSTree import BSTree


class NxBSTree(BSTree):
    def __init__(self):
        super().__init__()
        self.__nxTree = nx.Graph()

    def getTree(self):
        return self.__nxTree

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
        node.father = father
        if father is None:
            self._root = node
            self.__nxTree.add_node(node.getKey(), label=str(node.getKey()))
        elif node.getKey() <= father.getKey():
            father.setLeft(node)
            self.__nxTree.add_node(node.getKey(), label=str(node.getKey()))
            self.__nxTree.add_edge(father.getKey(), node.getKey())
        else:
            father.setRight(node)
            self.__nxTree.add_node(node.getKey(), label=str(node.getKey()))
            self.__nxTree.add_edge(father.getKey(), node.getKey())

    def createNxBSTFromBST(self, tree):
        if tree is not None:
            self.createNxBSTFromBST(tree.getLeft())
            self.createNxBSTFromBST(tree.getRight())
            if tree.getLeft() is not None:
                self.__nxTree.add_edge(tree.getKey(), tree.getLeft().getKey())
            if tree.getRight() is not None:
                self.__nxTree.add_edge(tree.getKey(), tree.getRight().getKey())


