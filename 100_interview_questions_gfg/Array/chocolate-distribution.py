from ..utils import insertion_sort

def findMinDiff(nums, m):
    nums = insertion_sort(nums)
    n = len(nums)

    min_diff = nums[-1] - nums[0]
    for i in range(0, n-m+1):
        min_diff = min(min_diff, nums[i+m-1] - nums[i])
        
    return min_diff



if __name__ == "__main__":
    nums = [7, 3, 2, 4, 9, 12, 56]
    m = 3
    nums = [3, 4, 1, 9, 56, 7, 9, 12]
    m = 5

    nums = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
    m = 7
    print(findMinDiff(nums, m))