# This is a sample Python script.
import math
import time
from src.drawBundle.graph import AbrImagesHandler as aih
from src.drawBundle.chart import ChartHandler as ch
from src.mainBundle.booleanBst.BBSTree import BBSTree
from src.mainBundle.linkedListBundle.LLBSTree import LLBSTree
from src.mainBundle.bst import BSTree
from src.drawBundle.chart.ChartHandler import ChartHandler
from src.testBundle.test import Test, Tester
import sys
import numpy as np
from tqdm import tqdm
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
    values = [3, 5, 2, 3, 4, 6, 7, 3, 2, 3];
    for value in values:
        bst.insert(value)
    bst.inorderTreeWalk(bst.getRoot())
    valuesFound = bst.multipleFindFront(3)
    print(f'Number of values founded:{len(valuesFound)}')
    print(f'List:{valuesFound}')

def tryBbst():
    bbst = BBSTree()
    values = [9, 5, 3, 10, 3, 4, 3, 3]
    for value in values:
        bbst.insert(value)
    bbst.inorderTreeWalk(bbst.getRoot())
    valuesFound = bbst.multipleFindFront(3)
    print(f'Number of values founded:{len(valuesFound)}')
    print(f'List:{valuesFound}')
def tryLLBst():
    llbst = LLBSTree()
    values = [9, 5, 3, 10, 3, 4, 3, 3, 2, 3]
    for value in values:
        llbst.insert(value)
    llbst.inorderTreeWalk(llbst.getRoot())
    head = llbst.find(3)
    aih.drawGraph(llbst)
    print(f'Number of values founded: {head.getCount()}')
    head.showAllNextValues()

if __name__ == '__main__':

    # valuesToInsert = []
    # results = []
    # abr = BSTree.BSTree()
    # for i in range(2, 5):
    #     valuesToInsert.append(int(math.pow(2, i)))
    # for i in ( bar := tqdm(valuesToInsert)):
    #     bar.set_description(f"Testing with {i} values")
    #     t = Test.Test("settings.json", i, abr)
    #     results.append(t.testActions())
    #     time.sleep(0.3)
    # print(results)
    t = Tester.runAllTests()
    t = Tester.elaborateInsertResults(t)
    ch = ChartHandler()
    ch.genereateChartFromResults(t)

