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
        self.action = None
        self.rootProject = os.path.dirname(os.path.abspath(__file__)) + "/../../../"
        self.chartPath = os.path.join(self.rootProject, "dist/chart/")
    def setAction(self, action):
        self.action = action
    def saveChart(self, datasetX, datasetY, xLabel, yLabel, filename):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(datasetX, datasetY)
        ax.set(xlabel=xLabel, ylabel=yLabel)
        plt.savefig(os.path.join(self.chartPath, filename))
        plt.close()
    def createSubDirectory(self, directoryName):
        path = os.path.join(self.chartPath, directoryName)
        if (not os.path.exists(path)):
            os.mkdir(path)

    def emptyDirectory(self):
        path = os.path.join(self.chartPath, self.action)
        if os.path.exists(path) and os.listdir(path):
            for f in glob.glob(path+ "/*"):
                if os.path.isdir(f):
                    shutil.rmtree(f)
                else:
                    os.remove(f)
    def genereateChartFromResults(self, results):
       self.emptyDirectory()
       if (self.action == None):
              return
       else:
           self.createSubDirectory(self.action)
           for type in results:
               self.createSubDirectory(self.action+"/"+type)
               for percentage in results[type]:
                   label = results[type][percentage]['label']
                   xValues = []
                   yValues = []
                   for res in results[type][percentage]['values']:
                       xValues.append(res['numOfValues'])
                       yValues.append(res['time'])
                   self.saveChart(xValues, yValues, "elementi", "tempo [s]", self.action + "/" + type + "/" + label + "CaseChart")
