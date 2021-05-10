
def reverseList(A: list, startIndex: int, endIndex : int )-> list:

    midIndex = int(endIndex / 2)
    i = 0

    while( i <= midIndex):
        if endIndex % 2 == 1:
            # Number of elements is even.
            temp = A[midIndex - i]
            A[midIndex - i] = A[midIndex + 1 + i]
            A[midIndex + 1 + i] = temp
            i += 1


        elif endIndex % 2 == 0:
            # Number of elements is odd.
            temp = A[midIndex - i]
            A[midIndex - i] = A[midIndex + i]
            A[midIndex + i] = temp
            i += 1

    return A

def reverseListRec(A, i, j)->int:
    if i > j:
        return 0
    
    A[j], A[i] = A[i], A[j]
    print(A)
    i += 1
    j -= 1
    reverseListRec(A, i, j)
    



if __name__ == "__main__":
    # Driver function to test above function
    A = [1, 2, 3, 4, 5]
    print(A)
    #reverseList(A, 0, 5)
    reverseListRec(A, 0, 4)
    print("Reversed list is")
    print(A)