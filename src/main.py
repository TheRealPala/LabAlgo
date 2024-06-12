# This is a sample Python script.
import math
import sys

from src.drawBundle.chart.ChartHandler import ChartHandler
from src.testBundle.test import Tester
from src.drawBundle.images import generateImages
sys.setrecursionlimit(int(math.pow(10, 8)))

if __name__ == '__main__':

    valuesToInsert = []
    results = []
    abr = BSTree.BSTree()
    for i in range(2, 5):
        valuesToInsert.append(int(math.pow(2, i)))
    for i in ( bar := tqdm(valuesToInsert)):
        bar.set_description(f"Testing with {i} values")
        t = Test.Test("settings.json", i, abr)
        results.append(t.testActions())
        time.sleep(0.3)
    print(results)
    generateImages.createImages()
    # t = Tester.runAllTests()
    # insertResult = Tester.elaborateInsertResults(t)
    # ch = ChartHandler()
    # ch.setAction("insert")
    # ch.genereateChartFromResults(insertResult)
    # findResult = Tester.elaborateFindResults(t)
    # ch.setAction("find")
    # ch.genereateChartFromResults(findResult)

