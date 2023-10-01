'''
How is Min Heap represented ? 
A Min Heap is a Complete Binary Tree. 
A Min heap is typically represented as an array. The root element will be at Arr[0]. For any ith node, i.e., Arr[i]:

Arr[(i -1) / 2] returns its parent node.
Arr[(2 * i) + 1] returns its left child node.
Arr[(2 * i) + 2] returns its right child node.
Operations on Min Heap : 

getMin(): It returns the root element of Min Heap. Time Complexity of this operation is O(1).
extractMin(): Removes the minimum element from MinHeap. Time Complexity of this Operation is O(Log n) as this operation needs to maintain the heap property (by calling heapify()) after removing root.
insert(): Inserting a new key takes O(Log n) time. We add a new key at the end of the tree. If new key is larger than its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.
'''

import sys

class MinHeap:
    def __init__(self):
        self.arr = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * 1 + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def insert(self, key):
        self.arr.append(key)

        current = len(self.arr)
        parent = self.parent(current)

        while parent >= 0:
            if key < self.arr[parent]:
                self.arr[parent], self.arr[current] = self.arr[current], self.arr[parent]
                current = parent
                parent = self.parent(current)


    def MinHeapify(self, parent_index):
        
        n = len(self.arr)

        
        parent_val = self.arr[parent_index]
        l_child_index = self.left_child(parent_index)
        r_child_index = self.right_child(parent_index)
        
        if l_child_index >= n:
            return

        if r_child_index >= n and l_child_index < n:
            l_child_val = self.arr[l_child_index]
            
            if parent_val > l_child_val:
                self.arr[parent_index], self.arr[l_child_index] = self.arr[l_child_index], self.arr[parent_index]
            
            return
        
     
            
        l_child_val = self.arr[l_child_index]
        r_child_val = self.arr[r_child_index]
                    
    
        min_child_val = min(l_child_val, r_child_val)

        if parent_val < min_child_val:
            return 

        if l_child_val < r_child_val:
            self.arr[parent_index], self.arr[l_child_index] = self.arr[l_child_index], self.arr[parent_index]
            parent_index = l_child_index
        else:
            self.arr[parent_index], self.arr[r_child_index] = self.arr[r_child_index], self.arr[parent_index]
            parent_index = r_child_index

        self.MinHeapify(parent_index)



        






    def extractMin(self):
        arr = self.arr

        # swap the 1st and last element in the heap array.
        arr[0], arr[-1] = arr[-1], arr[0]

        Min = arr[-1]
        
        arr.pop()

        self.MinHeapify(0)

        return Min
        

    def decrease(self, i, x):
        pass

    def delete(self, i):
        pass 




    


