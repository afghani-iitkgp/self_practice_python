def powerSetIter(s, n):
    combination = []
    for t in range(1, n):
        for i in range(0, n-t):
            for j in range(i+t, n):
                ch = s[i: i+t] + s[j]
                print(ch)
                combination.append(ch)

    return len(combination)

    
    
def powerSetRecursion(s):
    if len(s) == 1:
        lst = [s]
        return lst 
    
    lst = powerSetRecursion(s[1:])
    n = len(lst)
    for i in range(n):
        lst.append( s[0] + lst[i] )
    
    lst.append(s[0])
    return lst


def inclusion_exclusion(s):
    if len(s) == 0:
        return " "

    n = len(s)
    lst = []
    for i in range(n-1):
        a = inclusion_exclusion( s[:i] + s[i+1:] ) # Excluding ith charachter
        b = inclusion_exclusion( s[:] )  # Including ith character
        lst.append(a)
        lst.append(b)
    
    return lst

def inclusion_exclusion2(s, curr, i):
    if i==len(s):
        print(curr, end=",")
        return
    
    inclusion_exclusion2(s, curr, i+1)
    inclusion_exclusion2(s, curr+s[i], i+1)


def inclusion_exclusion3(s, i, N, lst):

    if i==N:
        print(s)
        lst.append(s)
        return lst



    lst = inclusion_exclusion3(s[:i]+s[i+1:], i+1, N, lst)

    lst = inclusion_exclusion3(s, i+1, N, lst)
        
    return lst 


if __name__ == "__main__":
    n = 9
    p = 9
    s = "abc"
    N = len(s)
    # lst = powerSetRecursion(s)
    # lst.append(" ")
    # print(len(lst))
    # print(lst)
    # print(inclusion_exclusion(s))
    # print(inclusion_exclusion2(s, "", 0))

    lst = []

    print(inclusion_exclusion3(s, 0, N, lst))