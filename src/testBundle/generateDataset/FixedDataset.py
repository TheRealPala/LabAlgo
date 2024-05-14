import random
import sys


# 1 è il valore di chiave duplicato
# da 2 a lenght si hanno tutte le chiavi non duplicate

class FixedDataset:
    def __init__(self, length, percentageOfDuplicates):
        self.length = length
        self.percentageOfDuplicates = percentageOfDuplicates

    def generateFixedDataset(self):
        if self.percentageOfDuplicates < 0 or self.percentageOfDuplicates > 1:
            sys.stderr.write("Percentage of duplicates must be between 0 and 1")
            self.percentageOfDuplicates = 0.3
            sys.stderr.write("Percentage of duplicates set to 30%")
        numOfFlatKeys = int(self.length * (1 - self.percentageOfDuplicates))
        numOfDuplicateKeys = self.length - numOfFlatKeys
        list = []
        for i in range(2, numOfFlatKeys + 2):
            list.append(i)
        for i in range(numOfDuplicateKeys):
            list.append(1)
        random.shuffle(list)
        return list

    def getNumOfDuplicatedKeys(self):
        if self.percentageOfDuplicates < 0 or self.percentageOfDuplicates > 1:
            sys.stderr.write("Percentage of duplicates must be between 0 and 1")
            percentageOfDuplicates = 0.3
            sys.stderr.write("Percentage of duplicates set to 30%")
        numOfFlatKeys = int(self.length * (1 - self.percentageOfDuplicates))
        numOfDuplicateKeys = self.length - numOfFlatKeys
        return numOfDuplicateKeys
