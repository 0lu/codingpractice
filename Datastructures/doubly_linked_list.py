class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        temp = Node(data, None, self.head)
        if self.head:
            self.head.prev = temp
        self.head = temp
        self.tail = self.head if not self.tail else self.tail

    def insert_at_tail(self, data):
        temp = Node(data, self.tail, None)
        if self.tail:
            self.tail.next = temp
        self.tail = temp
        self.head = self.tail if not self.head else self.head

    def is_empty(self):
        return not self.head and not self.tail

    def insert(self, data):
        self.insert_at_head(data)

    def insert_at_index(self, data, index):
        curr = self.head
        if index == 0:
            self.insert_at_head(data)
            return
        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1

        if i != index:
            raise IndexError("Index exceeded")

        temp = Node(data, curr.prev, curr)
        curr.prev.next = temp
        curr.prev = temp

    def delete(self, data):
        curr = self.head

        while curr and curr.data != data:
            curr = curr.next

        if not curr:
            return False

        if curr.prev:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        else:
            self.head = curr.next
        return True

    def delete_at_tail(self):
        if self.head is self.tail:
            self.head = self.tail = None
            return

        self.tail.prev.next = self.tail.next
        self.tail = self.tail.prev

    def delete_at_head(self):
        if self.head is self.tail:
            self.head = self.tail = None
            return

        self.head.next.prev = None
        self.head = self.head.next

    def __str__(self):
        curr = self.head
        result = ""
        while curr:
            result += f"{str(curr.data)} <-> "
            curr = curr.next
        return result

    def __repr__(self):
        return self.__str__()

tem = LinkedList()
tem.insert_at_tail(6)
tem.insert(89)
tem.insert_at_index(78, 0)
print(tem)
print(tem.delete(78))
print(tem)
