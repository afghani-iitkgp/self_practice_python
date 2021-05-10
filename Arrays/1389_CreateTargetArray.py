
from typing import List

def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
    target = []

    for i in range(0, len(nums)):
        if len(target) == index[i]:
            target.append(nums[i])
        elif len(target) > index[i] :
            for j in range(-1, index[i]-i-1, -1):
                # print(j)
                if j == -1:
                    target.append(target[j])
                else:
                    target[j] = target[j-1]
            print(j-1, "  ", i)
            target[j-1] = nums[i]
    
    return target
            

if __name__ == "__main__":
    nums = [0,1,2,3,4]
    index = [0,1,2,2,1]

    # nums = [1] 
    # index = [0]


    print(createTargetArray(nums, index))


