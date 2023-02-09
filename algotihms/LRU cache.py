class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.h = {}
        self.list = LinkedList()

    def get(self, key: int) -> int:
        if key in self.h:
            node = self.h[key]
            self.list.remove(node)
            self.list.add(node.value, key)
            self.h[key] = self.list.tail
            print(node.value)
            return node.value
        print(-1)
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            self.list.remove(self.h[key])
        else:
            if self.list.count == self.capacity:
                head = self.list.head
                self.list.remove(head)
                del self.h[head.key]

        self.list.add(value, key)
        self.h[key] = self.list.tail
        self.list.tail.key = key


class Node:
    def __init__(self, value, key):
        self.value = value
        self.next = None
        self.prev = None
        self.key = key

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add(self, value, key):
        if not self.head:
            self.head = Node(value, key)
            self.tail = self.head
        else:
            node = Node(value, key)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.count += 1

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        else:
            prev = node.prev
            next = node.next

            if prev:
                prev.next = next
            if next:
                next.prev = prev

        self.count -= 1

    def print_(self):
        node = self.head
        while node:
            print(node, end=' ')
            node = node.next

        print('')


lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)