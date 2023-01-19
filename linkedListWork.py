# classes for all work

class Node:
    def __init__(self, dataValue=None):
        self.dataValue = dataValue
        self.nextValue = None
class SinglyLinkedList:
    def __init__(self):
        self.startValue = None
    def listprint(self):
        printValue = self.startValue
        while printValue is not None:
            print(printValue.dataValue)
            printValue = printValue.nextValue


# adding nodes
workingList = SinglyLinkedList()
workingList.startValue = Node("Monday")

node2 = Node("Tuesday")
node3 = Node("Wednesday")

workingList.startValue.nextValue = node2  # links node2 to the first node (startValue)
node2.nextValue = node3  # links node3 to node2


# traversing nodes
workingList.listprint()