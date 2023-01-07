class Node:
    def __init__(self, indata):
        self.data = indata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class Deque:                                      #链表头为后端，链表尾为前端
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def addFront(self, item):
        temp = Node(item)
        tail = self.head
        len = self.size()
        for i in range(len - 1):
            tail = tail.getNext()
        tail.setNext(temp)

    def addRear(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def removeRear(self):
        self.head = self.head.getNext()

    def removeFront(self):
        sec_tail = self.head
        len = self.size()
        for i in range(len - 2):
            sec_tail = sec_tail.getNext()
        sec_tail.setNext(None)

    def show(self):
        n = self.size()
        l = []
        pin = self.head
        for i in range(n):
            l.append(pin.getData())
            pin = pin.getNext()
        return l


d = Deque()
d.isEmpty()
d.addRear(4)
d.addRear('dog')
print(d.show())
d.addFront('cat')
d.addFront(True)
print(d.show())
print(d.size())
d.addRear(8.4)
print(d.show())
d.removeRear()
print(d.show())
d.removeFront()
print(d.show())


