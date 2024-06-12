import copy
import json
import os

from tqdm import tqdm
import time
import math

from src.testBundle.test import Test
from src.testBundle.generateDataset.DatasetGenerator import DatasetGenerator
filename = "settings.json"

def readsTestDataParameters():
    absPath = os.path.dirname(os.path.abspath(__file__)) + "/../"
    filePath = os.path.join(absPath, filename)
    with open(filePath) as f:
        data = json.load(f)
        data = data["rangeSettings"]
        return data

def runTest(abr, parameters, dataSets):
    valuesToInsert = []
    results = []
    for i in range(parameters['minExp'], parameters['maxExp'] + 1):
        valuesToInsert.append(int(math.pow(parameters['base'], i)))
    for i in (bar := tqdm(valuesToInsert)):
        bar.set_description(f"{abr}: Testing with {i} values")
        t = Test.Test(filename, i, abr, dataSets)
        results.append(t.testActions())
        time.sleep(0.3)
    return results


def runAllTests():
    results = {}
    parameters = readsTestDataParameters()
    dataSetGen = DatasetGenerator('settings.json')
    dataSets = dataSetGen.getDataSet()
    results["abr"] = runTest("bst", parameters, dataSets)
    results["boolean"] = runTest("boolean", parameters, dataSets)
    results["linked"] = runTest("linked", parameters, dataSets)
    return results


def elaborateInsertResults(results):
    values = {}
    tmp = {}
    for abr in results:
        for result in results[abr]:
            for tmpRes in result:
                tmp[tmpRes["percentage"]] = {"label": tmpRes["label"], "values": []}
        values[abr] = copy.deepcopy(tmp)
    for a in results:
        for r in results[a]:
            for t in r:
                values[a][t["percentage"]]["values"].append({"numOfValues": t["numOfValues"],"time": t["timeInsert"]})
    return values
def elaborateFindResults(results):
    values = {}
    tmp = {}
    for abr in results:
        for result in results[abr]:
            for tmpRes in result:
                tmp[tmpRes["percentage"]] = {"label": tmpRes["label"], "values": []}
        values[abr] = copy.deepcopy(tmp)
    for a in results:
        for r in results[a]:
            for t in r:
                values[a][t["percentage"]]["values"].append({"numOfValues": t["numOfValues"],"time": t["timeFind"]})
    return values