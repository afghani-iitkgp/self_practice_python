# The program creates a binary max-heap and presents a menu to the user to perform various operations on it.

class BinaryHeap:
    
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2
    
    def get(self, i):
        return self.items[i]

    def get_max(self):
        if self.size == 0:
            return None
        
        return self.items[0]
    
    def extract_max(self):
        if self.size() == 0:
            return None
        largest = self.get_max()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify(0)

        return largest
    
    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        if (l <= self.size() - 1 and self.get(l) > self.get(i) ):
            largest = l
        else:
            largest = i
        
        if (r <= self.size() - 1 and self.get(r) > self.get(largest)):
            largest = r 
        if (largest != i):
            self.swap(largest, i)
            self.max_heapify(largest)

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]
    

    def insert(self, key):
        index = self.size()
        self.items.append(key)

        while (index != 0):
            p = self.parent(index)
            
            if self.get(p) < self.get(index):
                self.swap(p, index)
            
            index = p



if __name__ == "__main__":
    bheap_obj = BinaryHeap()
    print("Menu")
    print("insert <data>")
    print("max get")
    print("max extract")
    print("Quit")


    while True:
        
        do = input("What you would like to do ?").split()

        operartion = do[0].lower()

        if operartion == "insert":
            data = int(do[1])
            bheap_obj.insert(data)
        
        elif operartion == "max":
            suboperation = do[1].strip().lower()
            if suboperation == "get":
                print("Maximum value: {}".format(bheap_obj.get_max()))
            elif suboperation == "extract":
                print("Maximum value removed: {}".format(bheap_obj.extract_max()))
        elif operartion == "quit":
            break

