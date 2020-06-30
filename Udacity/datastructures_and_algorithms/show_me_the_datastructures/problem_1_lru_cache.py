

class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"Node({self.key}, {self.value})"

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
        if not self.tail:
            return

        if self.tail.prev:
            self.tail.prev.next = self.tail.next
        self.tail = self.tail.prev

        if not self.tail:
            self.head = None

    def __str__(self):
        curr = self.head
        result = ""
        while curr:
            result += f"{curr.key}:{curr.value} ->"
            curr = curr.next
        return result



class LRU_Cache:
    def __init__(self, size):
        self.map = {}
        self.list = LinkedList()
        self.size = size

    def set(self, key, value):
        if self.size == 0:
            return
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

    def get(self, key):
        if key not in self.map:
            return -1

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


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)



print(our_cache.get(1))
#-1
print(our_cache.get(2))
#2
print(our_cache.get(9))
#-1
print(our_cache.get(""))
#-1

our_cache.set("", "")
print(our_cache.get(""))
#

our_cache.set("", "..")
print(our_cache.get(""))
#..

our_cache = LRU_Cache(0)
print(our_cache.get("s"))
#-1

our_cache.set(1,2)
print(our_cache.get(1))
#-1