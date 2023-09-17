from typing import List

def checkPair(arr: List, target: int) -> bool:

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

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    arr = [1, 4, 45, 6, 10, -8]
    x = -2

    print(checkPair(arr, x))