import matplotlib.pyplot as plt
import os
import glob
import shutil

import numpy as np
from matplotlib.ticker import ScalarFormatter
from scipy.signal import medfilt


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
        self.multiChart = None

    def setAction(self, action):
        self.action = action

    def saveChart(self, datasetX, datasetY, xLabel, yLabel, filename, title):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(datasetX, datasetY)
        ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        ax.set(xlabel=xLabel, ylabel=yLabel)
        if title:
            ax.set_title(title)
        plt.savefig(os.path.join(self.chartPath, filename))
        plt.close()

    def createSubDirectory(self, directoryName):
        path = os.path.join(self.chartPath, directoryName)
        if (not os.path.exists(path)):
            os.mkdir(path)

    def movingAverageFilter(self, data, windowSize):
        return np.convolve(data, np.ones(windowSize) / windowSize, mode='valid')

    def emptyDirectory(self):
        path = os.path.join(self.chartPath, self.action)
        if os.path.exists(path) and os.listdir(path):
            for f in glob.glob(path + "/*"):
                if os.path.isdir(f):
                    shutil.rmtree(f)
                else:
                    os.remove(f)

    def genereateChartFromResults(self, results):
        print(results)
        self.emptyDirectory()
        if (self.action == None):
            return
        else:
            self.createSubDirectory(self.action)
            labels = []
            for type in results:
                self.createSubDirectory(self.action + "/" + type)
                for percentage in results[type]:
                    label = results[type][percentage]['label']
                    if label not in labels:
                        labels.append(label)
                    xValues = []
                    yValues = []
                    for res in results[type][percentage]['values']:
                        filteredNumValues = self.movingAverageFilter(res['time'], 3)
                        xValues.append(res['numOfValues'])
                        yValues.append(res['time'])
                    self.saveChart(xValues, yValues, "elementi", "tempo [s]",
                                   self.action + "/" + type + "/" + label + "CaseChart", title = self.action + ":" + label)
            print(labels)
            xValues = {}
            yValues = {}
            print(self.action)
            for label in labels:
                print(label)
                xValues[label] = []
                yValues[label] = {}
                for type in results:
                    print(type)
                    yValues[label][type] = []
                    for percentage in results[type]:
                        for res in results[type][percentage]['values']:
                            if(label == results[type][percentage]['label']):
                                print(res)
                                if (res['numOfValues'] not in xValues[label]):
                                    xValues[label].append(res['numOfValues'])
                                yValues[label][type].append(res['time'])
            #generateMixedChart
            self.createSubDirectory(self.action + "/mixed")
            for labels in xValues:
                fig, ax = plt.subplots(figsize=(8, 6))
                for type in yValues[labels]:
                    ax.plot(xValues[labels], yValues[labels][type], label=type)
                ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
                ax.set(xlabel="elementi", ylabel="tempo [s]")
                ax.set_title(self.action + ":" + labels)
                ax.legend()
                plt.savefig(os.path.join(self.chartPath, self.action + "/mixed/" + labels + "MixedChart"))
