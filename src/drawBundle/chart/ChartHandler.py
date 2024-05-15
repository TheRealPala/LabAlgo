import matplotlib.pyplot as plt
import os
import glob

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
    def createSubDirectory(self, directoryName):
        path = os.path.join(self.chartPath, directoryName)
        if (not os.path.exists(path)):
            os.mkdir(path)

    def emptyDirectory(self):
        if (os.listdir(self.chartPath)):
            for f in glob.glob(os.path.join(self.chartPath, "*")):
                if (os.path.isdir(f)):
                    os.rmdir(f)
                else:
                    os.remove(f)
    def genereateChartFromResults(self, results):
       self.emptyDirectory()