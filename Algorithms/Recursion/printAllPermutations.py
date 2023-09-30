def printWithoutLoop(n):
    # base case;
    if n==0:
        return 0

    print(n%10,  end='---')
    
def sumOfDigits(n):
    # base case;
    if n==0:
        return 0

    return n%10 + sumOfDigits(n//10)

def countDigits(n):
    # base case;
    if n==0:
        return 0

    return 1 + sumOfDigits(n//10)

def digitalRoot(n):
    # base cases:
    if n == 0:
        return 0       

    s = n%10 + digitalRoot(n//10)
    
    if s//10 == 0:
        return s
    else:
        return digitalRoot(s)

def powerRecursion(n, p): 
    if p==1:
        return n
    
    return n * powerRecursion(n, p-1)


if __name__ == "__main__":
    n = 45927653
    p = 2
    # print(printWithoutLoop(n))
    print( digitalRoot(n) )