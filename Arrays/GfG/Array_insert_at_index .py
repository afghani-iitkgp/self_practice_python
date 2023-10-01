def updateArray (arr, n ,idx, ele):
    if idx == n+1:
        arr.append(ele)
        return arr
    elif idx < n:
        arr.append(0)
    
    i = 0
    for i in range(-1 , idx-1-n, -1):
        arr[i] = arr[i-1]
    arr[i-1] = ele

    return arr

if __name__ == "__main__":
    # tcs = int(input())

    # for _ in range(tcs):
    #     n = int(input())
    #     idx, ele = [int(x) for x in input().split()]

    #     arr = [i+1 for i in range(n)]

    #     updateArray(arr, n, idx, ele)

    #     print(arr[idx])

    n = int(input())
    idx, ele = [int(x) for x in input().split()]

    arr = [i+1 for i in range(n)]

    updateArray(arr, n, idx, ele)

    print(arr[idx])