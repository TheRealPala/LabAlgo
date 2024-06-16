# This is a sample Python script.
import math
import sys

from src.drawBundle.chart.ChartHandler import ChartHandler
from src.testBundle.test import Tester
from src.drawBundle.images import generateImages
sys.setrecursionlimit(int(math.pow(10, 8)))

if __name__ == '__main__':
    generateImages.createImages()
    t = Tester.runAllTests()
    insertResult = Tester.elaborateInsertResults(t)
    ch = ChartHandler()
    ch.setAction("insert")
    ch.genereateChartFromResults(insertResult)
    findResult = Tester.elaborateFindResults(t)
    ch.setAction("find")
    ch.genereateChartFromResults(findResult)

