class Heap:
    def __init__(self, lst, n):
        self.length = n             # size of heap
        self.heap = [None] * [n+1]  # initialize an empty Heap list.
        self.last = 0               # index where the last item was inserted

        for x in lst:
            self.heap_insert(x)
    

    def heap_insert(self, item):
        self.last += 1
        if self.last <= self.length:
            self.heap[self.last] = item
        else:
            self.length += 1        # if heap is already full
            self.heap += [None]
            self.heap[self.last] = item

        self.bubble_up()

    def bubble_up(self):
        '''
        Find appropriat location for the item being inserted that satisfy either min-heap or max-heap property in O(logN) operation.
        Min-heap: self.heap[parent] > self.heap[current]
        Max-heap: self.heap[parent] < self.heap[current]
        ''' 
        parent = self.last / 2
        current = self.last

        while (self.heap[parent] > self.heap[current] and parent > 0):  # For Min-heap
            self.heap[parent], self.heap[current] = self.heap[current], self.heap[parent]
            current = parent
            parent /= 2

    def extract_minmax(self):
        if self.length >= 1:
            minn = self.heap[1]
            self.length -= 1
            self.heap[1], self.heap[self.last] = self.heap[self.last], self.heap[1]     # swap root with last element
            self.last -= 1          # decrement length
            self.heap.pop(-1)       # pop the root that was moved to the last element

            if self.length > 1:     # coz first item is None
                if self.length <= 2:
                    self.heap[1:] = sorted(self.heap[1:]) # Use reverse=True for Max-heap
                else:
                    self.bubble_down()
    
        return minn

    def bubble_down(self):
        '''
        After removal of the root this operation is done to maintain the heap property, called Heapify in O(logN) operation.
        '''
        current = 1
        left_child = current * 2
        right_child = current * 2 + 1

        while True:
            if  ( left_child <= self.length and right_child <= self.length ) and \
                ( current <= (self.length / 2) and ( self.heap[current] > self.heap[left_child] or self.heap[current] > self.heap[right_child] ) ) :
                '''
                If both children indices are within self.length
                '''
                #use max for max-heap
                #find the index of the element largest of the three
                #current element and two children

                ind=min((left_child,right_child),key=lambda x:self.heap[x])
                self.heap[current],self.heap[ind]=self.heap[ind],self.heap[current]
                current=ind
                left_child=current*2
                right_child=(current*2)+1
            elif left_child==self.length  and (current <=(self.length/2) and (self.heap[current] > self.heap[left_child])):
                """
                if left_child is the last element in the heap
                """
                self.heap[current],self.heap[ind]=self.heap[ind],self.heap[current]
                break
            else:
                """
                If none of the children indexes lie withing self.length
                """

