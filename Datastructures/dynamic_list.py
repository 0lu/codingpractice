
class ListIsEmptyException(Exception):
    pass

class InvalidIndexException(Exception):
    pass

class DynamicList:
    def __init__(self):
        self._size = 10
        self._index = 0
        self._list = [None] * self._size

    def append(self, value):
        if self._check_if_full():
            self._double_list_size()
        self._list[self._index] = value
        self._index += 1

    def pop(self):
        if self._check_if_empty():
            raise ListIsEmptyException("List is empty")
        temp = self._list[self._index - 1]
        self._list[self._index - 1] = None
        self._index -= 1
        return temp

    def get(self, index):
        if index < 0 or index > self._size - 1:
            raise InvalidIndexException(f"{index} is not valid, max index is {self._size - 1}")
        return self._list[index]

    def delete(self, index):
        if index < 0 or index > self._size - 1:
            raise InvalidIndexException(f"{index} is not valid, max index is {self._size - 1}")
        temp = self._list[index]
        for i in range(index, self._index):
            self._list[i] = self._list[i + 1]
        self._list[self._index] = None
        self._index -= 1
        return temp

    def delete_value(self, value):
        found = False
        position = 0
        for index, item in enumerate(self._list):
            if item == value:
                position = index
                found = True
                break
        if found:
            self.delete(position)

    def __repr__(self):
        return str(self._list)

    def __str__(self):
        return str(self._list)

    def _check_if_full(self):
        return self._index == self._size - 1

    def _check_if_empty(self):
        return self._index == 0

    def _double_list_size(self):
        self._size *= 2
        new_list = [None] * (self._size)
        for index in range(len(self._list)):
            new_list[index] = self._list[index]
        self._list = new_list
