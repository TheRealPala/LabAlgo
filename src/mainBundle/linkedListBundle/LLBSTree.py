from mainBundle.bst.BSTree import BSTree
from mainBundle.linkedListBundle.LLBSNode import LLBSNode


class LLBSTree(BSTree):
    def __init__(self):
        super().__init__()

    def insert(self, key):
        node = LLBSNode(key)
        father = None
        current = self._root
        insideLinkedList = False
        while current is not None and not insideLinkedList:
            father = current
            if node.getKey() < current.getKey():
                current = current.getLeft()
            elif node.getKey() > current.getKey():
                current = current.getRight()
            else:
                insideLinkedList = True
        node.setFather(father)
        if father is None:
            self._root = node
        else:
            if not insideLinkedList:
                if node.getKey() < father.getKey():
                    father.setLeft(node)
                else:
                    father.setRight(node)
            else:
                # change bst pointer to child and father (tipo trapianto ma con aggiornamento anche dei figli)
                node.setFather(father.getFather())
                node.setCount(father.getCount() + 1)
                father.setCount(0)
                if father.getLeft() is not None:
                    node.setLeft(father.getLeft())
                    father.getLeft().setFather(node)
                if father.getRight() is not None:
                    node.setRight(father.getRight())
                    father.getRight().setFather(node)
                if father.getFather() is None:
                    self._root = node
                elif father.getFather().getLeft() is not None and father.__eq__(father.getFather().getLeft()):
                    father.getFather().setLeft(node)
                else:
                    father.getFather().setRight(node)

                father.setFather(node)
                father.setLeft(None)
                father.setRight(None)
                node.setNext(father)

    def find(self, key):
        current = self._root
        while current is not None and current.getKey() != key:
            if key < current.getKey():
                current = current.getLeft()
            else:
                current = current.getRight()
        values = []
        if current is not None:
            while current is not None:
                values.append(current)
                current = current.getNext()
        return values
