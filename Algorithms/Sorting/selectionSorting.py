def minList(lst):
    if len(lst) ==1:
        return lst[0]
        
    return min( lst[0], lst[1:] )


def IndexOfMinimumElement(lst):
    index = 0
    n = len(lst)
    for i in range(1, n):
        if lst[index] > lst[i]:
            index, i = i, index 
        else:
            continue
    return lst[index], index


def selectionSort(arr:list)->list:
    n = len(arr)

    for i in range(n-1):
        Min, minIndex = IndexOfMinimumElement(arr[i+1:])
        minIndex += i + 1 
        if arr[i] > Min:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        else:
            continue

    return arr


def insertionSortIterative(arr:  list) -> list :
    n = len(arr)
    # sortedArr = [arr[0]]
    # sortedArr = []
    for i in range(0, n):
        # key = arr[i]
        # sortedArr.append(key)
        # len_sortedArr = len(sortedArr)
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                # arr[j+1] = arr[j]
                # arr[j] = key
                arr[j+1], arr[j] = arr[j], arr[j+1]
    
    return arr


def mergeArr(l_arr, r_arr):
    i = 0
    j = 0
    sortedArr = []
    while (i < len(l_arr) and j < len(r_arr) ) :
        if l_arr[i] < r_arr[j] :
            sortedArr.append(l_arr[i])
            i += 1
        elif l_arr[i] > r_arr[j] :
            sortedArr.append(r_arr[j])
            j += 1
        else:
            sortedArr.append(l_arr[i])
            sortedArr.append(r_arr[j])
            i += 1
            j += 1
    
    if i < len(l_arr):
        sortedArr.extend(l_arr[i : ])
    if j < len(r_arr):
        sortedArr.extend(r_arr[j:])

    return sortedArr





def mergeSort(arr, mid, sortedArr):
    n = len(arr)
    mid = int(n/2)
    sortedArr = []

    if n==1:
        return arr   

    l_arr = mergeSort( arr[ :  mid], mid, sortedArr)
    r_arr = mergeSort( arr[mid : ], mid, sortedArr)
    sortedArr = mergeArr(l_arr, r_arr)
    
    return sortedArr

    




if __name__ == "__main__":
    arr = [8, 4, 1, 9, 5, 12, 3, 3, 10]
    # print(arr)
    # selectionSort(arr)
    # print(IndexOfMinimumElement(arr))


    # print(insertionSortIterative([12, 11, 13, 5, 6] ))
    # arr = [38, 47, 27, 43, 3, 9, 82, 10]
    print(arr)
    print(mergeSort(arr, 0 , []))

