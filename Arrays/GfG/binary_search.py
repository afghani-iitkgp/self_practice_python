from typing import List

def binarySearch(A: List[int], li: int, ri: int, x: int) -> int :
    if li==ri:
        return -1
    
    mi = (li + ri) // 2

    if ( x == A[mi] ):
        return mi
    elif ( x < A[mi] ) :
        return binarySearch(A, li, mi-1, x)
    elif ( x > A[mi] ):
        return binarySearch(A, mi+1, ri, x)




if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    x = 11
    n = len(arr)
    print( binarySearch(arr, 0, n-1, x) )