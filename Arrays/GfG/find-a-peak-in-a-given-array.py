'''
Given an array arr of n elements that is first strictly increasing and then maybe strictly decreasing, find the 
maximum element in the array.

Note: If the array is increasing then just print the last element will be the maximum value.
'''

def findPeak(arr):
    n = len(arr)

    peak = []
    for i in range(1, n-1):
        if arr[i-1] < arr[i] and arr[i+1] < arr[i]:
            peak.append(arr[i])
    
    if len(peak) == 0:
        if arr[i] < arr[i+1] and  arr[i-1] < arr[i]:
            peak.append(arr[i+1])
        elif arr[0] > arr[1]:
            peak.append(arr[0])


    return peak


if __name__ == "__main__":
    arr = [5, 10, 20, 15]
    arr = [10, 20, 15, 2, 23, 90, 67]
    arr = [10, 20, 30, 40, 50]
    arr = [100, 80, 60, 50, 20]

    print(findPeak(arr))
