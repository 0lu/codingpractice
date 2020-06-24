

class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            self.head.next.prev = self.head

    def delete_at_tail(self):
        self.tail.prev = self.tail.next
        self.tail = self.tail.prev

        if not self.tail:
            self.head = None


class LRUCache:
    def __init__(self, size):
        self.map = {}
        self.list = LinkedList()
        self.size = size

    def add(self, key, value):
        if key in self.map:
            self.map[key].value = value
            return

        if len(self.map) >= self.size:
            to_remove = self.list.tail
            self.list.delete_at_tail()
            del self.map[to_remove.key]

        to_add = Node(key, value)
        self.map[key] = to_add
        self.list.insert_at_head(to_add)

    def search(self, key):
        if key not in self.map:
            return None

        to_return = self.map[key]
        if to_return.prev:
            to_return.prev.next = to_return.next
        else:
            self.list.head = to_return.next
        if to_return.next:
            to_return.next.prev = to_return.prev
        else:
            self.list.tail = to_return.prev

        to_return.next = self.list.head
        self.list.head.prev = to_return
        self.list.head = to_return

        return to_return.value



cache = LRUCache(3)
cache.add(1,2)
cache.add(2,3)
cache.add(3,4)
print(cache.search(1))
cache.add(4,5)
print(cache.search(2))



