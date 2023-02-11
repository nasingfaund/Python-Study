"""
https://leetcode.com/problems/lru-cache/description/

Input:
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

Output:
    [null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:
    cache = LRUCache(2);
    cache.put(1, 1); // cache is {1=1}
    cache.put(2, 2); // cache is {1=1, 2=2}
    cache.get(1);    // return 1
    cache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    cache.get(2);    // returns -1 (not found)
    cache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    cache.get(1);    // return -1 (not found)
    cache.get(3);    // return 3
    cache.get(4);    // return 4
"""
class Node:
    def __init__(self, key, value):
        self.value = value
        self.next = None
        self.key = key
        self.prev = None


class LinkedList:

    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def append(self, key, value) -> Node:
        node = Node(key, value)

        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.count += 1
        return self.tail

    def remove(self, node):
        if self.count == 1:
            self.head = self.tail = None
        elif node == self.head:
            self.head = self.head.next
        elif node == self.tail:
            self.tail = self.tail.prev
        else:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
        self.count -= 1


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.nodes = LinkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.nodes.remove(node)
            self.cache[key] = self.nodes.append(key, node.value)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.nodes.remove(self.cache[key])
        if self.nodes.count == self.capacity:
            head = self.nodes.head
            del self.cache[head.key]
            self.nodes.remove(head)

        self.cache[key] = self.nodes.append(key, value)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)