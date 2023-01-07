from pythonds.basic import Stack
from pythonds.trees import BinarySearchTree


def order1(node, s):                    #使用栈
    order = []
    while node or s.size() > 0:
        if node:
            s.push(node)
            node = node.leftChild
        else:
            node = s.pop()
            order.append(node.key)
            node = node.rightChild
    return order


def order2(node):                    #使用findSuccessor
    order = []
    x = node.findMin()
    for i in range(a.length()):
        order.append(x.key)
        x = x.findSuccessor()
    return order


a = BinarySearchTree()
a.put(70, 70)
a.put(14, 14)
a.put(93, 93)
a.put(94, 94)
a.put(31, 31)
a.put(23, 23)
a.put(73, 73)
s = Stack()
print(order1(a.root, s))
print(order2(a.root))
