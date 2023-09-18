from typing import List


def insertion_sort(arr: List) -> List:
    size = len(arr)

    def append_to_sorted_array(sorted_arr, n, t):
        
        if sorted_arr[n-1] > t:
            temp_t = sorted_arr[n]
            sorted_arr[n-1] = t
            sorted_arr.append(temp_t)
        else:
            sorted_arr.append(t)
        
        return sorted_arr

    for i in range(1, size):
        sorted_arr = append_to_sorted_array(arr[ : i], i, arr[i])

    print(sorted_arr)


lst = [9,4,6,7,1,3,4,10]

insertion_sort(lst)
    