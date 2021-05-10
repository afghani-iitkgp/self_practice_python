from typing import List

def countPermutations(lstDigit: List) -> int :
   
    # base condition 1:
    if len(lstDigit) == 1:
        return 1
    
    # base condition 2:
    if len(lstDigit) == 2:
        num = ''.join(lstDigit)

        if int(num) <= 26 :
            return 2
        else:
            return 0

    
    t = ''.join( lstDigit[:2] )
    c1 = 1
    c2 = 1

    if int(t) <= 26 :
        c2 *= countPermutations( lstDigit[2:] )
    else:
        c2 = 0

    c1 *= countPermutations( lstDigit[1:] )

    return c1 + c2
    
    

      


if __name__ == "__main__":
    alpha_mapping = dict()

    for i in range(0, 26):
        alpha_mapping[chr(i+65)] = i+1

    # for k, v in alpha_mapping.items():
    #     print(k," : ", v)

    # s = 2112212
    s = 1117
    lstDigit = [d for d in str(s)]
    # n = len(lstDigit)

    print( countPermutations(lstDigit) )