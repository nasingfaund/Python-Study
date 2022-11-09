class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:

    def __init__(self):
        self.__head = None
        self.__count = 0

    def add(self, value):

        node = Node(value)

        if not self.__head:
            self.__head = node
        else:
            tail = self.__get_node_by_index(self.__count - 1)
            tail.next = node

        self.__count += 1

    def __get_node_by_index(self, index):
        if index not in range(0, self.__count):
            raise Exception('index out of range')
        node = self.__head

        for _ in range(index):
            node = node.next
        return node

    def print(self):

        if self.__count == 0:
            print('empty list')
            return

        for i in range(self.__count):
            print(self.__get_node_by_index(i).value, end=' ')
        print()

    def remove(self, index):

        if index not in range(0, self.__count):
            raise Exception('index out of range')

        if index == 0:
            self.__head = self.__head.next
        else:
            node = self.__get_node_by_index(index - 1)
            prev = node
            next = prev.next.next
            prev.next = next

        self.__count -= 1

    def insert(self, index, value):
        if index not in range(0, self.__count):
            raise Exception('index out of range')

        newNode = Node(value)

        if index == 0:
            newNode.next = self.__head
            self.__head = newNode
        else:

            node = self.__get_node_by_index(index - 1)
            prev = node
            newNode.next = prev.next
            prev.next = newNode

        self.__count += 1

    def reverse(self):
        current = self.__head
        prev = None

        while current:
            # запомним ссылку на следующий элемент после текущего, т.к. следующим действием мы эту ссылку перезапишем
            temp = current.next
            # следующий становится предыдущим (меняем элементы местами)
            current.next = prev
            # предыдущий становится текущим, т.к. двигаемся вперед
            prev = current
            # текущий становится temp, то есть следующим
            current = temp

        self.__head = prev

    @property
    def count(self):
        return self.__count


l = LinkedList()
l.add(1)
l.add(3)
l.add(222)
l.add(2)
l.add(55)
l.print()

l.remove(0)
l.insert(3, 199)
l.print()
print(l.count)

linked_list = LinkedList()

commands_map = {
    'add': lambda: linked_list.add(int(input('value = '))),
    'r': lambda: linked_list.remove(int(input('index = '))),
    'c': lambda: print(f'elements count: {linked_list.count}'),
    'p': linked_list.print,
    'i':
        (
            lambda: linked_list.insert(
                int(input('index: ')),
                int(input('value: '))
            )
        ),
    'rev': linked_list.reverse,
}

try:

    linkedList = LinkedList()
    message = 'input one from the next commands (add=add, r=remove, c=count, p=print, i=insert, exit=exit, rev=reverse)'

    while True:

        print('\n')
        input_ = input(f'{message}: ')

        if input_ == 'exit':
            print('exit')
            break

        method = commands_map.get(input_, None)

        if not method:
            print(f"command '{input_}' does not exists")
            continue
        else:
            method()

except Exception as e:
    print(e)
