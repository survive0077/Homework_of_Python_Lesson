from pythonds import BinHeap


class PriorityQueue:
    def __init__(self):
        self.queue = BinHeap()

    def enqueue(self, item):
        self.queue.heapList.append(item)

    def dequeue(self):
        self.queue.heapList.pop(1)

    def show(self):
        print(self.queue.heapList[1:])


a = PriorityQueue()
a.enqueue(4)
a.show()
a.enqueue('dog')
a.show()
a.enqueue(True)
a.show()
a.enqueue(8.4)
a.show()
a.dequeue()
a.show()
a.dequeue()
a.show()
