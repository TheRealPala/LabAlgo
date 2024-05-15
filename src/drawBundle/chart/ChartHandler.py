import matplotlib.pyplot as plt
import os
import glob
import shutil
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
        plt.cla()
        plt.clf()
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
                if os.path.isdir(f):
                    shutil.rmtree(f)
                else:
                    os.remove(f)
    def genereateChartFromResults(self, results):
       self.emptyDirectory()
       for type in results:
           self.createSubDirectory(type)
           print(type)
           for percentage in results[type]:
               label = results[type][percentage]['label']
               print(label)
               xValues = []
               yValues = []
               for res in results[type][percentage]['values']:
                   xValues.append(res['numOfValues'])
                   yValues.append(res['time'])
               print(xValues)
               print(yValues)
               self.saveChart(xValues, yValues, "elementi", "tempo", type + "/" + label + "CaseChart")
