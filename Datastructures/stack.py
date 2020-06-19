from Datastructures.doubly_linked_list import LinkedList

class EmptyStackException(Exception):
    pass

class Stack:
    def __init__(self):
        self._stack = LinkedList()

    def push(self, data):
        self._stack.insert_at_tail(data)

    def pop(self):
        if self.is_empty():
            raise EmptyStackException("Stack is Empty")
        temp = self._stack.tail.data
        self._stack.delete_at_tail()
        return temp

    def peek(self):
        return self._stack.tail.data

    def is_empty(self):
        return self._stack.head is None and self._stack.tail is None

    def __repr__(self):
        return str(self._stack)

    def __str__(self):
        return self.__repr__()

stack = Stack()
breakpoint()
stack.push(3)