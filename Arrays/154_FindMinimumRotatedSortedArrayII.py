from typing import List


def findMin_II(nums: List[int]) -> int:
    n = len(nums)
    i = 0

    while i < n:
        if nums[i%n] <= nums[(i+1)%n]:
            pass
        else:
            break

        i += 1

    return nums[(i+1)%n]

if __name__ == "__main__":
    # nums = [4,4,5,5,6,7,8]
    nums = [2,2,2,0,1]
    # nums = [3,5,1]
    print(findMin_II(nums))