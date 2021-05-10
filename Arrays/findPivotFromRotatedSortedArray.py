def findPivot(arr, n, li, ri):

    # base condition:
    if n==1: # There is only one element.
        return 0 
    # if arr[li] < arr[ri]: # No rotation is found.
    #     return li

    
    mi = li + (ri-li)//2

    # if ( (li==0) and (li==ri) ):
    #     return n-1
    # if ( (li==n-1) and (li==ri) ):
    #     return 0
    
    if ( (li==mi) and (li<ri) and (li==0)):
        if ( (arr[mi] > arr[mi+1]) and (arr[mi] > arr[(mi-1)%n]) ):
            return mi+1
    
    if ( (li==mi) and (li<ri) and (ri==n-1)):
        if ( (arr[ri] < arr[ri-1]) and (arr[ri] < arr[(ri+1)%n]) ):
            return (ri+1)%n # return 0
    

    if ( arr[mi] < arr[mi-1] ) and ( arr[mi] < arr[mi+1] ):
        return mi

    else:
        if (arr[mi] > arr[li]): # Goto right sub-tree
            return findPivot(arr, n, mi+1, ri)
        
        if arr[mi] < arr[li]: # Goto left-subtree
            return findPivot(arr, n, li, mi-1)

    
def findMin(arr, li, ri): 
    if li >= ri:
        return arr[li]
    
    mi = (li+ri) // 2

    if mi>0 and arr[mi] < arr[mi-1] :
        return arr[mi]
    if mi>0 and arr[mi] > arr[mi+1]:
        return arr[mi+1]

    if arr[mi] < arr[li] and mi > li :
        # Goto left
        return findMin(arr, li, mi-1)
    else:
        return findMin(arr, li, mi-1)
    



def findPivot2(A, li, ri):
    n = len(A)

    # Corner cases 0:
    if n==1:
        return 0
    if n== 0:
        return None 
    
    mi = (li+ri)//2

    
    # Corner cases 1:
    if A[mi] < A[ri] and A[mi] > A[li] : # Array is sorted already in ascending order
        return li    
    
    # Corner cases 2:
    if li == 0 and mi == 0 and ri==1:
        if A[mi] > A[mi+1] and A[mi] > A[(mi-1)%n] :
            return mi+1
        else:
            return mi

    
    # Corner cases 3:
    if li == mi and ri == n-1:
        if A[ri] < A[ri-1] and A[ri] < A[(ri+1)%n] :
            return n-1
        # else:
        #     return 0
    


    # Check inflection point condition for middle index:
    if A[mi] > A[mi+1] and A[mi] > A[mi-1]:
        return mi+1
    elif A[mi] < A[mi+1] and A[mi] < A[mi-1]:
        return mi

    # Recursive calls:
    if A[mi] < A[li] and mi > li: # Goto Left
        return findPivot2(A, li, mi-1)

    elif A[mi] > A[li] and mi > li: # Goto Right
        return findPivot2(A, mi+1, ri)  




if __name__ == "__main__":
    # arr = [3,4,5,6,7,1,2]
    arr = [11,12,3,4,5,6,7,8,9,10]
    # arr= [1,2,3,4,5]
    # arr= [ 5, 1, 2, 3, 4] 
    n = len(arr)
    # print(findPivot(arr,n, 0, n-1))

    # print(findMin(arr, 0, n-1))
    # arr = [2,3,4,5,1]
    # arr = [1,2]
    # arr = [279,284,285,287,288,296,2,8,10,11,12,13,14,19,20,22,25,26,27,28,29,33,37,39,42,43,47,48,49,50,57,62,63,66,68,69,71,73,74,77,78,79,85,89,92,94,99,111,113,117,120,122,125,134,145,152,155,157,160,161,167,168,181,182,188,189,190,194,199,201,204,208,213,220,223,225,226,227,231,237,240,242,247,254,259,260,261,264,267,271,275]
    arr = [2,3,4,5,1]
    i = findPivot2(arr, 0, len(arr)-1)
    print(i)

