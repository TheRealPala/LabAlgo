import random
import sys


# 1 è il valore di chiave duplicato
# da 2 a lenght si hanno tutte le chiavi non duplicate
def generateFixedDataset(length, percentageOfDuplicates):
    if percentageOfDuplicates < 0 or percentageOfDuplicates > 1:
        sys.stderr.write("Percentage of duplicates must be between 0 and 1")
        percentageOfDuplicates = 0.3
        sys.stderr.write("Percentage of duplicates set to 30%")
    numOfFlatKeys = int(length * (1 - percentageOfDuplicates))
    numOfDuplicateKeys = length - numOfFlatKeys
    list = []
    for i in range(2, numOfFlatKeys + 2):
        list.append(i)
    for i in range(numOfDuplicateKeys):
        list.append(1)
    random.shuffle(list)
    return list


def getNumOfDuplicatedKeys(length, percentageOfDuplicates):
    if percentageOfDuplicates < 0 or percentageOfDuplicates > 1:
        sys.stderr.write("Percentage of duplicates must be between 0 and 1")
        percentageOfDuplicates = 0.3
        sys.stderr.write("Percentage of duplicates set to 30%")
    numOfFlatKeys = int(length * (1 - percentageOfDuplicates))
    numOfDuplicateKeys = length - numOfFlatKeys
    return numOfDuplicateKeys
