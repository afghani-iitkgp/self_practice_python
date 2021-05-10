from typing import List

def findMin(nums: List[int]) -> int:
    n = len(nums)
    if n>1:
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1] and i+2 != len(nums):
                continue
            elif nums[i] < nums[i+1] and i+2 == len(nums):
                return nums[0]
            else:
                return nums[i+1]
    elif n==1:
        return nums[0]
    else:
        return None


if __name__ == "__main__":
    nums = []

    print( findMin(nums) )