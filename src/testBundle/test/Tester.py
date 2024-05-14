from tqdm import tqdm
import time
import math

from src.mainBundle.booleanBst.BBSTree import BBSTree
from src.mainBundle.bst.BSTree import BSTree
from src.mainBundle.linkedListBundle.LLBSTree import LLBSTree
from src.testBundle.test import Test
def runTest(abr):
    valuesToInsert = []
    results = []
    for i in range(2, 7):
        valuesToInsert.append(int(math.pow(2, i)))
    for i in (bar := tqdm(valuesToInsert)):
        bar.set_description(f"{abr}: Testing with {i} values")
        t = Test.Test("settings.json", i, abr)
        results.append(t.testActions())
        time.sleep(0.3)
    return results

def runAllTests():
    results = {}
    results["abr"] = runTest("bst")
    results["boolean"] = runTest("boolean")
    results["linked"] = runTest("linked")
    print(results)
    return results