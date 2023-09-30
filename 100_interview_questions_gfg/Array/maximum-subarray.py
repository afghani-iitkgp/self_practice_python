
def add_elements(arr):
    s = 0
    for i in arr:
        s += i

    return s

def maxSubArray_BruteForce(nums):
    global_sum = 0
    n = len(nums)

    for i in range(0, n-1):
        s_temp = nums[i]
        for j in range(i+1, n):
            s_temp += nums[j]
            global_sum = s_temp if s_temp > global_sum else global_sum
     

    return global_sum



def maxSubArraySum_optimized(nums):
    temp_sum = 0
    global_sum = 0
    n = len(nums)
    
    for i in range(n):
        if temp_sum + nums[i] <= 0:
            temp_sum = 0
            continue
        else:
            temp_sum += nums[i]
        
        global_sum = global_sum if global_sum > temp_sum else temp_sum
    
    return global_sum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [5,4,-1,7,8]
    # nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(maxSubArray_BruteForce(nums))
    print(maxSubArraySum_optimized(nums))
