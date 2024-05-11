from src.testBundle.generateDataset import generateFixedDataset as genDataSet
import os
import json
from src.testBundle.timer import Timer as timer


class Test():

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

    def testInsertBack(self, args):
        dataSet = args['dataset']
        bst = args['bst']
        for value in dataSet:
            bst.insert(value)

    def testInsertFront(self, percentage, label):
        dataSet = genDataSet.generateFixedDataset(self.numOfValues, percentage)
        args = {'dataset': dataSet, 'bst': self.abr}
        time = timer.testFunction(self.testInsertBack, args, 2)
        return {
            "time": time,
            "percentage": percentage,
            "numOfValues": self.numOfValues,
            "action": "insert",
            "label": label
        }

    def testInsert(self):
        result = []
        for value in self.testCase:
            tmpRes = self.testInsertFront(value["percentage"], value["label"])
            result.append(tmpRes)
        return result
