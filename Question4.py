import sys

class Node:
    def __init__(self, data, idx):
        self.data = data 
        self.char = idx

class minHeap:
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
    def moveDown(self, idx):
        l = self.leftChild(idx)
        r = self.rightChild(idx)
        # Comparing with the left child.
        if l <= self.heapSize and self.heapArr[l].data < self.heapArr[idx].data :
            smallest = l
        else:
            smallest = idx
        # Comparing with the right child.
        if r <= self.heapSize and self.heapArr[r].data < self.heapArr[smallest].data :
            smallest = r
        # If the parent Node is less than the leftchild or rightchild.
        if smallest != idx:
            # Swap the largest of the three nodes with the parent.
            temp = self.heapArr[idx].char
            self.heapArr[idx].char = self.heapArr[smallest].char
            self.heapArr[smallest].char = temp
            self.heapArr[idx], self.heapArr[smallest] = self.heapArr[smallest], self.heapArr[idx]
            self.moveDown(smallest)

    # Building maxHeap of a given array.
    def buildHeap(self, A):
        self.heapSize = len(A)
        self.heapArr = [0] + A
        idx = self.parent(self.heapSize)
        for i in range(idx, 0, -1):
            self.moveDown(i)

    # Inserting node.
    def moveUp(self, idx):
        key = self.heapArr[idx]
        while self.parent(idx) != 0 and key.data < self.heapArr[self.parent(idx)].data :
            temp = self.heapArr[idx].char
            self.heapArr[idx].char = self.heapArr[smallest].char
            self.heapArr[smallest].char = temp
            self.heapArr[self.parent(idx)], self.heapArr[idx] = self.heapArr[idx], self.heapArr[self.parent(idx)]
            idx = self.parent(idx)

    # Displaying current status.
    def displayStats(self):
        print(len(h.heapArr) - 1)
        for i in range(1, h.heapSize + 1):
            print(self.heapArr[i].data, end = " ") 
            print(self.heapArr[i].char)
        print()

# HeapSort
# Taking in input.
gotdata = []
try:
    gotdata = map(int,sys.argv[1].split(','))
except IndexError:
    print("Enter proper Input")
    exit()

# Creating a min heap of frequencies.
A = []
h = minHeap()
count = 1
for x in gotdata:
    new = Node(x, count)
    A.append(new)
    count += 1
count = 1

h.buildHeap(A)

for i in range(0, len(A)):
    if count % 2 == 1:
        A[i].data -= 1
        h.moveUp(A[i].char)
    else:
        A[i].data += 1
        h.moveDown(A[i].char)
    count += 1

for i in range(1, h.heapSize + 1):
    print(h.heapArr[i].data, end = " ")
print()
