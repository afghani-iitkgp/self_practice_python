
def next_greater_elements(A):

    n = len(A)  # Calculate length of Array 
    B = []      # Output array. 

    if n==1:
        B.append(-1)

    for i in range(n): # Iterating over array 0 to n-1
        for j in range(i+1, i+n, 1):  # iterating entire array circularly for finding next greater element. 
            if A[i] < A[j%n]:
                B.append(A[j%n])
                break

            elif j==i+n-1:
                B.append(-1)
    
    return B










if __name__ == "__main__":
    # nums = [1,2,3,4,3]
    nums = [1]

    greater_arr = next_greater_elements(nums)

    print(greater_arr)

