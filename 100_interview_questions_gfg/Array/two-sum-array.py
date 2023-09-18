from typing import List

def checkPair_hashmap(arr: List, target: int) -> bool:

    arr_map: dict = {}

    # for k in arr:
    #     arr_map[k] = None

    for i in range(len(arr)):
        if arr[i] in arr_map.keys():
            print(arr[i], '+', arr_map[arr[i]], '=', target)
            return True
        else:
            arr_map[target - arr[i]] = arr[i]

    return False


def checkPair_twopointer(arr, target):
    arr.sort(reverse=False)

    l = 0 
    r = len(arr) - 1

    while l < r:
        if arr[l] + arr[r] == target:
            print(arr[l], '+', arr[r], '=', target)
            return True
        elif arr[l] + arr[r] < target:
            l += 1
        elif arr[l] + arr[r] > target:
            r -= 1

    return False
    
    
if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    arr = [1, 4, 45, 6, 10, -8]
    x = 16

    # print(checkPair_hashmap(arr, x))
    print(checkPair_twopointer(arr, x))