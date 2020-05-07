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
        if l <= self.heapSize and self.heapArr[l] > self.heapArr[idx]:
            largest = l
        else:
            largest = idx

        # Comparing with the right child.
        if r <= self.heapSize and self.heapArr[r] > self.heapArr[largest]:
            largest = r

        # If the parent Node is less than the leftchild or rightchild.
        if largest != idx:

            # Swap the largest of the three nodes with the parent.
            self.heapArr[idx], self.heapArr[largest] = self.heapArr[largest], self.heapArr[idx]
            self.heapify(largest)

    # Extracting the root of the heap.
    def extractMax(self):
        if self.heapSize > 0:
            res = self.heapArr[1]
            self.heapArr[1], self.heapArr[self.heapSize] = self.heapArr[self.heapSize], self.heapArr[1]
            self.heapSize -= 1
            if self.heapSize != 0:
                self.heapify(1)
            return res

    # HeapSort function.
    def heapSort(self):
        for i in range(self.heapSize, 0, -1):
            val = self.extractMax()
            self.heapArr[i] = val

    # Building maxHeap of a given array.
    def buildHeap(self, A):
        self.heapSize = len(A)
        self.heapArr = [0] + A
        idx = self.parent(self.heapSize)
        for i in range(idx, 0, -1):
            self.heapify(i)

    def PrintSorted(self):
        for i in range(1, len(self.heapArr)):
            print(self.heapArr[i], end = ' ')
        print()

# HeapSort
# Taking in input.
try:
    gotdata = sys.argv[1]
except IndexError:
    print("Enter proper Input")
    exit()

A = list(map(int,sys.argv[1].split(',')))

# Building empty heap.
h = maxHeap()

# Building heap of the give heap.
h.buildHeap(A)

# Sorting the given array using heapSort.
h.heapSort()

# Displaying the sorted array.
h.PrintSorted()
