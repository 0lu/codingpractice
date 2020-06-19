class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        self.head = Node(data, self.head)
        self.tail = self.head if not self.tail else self.tail

    def insert_at_tail(self, data):
        self.tail.next = Node(data)
        self.tail = self.tail.next
        self.head = self.tail if not self.tail else self.head

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
        prev = None
        while curr and i < index:
            prev = curr
            curr = curr.next

        if i != index:
            raise IndexError("Index exceeded")
        prev.next = Node(data)
        prev.next.next = curr

    def delete(self, data):
        curr = self.head
        prev = None

        while curr and curr.data != data:
            prev = curr
            curr = curr.next

        if not curr:
            return False

        if not prev:
            self.head = curr.next
            return True

        prev.next = curr.next
        return True

    def __str__(self):
        curr = self.head
        result = ""
        while curr:
            result += f"{str(curr.data)} -> "
            curr = curr.next
        return result

    def __repr__(self):
        return self.__str__()
