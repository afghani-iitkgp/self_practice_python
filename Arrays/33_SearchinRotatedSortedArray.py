from typing import List


def findPivot(arrList, l, r, n):
    mid = l + (r-l)//2

    if mid == l or mid == r:
        if arrList[mid] > arrList[(mid-1)%n] and arrList[mid] > arrList[(mid+1)%n]:
            return mid
        else:
            return -1
    
    # if mid == r:
    #     if arrList[mid] > arrList[(mid-1)%n] and arrList > arrList[(mid+1)%n]:
    #         return mid
    #     else:
    #         return -1

    
    if (arrList[mid] > arrList[mid-1]) and (arrList[mid] > arrList[mid+1]) :
        return mid
    
    # if (arrList[mid] < arrList[(mid-1)%n]) and (arrList[mid] < arrList[(mid+1)%n]) :
    #     return mid
    
    left_i = findPivot(arrList, l, mid-1, n)

    if left_i == -1:
        right_i = findPivot(arrList, mid+1, r, n)
        return right_i
    else:
        return left_i



def search_target_recursion (nums, si, ei, target):
      

    if si==ei:
        return -1

    mi = si + (ei-si)//2  

    
    if nums[mi] == target:
        return mi
    
    elif target > nums[mi]:
        search_target_recursion(nums, mi+1, ei, target)
    elif target < nums[mi]:
        search_target_recursion(nums, si, mi-1, target)

 
            


def search_target(nums: List[int], target: int) -> int:
    si = ( findPivot(nums, 0, len(nums)-1, n) + 1 ) % n 
    ei = ( findPivot(nums, 0, len(nums)-1, n) ) % n


    print( search_target_recursion (nums, si, ei, target) )




if __name__ == "__main__":
    # nums = [4,5,6,7,0,1,2]
    nums = [0,1,2,4,5,6,7]
    # # nums = [4,5,6,7,8,9,11,12,14,15,0,1,2]
    # nums = [7,8,9,11,12,14,15,0,1,2,4,5,6,]
    n = len(nums)
    target = 0

    # print( findPivot(nums, 0, len(nums)-1, n) )
    
    print(search_target(nums, target))