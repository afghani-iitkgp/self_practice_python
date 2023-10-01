
def minSwapPalindrome(s : str):
    s_list = list(s)
    n = len(s_list)
    l = 0
    r = n-1

    unmap = {}
    odd = 0

    for c in s:
        if c in unmap.keys():
            unmap[c] += 1
        else:
            unmap[c] = 1
    
    for k, v in unmap.items():
        if v % 2 > 0:
            odd += 1

    if odd > 1:
        return False
    
    count = 0
    while l < r:
        k = r
        while s_list[l] != s_list[r]:        
            k -= 1
            continue
        if l==r:
            s_list[k], s_list[k+1] = s_list[k+1], s_list[k]
            count += 1
            continue
        else:
            while k < r:
                s_list[k], s_list[k+1] = s_list[k+1], s_list[k]
                k += 1
                count += 1
        
        l += 1
        r -= 1
        print(''.join(s_list))
    
    return count



def minSwap(s):
    strng = list(s)
    unmp = {}
    for i in strng:
        unmp[i] = unmp.get(i,0)+1
    odd = 0
    result = 0
    left = 0
    right = len(strng)-1
    for i in unmp:
        if unmp[i]%2 != 0:
            odd += 1
    # If we found more than one odd number
    if odd > 1:
        return -1
    while left < right:
        l = left
        r = right
        while strng[l] != strng[r]:
            r -= 1
        if l == r:
            # When we found odd element move towards middle
            strng[r],strng[r+1] = strng[r+1],strng[r]
            result += 1
            continue
        else:
            # Normal element  move towards right of string
            while r < right:
                strng[r],strng[r+1] = strng[r+1],strng[r]
                r += 1
                result += 1
        left += 1
        right -= 1
    print(strng)
    return result






if __name__ == "__main__":
    s = "abcdabd"
    # print(minSwapPalindrome(s))
    print(minSwap(s))