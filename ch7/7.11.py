from pythonds.graphs import PriorityQueue, Graph, Vertex
from pythonds.basic import Queue, Stack
import sys


def Search(start, end):
    start.setDistance(0)
    start.setPred(None)
    q = Queue()
    q.enqueue(start)
    s = Stack()
    l = []
    while q.size() > 0:
        current = q.dequeue()
        for nbr in current.getConnections():
            if nbr.getColor() == 'White':
                nbr.setDistance(current.getDistance() + current.getWeight(nbr))
                nbr.setColor('Black')
                nbr.setPred(current)
            else:
                if (current.getDistance() + current.getWeight(nbr)) < nbr.getDistance():
                    nbr.setDistance(current.getDistance() + current.getWeight(nbr))
                    nbr.setPred(current)
            q.enqueue(nbr)

    s.push(end)
    while end.getPred():
        end = end.getPred()
        s.push(end)

    if s.peek() != start:
        return 'There is no way.'
    else:
        while not s.isEmpty():
            l.append(s.pop().id)
        return l


g = Graph()
l = ['u', 'v', 'w', 'x', 'y', 'z']
g.addEdge('u', 'v', 2)
g.addEdge('v', 'w', 3)
g.addEdge('w', 'z', 5)
g.addEdge('u', 'x', 1)
g.addEdge('x', 'y', 1)
g.addEdge('y', 'z', 1)
g.addEdge('u', 'w', 5)
g.addEdge('v', 'x', 2)
g.addEdge('x', 'w', 3)
g.addEdge('y', 'w', 1)

for x in l:
    for y in l:
        if x != y:
            print('The shortest way between', x, 'and', y, ':', Search(g.getVertex(x), g.getVertex(y)))
            for n in l:
                g.getVertex(n).setPred(None)
                g.getVertex(n).setDistance(sys.maxsize)

