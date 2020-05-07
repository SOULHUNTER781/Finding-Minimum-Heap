import sys

class maxHeap:
    # For getting the index of the parent Node.
    def parent(self, idx): return (idx // 2)

    # For getting the index of the leftChild Node.
    def leftChild(self, idx): return (idx * 2)

    # For getting the index of the rightChild Node.
    def rightChild(self, idx): return (idx * 2 + 1)

    # Initializing a empty heap.
    def __init__(self):
        self.heapSize = 0
        self.heapArr = [0]

    # Max_Heapify function for placing parent node in its proper position.
    def heapify(self, idx):
        l = self.leftChild(idx)
        r = self.rightChild(idx)

        # Comparing with the left child.
        if l <= self.heapSize and ord(self.heapArr[l]) > ord(self.heapArr[idx]):
            largest = l
        else:
            largest = idx

        # Comparing with the right child.
        if r <= self.heapSize and ord(self.heapArr[r]) > ord(self.heapArr[largest]):
            largest = r

        # If the parent Node is less than the leftchild or rightchild.
        if largest != idx:

            # Swap the largest of the three nodes with the parent.
            self.heapArr[idx], self.heapArr[largest] = self.heapArr[largest], self.heapArr[idx]
            self.heapify(largest)

    # Building maxHeap of a given array.
    def buildHeap(self, A):
        self.heapSize = len(A)
        self.heapArr = [0] + A
        idx = self.parent(self.heapSize)
        for i in range(idx, 0, -1):
            self.heapify(i)

    # Displaying the heap.
    def displayHeap(self):
        for i in range(1, self.heapSize + 1):
            print(self.heapArr[i], end = " ")
        print()

    # Inserting a node in heap.
    def insert(self, val):
        self.heapSize += 1
        self.heapArr.append(val)
        idx = self.heapSize
        while self.parent(idx) != 0 and ord(val) > ord(self.heapArr[self.parent(idx)]):
            self.heapify(self.parent(idx))
            idx = self.parent(idx)
            
# Taking in input.
try:
    gotdata = sys.argv[1]
except IndexError:
    print("Enter proper Input")
    exit()

A = [x for x in sys.argv[1]]

# Building empty heap.
h = maxHeap()

# Building heap of the give heap.
h.buildHeap(A)
for i in range(2, len(sys.argv)):
    A = [x for x in sys.argv[i]]
    for x in A:
        h.insert(x)

# Displaying the sorted array.
h.displayHeap()
