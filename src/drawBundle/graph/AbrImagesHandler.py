import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import numpy as np
import os
from src.drawBundle.graph.NxBSTree import NxBSTree


def createRandomGraph(n=7):
    bTree = NxBSTree()
    numbers = [i for i in range(n)]
    np.random.shuffle(numbers)
    for number in numbers:
        bTree.insert(number)
    return bTree.getTree()


def drawNxGraph(g):
    pos = graphviz_layout(g, prog="dot")
    nx.draw(g, pos, with_labels=True, arrows=True)
    plt.show()


def getNxBStreeFromBSTree(bst):
    bTree = NxBSTree()
    bTree.createNxBSTFromBST(bst.getRoot())
    return bTree.getTree()

def drawGraph(g):
    nxGraph = getNxBStreeFromBSTree(g)
    drawNxGraph(nxGraph)
def drawBGraph(g):
    nxGraph = getNxBBStreeFromBSTree(g)
    drawNxGraph(nxGraph)

def createExampleGraph():
    numbers = [4, 2, 6, 1, 3, 5, 7]
    bTree = NxBSTree()
    for number in numbers:
        bTree.insert(number)
    return bTree.getTree()


def createNxCustomGraphFromValues(values):
    bTree = NxBSTree()
    for value in values:
        bTree.insert(value)
    return bTree.getTree()


class AbrImagesHandler:
    def __init__(self):
        self.rootProject = os.path.dirname(os.path.abspath(__file__)) + "/../../../"
        self.imgPath = os.path.join(self.rootProject, "dist/img/")

    def saveGraphImg(self, g, filename):
        pos = graphviz_layout(g, prog="dot")
        nx.draw(g, pos, with_labels=True, arrows=True)
        plt.savefig(os.path.join(self.imgPath, filename))
