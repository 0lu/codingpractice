from Datastructures.doubly_linked_list import LinkedList

class QueueEmptyException(Exception):
    pass


class Queue:
    def __init__(self):
        self._queue = LinkedList()

    def enqueue(self, data):
        self._queue.insert_at_tail(data)

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyException()

        temp = self._queue.head.data
        self._queue.delete_at_head()
        return temp

    def peek(self):
        return self._queue.head.data

    def is_empty(self):
        return self._queue.head is None and self._queue.tail is None

    def __repr__(self):
        return str(self._queue)

    def __str__(self):
        return self.__repr__()

queue = Queue()
