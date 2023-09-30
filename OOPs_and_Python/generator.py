
'''
Use the generator with a for loop
Behind the scene, the for loop is calling the generator's __next__() function.

Big advantages over List:
- generator can provide an infinite sequence
- generator doesn't load values into memory.

'''

def my_generator(x=1):
    while True:
        yield x
        x += 1


def first_n(n):
    '''Buod and return a list of '''
    num = 0
    nums = []

    while num < n:
        nums.append(num)
        num += 1
    
    return nums

# Using the generator pattern (an iterable)
class first_n:
    
    def __init__(self, n):
        self.n = n
        self.num = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()
    

    def next(self):
        if self.num < self.n:
            cur = self.num
            self.num += 1
            

        

if __name__ == "__main__":
    # my_generator()
    n = 1000000
    sum_of_first_n = sum(first_n(n))
    print(sum_of_first_n)