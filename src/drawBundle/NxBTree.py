import networkx as nx
import src.drawBundle.BNode as BNode


class NxBTree:
    def __init__(self):
        self.nxTree = nx.DiGraph()
        self.root = None

    def getTree(self):
        return self.nxTree

    def insert(self, key):
        node = BNode.BNode(key)
        father = None
        current = self.root
        while current is not None:
            father = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right
        node.father = father
        if father is None:
            self.root = node
            self.nxTree.add_node(node.key, label=str(node.key))
        elif node.key < father.key:
            father.left = node
            self.nxTree.add_node(node.key, label=str(node.key))
            self.nxTree.add_edge(father.key, node.key)
        else:
            father.right = node
            self.nxTree.add_node(node.key, label=str(node.key))
            self.nxTree.add_edge(father.key, node.key)
