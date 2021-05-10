class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.begin_iter = 0
        self.nums = nums



    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        if self.nums[self.begin_iter + 1]:
        	self.begin_iter += 1
        	return True
        else:
        	return False


    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        if self.nums[self.begin_iter + 1]:
        	self.begin_iter += 1
        	return self.nums[self.begin_iter]
        else:
        	raise IndexError



class PeekingIterator(Iterator):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        super.__init__()


        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return super.nums[super.begin_iter + 2]

        

    def next(self):
        """
        :rtype: int
        """
        super.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        super.hasNext()



if __name__ == "__main__":
    nums = [1,2,3,4,5]
    iter = PeekingIterator(Iterator(nums))