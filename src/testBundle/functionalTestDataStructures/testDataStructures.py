from mainBundle.booleanBst.BBSTree import BBSTree
from mainBundle.bst.BSTree import BSTree
from mainBundle.linkedListBundle.LLBSTree import LLBSTree

def tryBst():
    bst = BSTree()
    values = [3, 5, 2, 3, 4, 6, 7, 3, 2, 3];
    for value in values:
        bst.insert(value)
    bst.inorderTreeWalk(bst.getRoot())
    valuesFound = bst.find(3)
    print(f'Number of values founded:{len(valuesFound)}')
    print(f'List:{valuesFound}')

def tryBbst():
    bbst = BBSTree()
    values = [9, 5, 3, 10, 3, 4, 3, 3]
    for value in values:
        bbst.insert(value)
    bbst.inorderTreeWalk(bbst.getRoot())
    valuesFound = bbst.multipleFindFront(3)
    print(f'Number of values founded:{len(valuesFound)}')
    print(f'List:{valuesFound}')
def tryLLBst():
    llbst = LLBSTree()
    values = [9, 5, 3, 10, 3, 4, 3, 3, 2, 3]
    for value in values:
        llbst.insert(value)
    llbst.inorderTreeWalk(llbst.getRoot())
    head = llbst.find(3)
    print(f'Number of values founded: {head.getCount()}')
    head.showAllNextValues()