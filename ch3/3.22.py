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


class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def peek(self):
        return self.head.getData()

    def pop(self):
        temp = self.head.getData()
        self.head = self.head.getNext()
        return temp

    def show(self):
        n = self.size()
        l = []
        pin = self.head
        for i in range(n):
            l.append(pin.getData())
            pin = pin.getNext()
        return l


a = Stack()
a.push(1)
a.push(3)
a.push(6)
a.push(5)
a.push(2)
a.push(4)
print(a.show())
print(a.size())
print(a.peek())
print(a.pop())
print(a.size())
print(a.peek())
print(a.show())
