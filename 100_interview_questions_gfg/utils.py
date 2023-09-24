from typing import List


def insertion_sort(arr: List) -> List:
    n = len(arr)

    sort_arr = [arr[0]]

    for i in range(1, n):
        sort_arr.append(arr[i])
        for j in range(len(sort_arr)-1, 0, -1):
            if sort_arr[j] < sort_arr[j-1]:
                temp = sort_arr[j]
                sort_arr[j] = sort_arr[j-1]
                sort_arr[j-1] = temp
    
    return sort_arr



if __name__ == "__main__":

    lst = [9,4,6,7,1,3,4,10]    
    lst = [5, 3, 16, 6, 12, 11, 4, 2, 8]
    print(lst)
    print(insertion_sort(lst))
    