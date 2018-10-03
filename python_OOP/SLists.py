###### Part 1 ######
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self, value):
        self.head = Node(value)
    def addNode(self, value):
        runner = self.head
        while(runner.next): ## don't need to check for != None
            runner = runner.next
        runner.next = Node(value)
        return self
    def printAllValues(self, msg=""):
        runner = self.head
        print("\n\nhead points to ", id(self.head))
        print("Printing values in the list ---", msg, "---")
        while(runner.next):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next
        print(id(runner), runner.value, id(runner.next))
        return self
    def removeNode(self, value):
        runner = self.head
        if(runner.value == value):
            self.head = runner.next
            return self
        prevRunner = runner
        while(runner.next and runner.value != value):
            prevRunner = runner
            runner = runner.next
        if(runner.value == value):
            prevRunner.next = runner.next
        return self
    def insertNode(self, value, index):
        i = 0
        node = Node(value)
        runner = self.head
        if(i == index):
            node.next = self.head
            self.head = node
        while(runner.next):
            i += 1
            if(i == index):
                node.next = runner.next
                runner.next = node
            runner = runner.next
        return self


print("\n\n\n=========== START OF THE PROGRAM ===========")
sList = SList(5).addNode(7).addNode(9).addNode(1)
sList.printAllValues("Part 1")

sList.removeNode(12).removeNode(1)
sList.printAllValues("Part 2")

sList.insertNode(12,0)
sList.insertNode(3,1)
sList.printAllValues("Part 3")

