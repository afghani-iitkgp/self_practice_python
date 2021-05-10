# MAX_CHAR = [26]  
  
# Returns minimum changes to str so  
# that no substring is repeated.  
def minChanges(s): 
  
    # n = len(str) 
  
    # # If length is more than maximum  
    # # allowed characters, we cannot  
    # # get the required string.  
    # # if (n > MAX_CHAR[0]):  
    # #     return -1
  
    # # Variable to store count of  
    # # distinct characters  
    # dist_count = 0
      
    # # To store counts of different  
    # # characters  
    # # count = [0] * MAX_CHAR[0]  
    # count = [0]* n
  
    # for i in range(n):  
    #     if (count[ord(str[i]) - ord('a')] == 0) : 
    #         dist_count += 1
    #     count[(ord(str[i]) - ord('a'))] += 1
      
    # # Answer is, n - number of distinct char  
    # print(count)
    # return (n - dist_count)  


    n = len(s)
    
    freq = 0
    cnt = [0] * n
    
    for i in range(n):
        if (cnt[ord(s[i]) - ord("a")] == 0):
            freq += 1
        cnt[(ord(s[i])) - ord("a")] += 1
    
    return (n - freq)
  
# Driver Code  
if __name__ == '__main__': 
    str = "abcab"
    print(minChanges(str)) 