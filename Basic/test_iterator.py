class Node:
    def __init__(self, id, val):
        self.id = id
        self.val = val
        self.next = None


class NodeIterator():
    def __init__(self, node):
        self.cur = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur is None:
            raise StopIteration()
        val = self.cur.val
        id = self.cur.id
        self.cur = self.cur.next
        return id, val


a = Node(1, 'a')
b = Node(2, 'b')
c = Node(3, 'c')
d = Node(4, 'd')

a.next = b
b.next = c
c.next = d

ni = NodeIterator(a)
ni2 = NodeIterator(a)

print(id(ni), id(ni2))

for x in ni:
    print(x)
