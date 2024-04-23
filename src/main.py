# This is a sample Python script.
import math


from src.drawBundle.graph import AbrImagesHandler as aih
from src.drawBundle.chart import ChartHandler as ch
from src.performanceBundle.timer import Timer as pt
from src.mainBundle.abr import BSTree
import sys
import numpy as np

sys.setrecursionlimit(int(math.pow(10, 8)))

def abrImage():
    abrImageHandler = aih.AbrImagesHandler()
    g = aih.createExampleGraph()
    aih.drawGraph(g)
    abrImageHandler.saveGraphImg(g, "exampleBtree.png")


def printChart():
    ch.printChart()


def saveChart():
    datasetX = np.random.randint(0, 100, size=100)
    datasetY = np.random.randint(0, 100, size=100)
    datasetX.sort()
    datasetY.sort()
    chHandler = ch.ChartHandler()
    chHandler.saveChart(datasetX, datasetY, "X", "Y", "chart.png")

def tryBst():
    bst = BSTree.BSTree()
    values = [9, 5, 15, 3, 7, 1, 4, 20, 25]
    for value in values:
        bst.insert(value)
    bst.inorderTreeWalk(bst.getRoot())
    aih.drawGraph(bst)

if __name__ == '__main__':
    #print(pt.testFunction(saveChart))
    tryBst()
    # abrImage();

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
