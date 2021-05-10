import time


def greedy_rope(n):
    # base condition:
    if n==2:
        return 2
    if n==3:
        return 3
    if n ==1:
        return 1
    

    Max = 0
    for i in range(2, n):
       
        k = greedy_rope(n-i)

        if Max < i*k:
            Max = i*k
    
    return Max


def greedy_rope_dp(n, dp_lst):
    # Base conditions
    if n==2 or n==3 or n==4:
        dp_lst.insert(n-1, n)
        return n
    
    Max = 0
    for i in range(2, n):
        if (dp_lst[n-1-i] == 0):
            k = greedy_rope_dp(n-1-i, dp_lst) 
        else:
            k = dp_lst[n-1-i]

        if Max < i*k:
            Max = i*k
    
    dp_lst.insert(n-1, Max)
    return Max


if __name__ == "__main__":

    n = 500
    dp_lst = [0] * n
        
    # start_t1 = time.time() 
    # print(greedy_rope(n))
    # print("Without DP--- %s seconds ---" % (time.time() - start_t1))
    
    start_t2 = time.time() 
    import sys
    print(sys.getrecursionlimit())
    print(greedy_rope_dp(n, dp_lst))
    print(dp_lst[n-1])
    print("Using DP--- %s seconds ---" % (time.time() - start_t2))
