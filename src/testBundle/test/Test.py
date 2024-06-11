import sys

from src.mainBundle.booleanBst.BBSTree import BBSTree
from src.mainBundle.bst.BSTree import BSTree
from src.mainBundle.linkedListBundle.LLBSTree import LLBSTree
from src.testBundle.generateDataset import FixedDataset
import os
import json
from src.testBundle.timer import Timer as timer


class Test():

    def __readTestCase(self):
        with open(self.filename) as f:
            data = json.load(f)
            data = data["testCases"]
            return data

    def __init__(self, configFileName, numOfValues, bstName):
        self.bst = None
        self.rootProject = os.path.dirname(os.path.abspath(__file__)) + "/../../"
        self.bundlePath = os.path.join(self.rootProject, "testBundle/")
        self.filename = os.path.join(self.bundlePath, configFileName)
        self.numOfValues = numOfValues
        self.testCase = self.__readTestCase()
        self.numOfKeysDuplicated = 0
        self.bstName = bstName
        self.ds = None
    
    def createDataStructure(self):
        if self.bstName == "bst":
            return BSTree()
        elif self.bstName == "boolean":
            return BBSTree()
        else:
            return LLBSTree()


    def testInsertBack(self, args):
        dataSet = args['dataset']
        bst = args['bst']
        for value in dataSet:
            bst.insert(value)

    def testInsertFront(self, percentage, label):
        fd = FixedDataset.FixedDataset(self.numOfValues, percentage)
        dataSet = fd.generateFixedDataset()
        self.ds = dataSet
        self.numOfKeysDuplicated = fd.getNumOfDuplicatedKeys()
        args = {'dataset': dataSet, 'bst': self.bst}
        ret = timer.testFunction(self.testInsertBack, args, 2)
        time = ret['time']
        return {
            "timeInsert": time,
            "percentage": percentage,
            "numOfValues": self.numOfValues,
            "label": label,
            "timeFind": None
        }

    def testFindBack(self, args):
        bst = args['bst']
        res = bst.find(1)
        return res


    def testFindFront(self):
        ret = timer.testFunction(self.testFindBack, {'bst': self.bst}, 2)
        time = ret['time']
        retFunction = ret['retFunction']
        if (retFunction is None):
            print('Error:' + self.bstName)
        else:
            length = len(retFunction)
            if length == 0:
                valuesFound = 0
            else:
                valuesFound = length
            if valuesFound != self.numOfKeysDuplicated:
                print(f'Error: {valuesFound} != {self.numOfKeysDuplicated}')
            return time

    def testActions(self):
        ret = []
        for value in self.testCase:
            self.bst = self.createDataStructure()
            tmpRes = self.testInsertFront(value["percentage"], value["label"])
            timeFind = self.testFindFront()
            tmpRes["timeFind"] = timeFind
            ret.append(tmpRes)
        return ret


