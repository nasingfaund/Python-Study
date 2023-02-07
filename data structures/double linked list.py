class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.__count = 0

    @property
    def count(self):
        return self.__count

    def add(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self.__count += 1
            return

        node = Node(value)
        self.tail.next = node
        node.prev = self.tail

        self.tail = node
        self.__count += 1

    def find_by_index(self, index):
        node = self.head

        for _ in range(index):
            node = node.next

        return node

    def remove(self, index):
        target_node = self.find_by_index(index)

        if index == self.count - 1 and index > 0:
            target_node.prev.next = None
            self.tail = target_node.prev

        if index == 0:
            if self.count > 1:
                next_node = target_node.next
                self.head = next_node
                next_node.prev = None
            else:
                self.tail = None
                self.head = None

        if 0 < index < self.count - 1:
            next_node = target_node.next
            prev_node = target_node.prev

            prev_node.next = next_node
            next_node.prev = prev_node

        self.__count -= 1

    def add_(self, *values):
        for value in values:
            self.add(value)

    def print_(self):
        node = self.head
        while node:
            print(node, end=' ')
            node = node.next

        print('')


l = LinkedList()

for i in range(100):
    l.add(i)

for i in range(100):
    l.remove(99 - i)

l.print_()
print(l.count)


