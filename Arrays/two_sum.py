def two_sum(A, tar):
    B = {}
    n = len(A)

    for i in range(0,n):
        B[A[i]] = tar - A[i]

    print(B)
    for k, v in B.items():
        if v in B and k!=v:
            return [A.index(k), A.index(v)]
            # print(A.index(k), " and ", A.index(v))
            # return [i for i in range(n) if A[i] == k or A[i] == v]
    
    return A.index(k), A.index(v)


if __name__ == "__main__":
    A = [3, 3]
    tar = 6
    res = two_sum(A, tar)
    # print(type(res))
    print(res)
    # print (res[0])
    # print (res[1])