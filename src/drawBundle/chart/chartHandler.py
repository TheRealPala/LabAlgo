import matplotlib.pyplot as plt
import numpy as np
import os


def drawChart(datasetX, datasetY, xLabel, yLabel):
    plt.plot(datasetX, datasetY)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()


class ChartHandler:
    def __init__(self):
        self.rootProject = os.path.dirname(os.path.abspath(__file__)) + "/../../../"
        self.chartPath = os.path.join(self.rootProject, "dist/chart/")

    def saveChart(self, datasetX, datasetY, xLabel, yLabel, filename):
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.plot(datasetX, datasetY)
        plt.savefig(os.path.join(self.chartPath, filename))
