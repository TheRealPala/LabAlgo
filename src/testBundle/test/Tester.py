from src.testBundle.generateDataset import generateFixedDataset as genDataSet
import os
import json
from src.testBundle.timer import Timer as timer

class Tester():

    def __readTestCase(self):
        with open(self.filename) as f:
            data = json.load(f)
            data = data["testCases"]
            return data

    def __init__(self, configFileName, numOfValues, abr):
        self.bst = None
        self.rootProject = os.path.dirname(os.path.abspath(__file__)) + "/../../"
        self.bundlePath = os.path.join(self.rootProject, "testBundle/")
        self.filename = os.path.join(self.bundlePath, configFileName)
        self.numOfValues = numOfValues
        self.testCase = self.__readTestCase()
        self.abr = abr

    def testInsert(self, dataSet):
        for value in dataSet:
            self.bst.insert(value)

    def testInsertFront(self, percentage):
        dataSet = genDataSet.generateFixedDataset(self.numOfValues, percentage)
        time = timer.testFunction(self.testInsert, dataSet)
        return {
            "time": time,
            "percentage": percentage,
            "numOfValues": self.numOfValues
            "action": "insert"
        }