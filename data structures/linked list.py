class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:

    def __init__(self):
        self.__head = None
        self.count = 0

    def add(self, value):

        node = Node(value)

        if self.__head is None:
            self.__head = node
        else:
            tail = self.__head

            while tail.next is not None:
                tail = tail.next

            tail.next = node

        self.count += 1

    def print(self):

        if self.count == 0:
            print('empty list')
            return

        head = self.__head
        print(head.value, end=' ')

        while head.next is not None:
            head = head.next
            print(head.value, end=' ')

    def remove(self, index):

        if index not in range(0, self.count):
            raise Exception('index out of range')

        if index == 0:
            self.__head = self.__head.next
        else:
            node = self.__head

            for i in range(0, index - 1):
                node = node.next

            prev = node
            next = prev.next.next
            prev.next = next

        self.count -= 1

    def insert(self, index, value):
        if index not in range(0, self.count):
            raise Exception('index out of range')

        newNode = Node(value)

        if index == 0:
            newNode.next = self.__head
            self.__head = newNode
        else:

            node = self.__head

            for i in range(0, index - 1):
                node = node.next

            prev = node
            newNode.next = prev.next
            prev.next = newNode

        self.count += 1


try:

    linkedList = LinkedList()
    message = 'input command (a=add, r=remove, c=count, p=print, i=insert, e=exit)'

    while True:

        print('\n')
        s = input(f'{message}: ')

        if s == 'a':
            value = int(input('value = '))
            linkedList.add(value)
            continue

        if s == 'r':
            index = int(input('index = '))
            linkedList.remove(index)
            continue

        if s == 'c':
            print(f'elems count: {linkedList.count}')
            continue

        if s == 'p':
            linkedList.print()
            continue

        if s == 'i':
            index = int(input('index: '))
            value = int(input('value: '))
            linkedList.insert(index, value)
            continue

        if s == 'e':
            print('exit')
            break

except Exception as e:
    print(e)



# написать юнит тест
