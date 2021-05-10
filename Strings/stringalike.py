
def halvesAreAlike(s: str) -> bool:
    if len(s)%2 != 0:
        print("Inval")
        return None
    
    N = int(len(s)/2)

    cnt1 = 0 
    for i in range(N):
        if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            cnt1 += 1

    cnt2 = 0
    for i in range(N, 2*N):
        if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            cnt2 += 1



    return cnt1 == cnt2
    
    
    





if __name__ == "__main__":
    s = "fookAp"
    print(halvesAreAlike(s))

