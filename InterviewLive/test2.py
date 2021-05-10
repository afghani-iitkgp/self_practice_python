A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]


def monotonic(lst):
    if lst[0] > lst[1]:
        #decreasing 
        for i in range(1, len(lst)-1):
            if lst[i] >= lst[i+1]:
                continue
            else:
                print(lst[i], lst[i+1])
                flag = 0
                return flag
        flag = 1
          
    elif lst[0] <= lst[1]: # Increasing
        for i in range(1, len(lst)-1):
            if lst[i] <= lst[i+1]:
                continue
            else:
                flag = 0
                return flag
                
        flag = 1

    return flag



def check_palin(s):
    l = len(s) 
    for i in range(l//2):
        if s[i] == s[l-i-1]:
            continue
        else:
            return False

    return True

def check_rem(s):
    if not check_palin(s):
        str_lst = list(s)
        for i in range(len(str_lst)):
            str_lst.pop(i)
            s1 = "".join(str_lst)
            t = check_palin(s1)
            if not t:
                continue
    
        return "Yes"
        

def c_(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]: return True

    return s == s[::-1]


if __name__ == "__main__":
    # A = [6, 5, 4, 4] 
    # B = [1,1,1,3,3,4,3,2,4,2]
    # C = [1,1,2,3,7]

    # D = [1,2,3,2]
    # print(monotonic(C))
    # print(check_palin("rrradarrr"))
    print(c_("radtar"))


# return s1 == s1[::-1]
