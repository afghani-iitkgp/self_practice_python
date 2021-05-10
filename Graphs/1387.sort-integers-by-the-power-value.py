def getKth(lo, hi, k):
    
    dict_powers = {}
    lst_powers = []

    for i in range(lo, hi+1):
        p = power2(i) - 1
        # dict_powers[p] = i
        dict_powers[i] = p

        lst_powers.append(p)
    
    lst_powers.sort(reverse=False)
    # print(lst_powers)
    # ll = [v[0] for v in sorted(dict_powers.items(), key=lambda(k,v) : (v,k))]
    ll = [v[0] for v in sorted(dict_powers.items(), key=lambda kv : (kv[1],kv[0]) )]

    print(ll)
    val = lst_powers[k-1]
    print((dict_powers))
    print((lst_powers))
    # print(dict_powers[val])

    return ll[k-1]




def power(x, lst):
    if x == 1:
        return len(lst)
    
    if x%2==0:
        x /= 2
        x = int(x)
    else:
        x = 3 * x + 1
    lst.append(x)
    return power(x, lst)


def power2(x):
    # Base condition
    if x == 1:
        return 1
    
    if x%2==0:
        x /= 2
    else:
        x = 3 * x + 1

    return power2(x) + 1
    

if __name__ == "__main__":
    x = 12
    lst = []

    # print(power(x, lst))
    
    # print(power2(x)-1)

    lo = 1
    hi = 1000
    k = 777
    print(getKth(lo, hi, k))