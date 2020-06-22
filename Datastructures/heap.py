from abc import ABCMeta, abstractmethod

class EmptyHeapException(Exception):
    pass

class Heap(metaclass=ABCMeta):
    def __init__(self):
        self._heap = []

    def insert(self, value):
        self._heap.append(value)
        self._percolate_up(len(self._heap) - 1)

    def remove(self):
        if len(self._heap) == 0:
            raise EmptyHeapException("heap is empty")
        temp = self._heap[0]
        self._heap[0] = self._heap[-1]
        del self._heap[-1]
        self._percolate_down(0)
        return temp

    def top(self):
        return self._heap[0]

    @abstractmethod
    def _percolate_up(self, index):
        pass

    @abstractmethod
    def _percolate_down(self, index):
        pass

    @classmethod
    def build_heap(cls, array):
        heap = cls()
        heap._heap = array
        for i in range((len(heap._heap) - 1) // 2, -1, -1):
            heap._percolate_down(i)
        return heap

class MinHeap(Heap):
    def _percolate_up(self, index):
        if index <= 0:
            return
        p_index = (index - 1) // 2
        c_index = index
        min_index = p_index if self._heap[p_index] < self._heap[c_index] else c_index
        if min_index != p_index:
            self._heap[min_index], self._heap[p_index] = self._heap[p_index], self._heap[min_index]
            self._percolate_up(p_index)

    def _percolate_down(self, index):
        if index >= len(self._heap) - 1:
            return

        p_index = index
        l_index = (p_index * 2) + 1
        r_index = (p_index * 2) + 2

        l_child = self._heap[l_index] if (len(self._heap) - 1) >= l_index else None
        r_child = self._heap[r_index] if (len(self._heap) - 1) >= r_index else None

        min_index = p_index
        min_index = l_index if l_child and l_child < self._heap[min_index] else min_index
        min_index = r_index if r_child and r_child < self._heap[min_index] else min_index

        if min_index != p_index:
            self._heap[min_index], self._heap[p_index] = self._heap[p_index], self._heap[min_index]
            self._percolate_down(min_index)


class MaxHeap(Heap):
    def _percolate_up(self, index):
        if index <= 0:
            return
        p_index = (index - 1) // 2
        c_index = index
        max_index = p_index if self._heap[p_index] > self._heap[c_index] else c_index
        if max_index != p_index:
            self._heap[max_index], self._heap[p_index] = self._heap[p_index], self._heap[max_index]
            self._percolate_up(p_index)

    def _percolate_down(self, index):
        if index >= len(self._heap) - 1:
            return

        p_index = index
        l_index = (p_index * 2) + 1
        r_index = (p_index * 2) + 2

        l_child = self._heap[l_index] if (len(self._heap) - 1) >= l_index else None
        r_child = self._heap[r_index] if (len(self._heap) - 1) >= r_index else None

        max_index = p_index
        max_index = l_index if l_child and l_child > self._heap[max_index] else max_index
        max_index = r_index if r_child and r_child > self._heap[max_index] else max_index

        if max_index != p_index:
            self._heap[max_index], self._heap[p_index] = self._heap[p_index], self._heap[max_index]
            self._percolate_down(max_index)


heap = MinHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(2)
print(heap.remove())
print(heap.remove())
print(heap.remove())
print(heap.remove())

heap2 = MaxHeap()
heap2.insert(2)
heap2.insert(5)
heap2.insert(20)
heap2.insert(10)
print(heap2.remove())
print(heap2.remove())
print(heap2.remove())
print(heap2.remove())

heap3 = MinHeap.build_heap([5, 4, 3, 2, 1])
print(heap3.remove())
print(heap3.remove())
print(heap3.remove())
print(heap3.remove())
print(heap3.remove())

heap4 = MaxHeap.build_heap([1, 2, 3, 4, 5])
print(heap4.remove())
print(heap4.remove())
print(heap4.remove())
print(heap4.remove())
print(heap4.remove())
