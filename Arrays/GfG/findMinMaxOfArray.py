import sys

def getMin(arr: list, n: int) -> int :

    Min = 2**63-1
    
    for i in range(n):
        if arr[i] < Min:
            Min = arr[i]
    
    return Min


def getMinRec(arr: list, n: int) -> int:

    if n==1:
        return arr[0]
    


    # if arr[n-1] > getMinRec(arr, n-1):
    #     Min = getMinRec(arr, n-1)
    # else:
    #     Min = arr[n-1]

    Min = getMinRec(arr[1:], n-1) 

    if arr[0] > Min:
        return Min
    else:
        return arr[0]


def getMaxRec(arr, n) -> int:
    if n==1:
        return arr[0]

    Max = getMaxRec(arr[1:], n-1)

    if arr[0] > Max:
        return arr[0]
    else:
        return Max


def getMax(arr: list, n: int) -> int :
    Max = -2**63+1

    for i in range(n):
        if arr[i] > Max:
            Max = arr[i]
    
    return Max


def getMinRec2(arr: list):
    if len(arr)==1:
        return arr[0]

    
    return min(arr[0], getMinRec2(arr[1:]))


if __name__ == "__main__":
    # Driver Program
    arr = [12, 1234, 45, 67, 1]
    n = len(arr)
    print ("Minimum element of array:", getMin(arr, n))
    print ("Maximum element of array:", getMax(arr, n))

    print("Recursion Min = ", getMinRec(arr, n))
    print("Recursion Min = ", getMaxRec(arr, n))
    print("Recursion Min = ", getMinRec2(arr))