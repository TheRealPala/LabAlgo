# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.drawBundle.graph import AbrImagesHandler as aih
from src.drawBundle.chart import chartHandler as ch
import numpy as np
# Press the green button in the gutter to run the script.
def abrImage():
    abrImageHandler = aih.AbrImagesHandler()
    g = aih.createExampleGraph()
    aih.drawGraph(g)
    abrImageHandler.saveGraphImg(g, "exampleBtree.png")
def printChart():
    ch.printChart()
if __name__ == '__main__':
    #abrImage();
    datasetX = np.random.randint(0, 100, size=100)
    datasetY = np.random.randint(0, 100, size=100)
    datasetX.sort();
    datasetY.sort();
    chHandler = ch.ChartHandler()
    chHandler.saveChart(datasetX, datasetY, "X", "Y", "chart.png")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
