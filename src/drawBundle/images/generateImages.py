from drawBundle.graph import AbrImagesHandler as aih


abrImageHandler = aih.AbrImagesHandler()


def saveBalacedTree():
    g = aih.createBalancedGraph()
    abrImageHandler.saveGraphImg(g, "balancedTree.png")


def saveNxBalancedTree():
    tree = aih.createBalancedTree()
    abrImageHandler.saveGraphImg(tree, "balancedTreeNx.png")


def saveUnbalancedTree():
    values = []
    for i in range(1, 5):
        values.append(i)
    g = aih.createNxCustomGraphFromValues(values)
    abrImageHandler.saveGraphImg(g, "unbalancedTree.png")


def generateExampleTree():
    values = [6, 4, 7, 2, 5, 8]
    g = aih.createNxCustomGraphFromValues(values)
    abrImageHandler.saveGraphImg(g, "exampleTree.png")


def createImages():
    saveBalacedTree()
    saveNxBalancedTree()
    saveUnbalancedTree()
    generateExampleTree()


createImages()
