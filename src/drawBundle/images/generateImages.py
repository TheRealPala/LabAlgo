from src.drawBundle.graph import AbrImagesHandler as aih
from src.drawBundle.chart import ChartHandler as ch
import numpy as np
abrImageHandler = aih.AbrImagesHandler()
def saveBalacedTree():
    g = aih.createBalancedGraph()
    abrImageHandler.saveGraphImg(g, "balancedTree.png")

def saveNxBalancedTree():
    tree = aih.createBalancedTree()
    abrImageHandler.saveGraphImg(tree, "balancedTreeNx.png")

def saveUnbalancedTree():
    values = []
    for i in range(1, 5):
        values.append(i)
    g = aih.createNxCustomGraphFromValues(values)
    abrImageHandler.saveGraphImg(g, "unbalancedTree.png")

def createImages():
    saveBalacedTree()
    saveNxBalancedTree()
    saveUnbalancedTree()



