import sys


# defining a class min_heap for the heap data structure

class min_heap:
    def __init__(self, sizelimit):
        self.sizelimit = sizelimit
        self.cur_size = 0
        self.Heap = [0] * (self.sizelimit + 1)
        self.Heap[0] = sys.maxsize * -1
        self.root = 1

    # helper function to swap the two given nodes of the heap
    # this function will be needed for heapify and insertion to swap nodes not in order
    def swapnodes(self, node1, node2):
        self.Heap[node1], self.Heap[node2] = self.Heap[node2], self.Heap[node1]

    # THE MIN_HEAPIFY FUNCTION
    def min_heapify(self, i):

        # If the node is a not a leaf node and is greater than any of its child
        if not (i >= (self.cur_size // 2) and i <= self.cur_size):
            if (self.Heap[i] > self.Heap[2 * i] or self.Heap[i] > self.Heap[(2 * i) + 1]):
                if self.Heap[2 * i] < self.Heap[(2 * i) + 1]:
                    # Swap the node with the left child and then call the min_heapify function on it
                    self.swapnodes(i, 2 * i)
                    self.min_heapify(2 * i)

                else:
                    # Swap the node with right child and then call the min_heapify function on it
                    self.swapnodes(i, (2 * i) + 1)
                    self.min_heapify((2 * i) + 1)

    # THE HEAPPUSH FUNCTION
    def heappush(self, element):
        if self.cur_size >= self.sizelimit:
            return
        self.cur_size += 1
        self.Heap[self.cur_size] = element
        current = self.cur_size
        while self.Heap[current] < self.Heap[current // 2]:
            self.swapnodes(current, current // 2)
            current = current // 2

    # THE HEAPPOP FUNCTION
    def heappop(self):
        last = self.Heap[self.root]
        self.Heap[self.root] = self.Heap[self.cur_size]
        self.cur_size -= 1
        self.min_heapify(self.root)
        return last

    # THE BUILD_HEAP FUNCTION
    def build_heap(self):
        for i in range(self.cur_size // 2, 0, -1):
            self.min_heapify(i)

    # helper function to print the heap
    def Print(self):
        for i in range(1, (self.cur_size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) +
                  " LEFT CHILD : " + str(self.Heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))

    def __repr__(self):
        return str(self.Heap[1:])


minHeap = min_heap(10)
minHeap.heappush(15)
minHeap.heappush(7)
minHeap.heappush(9)
minHeap.heappush(4)
minHeap.heappush(13)
print(minHeap)
# minHeap.Print()

minHeap.heappop()
print(minHeap)
