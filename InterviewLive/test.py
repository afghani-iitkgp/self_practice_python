
# '''
# Array = {1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17}

# Corresponding Complete Binary Tree is:
#                  1
#               /     \
#             3         5
#          /    \     /  \
#         4      6   13  10
#        / \    / \
#       9   8  15 17
      
# '''


class BinaryMinHeap:
    def __init__(self, arrList):
        self.arrList = arrList
        self.size = len(arrList)

    def swap(self, a, b):
        return b, a


    def parent(self, idx):
        return (idx - 1) // 2
    
    def left(self, idx):
        return 2 * idx + 1
    
    def right(self, idx):
        return 2 * idx + 2

    def minHeapify(self, idx):
        smallest_idx = idx
        left_idx = self.left(idx)
        right_idx = self.right(idx)


        if left_idx < self.size and self.arrList[smallest_idx] > self.arrList[left_idx]:
            smallest_idx = left_idx
        
        if right_idx < self.size and self.arrList[smallest_idx] > self.arrList[right_idx]:
            smallest_idx = right_idx

        if smallest_idx != idx:
            self.arrList[smallest_idx], self.arrList[idx] =  self.arrList[idx], self.arrList[smallest_idx]    
            self.minHeapify(smallest_idx)
              

    def buildHeap(self):
        
        k = self.parent(self.size - 1)
        
        for i in range(k, 0, -1):
            if self.arrList[i] < self.arrList[self.parent(i)]:
                self.arrList[i], self.arrList[self.parent(i)] = self.arrList[self.parent(i)] , self.arrList[i]

                self.minHeapify(self.parent(i))


    def extractMin(self):
        
        self.arrList[self.size-1], self.arrList[0] = self.arrList[0] , self.arrList[self.size-1]

        self.size -= 1
        self.minHeapify(0)

        Min = self.arrList[self.size]
        self.arrList = self.arrList[:self.size]
        # self.size -= 1
    
        print(self.arrList)

        return Min

    def insert(self, ele):
            
        self.arrList.append(ele)
        self.size += 1

        i = self.size - 1

        while i != 0:
            if self.arrList[i] < self.arrList[self.parent(i)]:                
                self.arrList[self.parent(i)], self.arrList[i] = self.arrList[i], self.arrList[self.parent(i)]    
                i = self.parent(i)
            else:
                # We know that rest of the tree is already heapified.
                break


    def decreaseKey(self, idx, ele):
        '''
        Insert at index
        '''

        self.arrList.insert(idx, ele)
        
        while idx != 0:
            if self.arrList[idx] < self.arrList[self.parent(idx)] :
                self.arrList[idx] , self.arrList[self.parent(idx)] = self.arrList[self.parent(idx)] , self.arrList[idx]

                idx = self.parent(idx)
            else:
                break
        
        

    def deleteKey(self, idx):
        self.decreaseKey(idx, float("inf"))
        self.extractMin()



if __name__ == '__main__':
    arrList = []
    minheap_obj = BinaryMinHeap(arrList)
    minheap_obj.insert(3)
    minheap_obj.insert(1)
    minheap_obj.insert(6)
    minheap_obj.insert(5)
    minheap_obj.insert(2)
    minheap_obj.insert(4)

    print(minheap_obj.extractMin())
    print(minheap_obj.extractMin())
    print(minheap_obj.extractMin())




