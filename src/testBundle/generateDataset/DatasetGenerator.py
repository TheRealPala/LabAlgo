import json
import math
import os
from testBundle.generateDataset.FixedDataset import FixedDataset


class DatasetGenerator:
    def __init__(self, configFileName):
        self.rootProject = os.path.dirname(os.path.abspath(__file__)) + "/../../"
        self.bundlePath = os.path.join(self.rootProject, "testBundle/")
        self.filename = os.path.join(self.bundlePath, configFileName)
        self.numOfKeysDuplicated = 0
        self.dataSets = None
        self.ds = None

    def readConfigFile(self):
        with open(self.filename) as f:
            data = json.load(f)
            return data

    def generateDatasetFromConfigFile(self):
        config = self.readConfigFile()
        testCases = config["testCases"]
        rangeSettings = config["rangeSettings"]
        for testCase in testCases:
            self.dataSets[testCase["percentage"]] = {
                'label': testCase["label"],
                'percentage': testCase["percentage"],
                'elements': {}
            }
        for testCase in testCases:
            for i in range(rangeSettings['minExp'], rangeSettings['maxExp'] + 1):
                values = int(math.pow(rangeSettings['base'], i))
                fixedDaset = FixedDataset(values, testCase["percentage"])
                self.dataSets[testCase["percentage"]]['elements'][values] = {
                    'values': fixedDaset.generateFixedDataset(),
                    'numOfKeysDuplicated': fixedDaset.getNumOfDuplicatedKeys()
                }

    def getDataSet(self):
        if (self.dataSets == None):
            self.dataSets = {}
            self.generateDatasetFromConfigFile()
        return self.dataSets
