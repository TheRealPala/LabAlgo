# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.drawBundle import AbrImagesHandler as aih

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    abrImageHandler = aih.AbrImagesHandler()
    g = aih.createExampleGraph()
    aih.drawGraph(g)
    abrImageHandler.saveGraphImg(g, "exampleBtree.png")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
