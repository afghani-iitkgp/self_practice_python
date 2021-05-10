
def sumSummation(lst):
    if len(lst)==1:

        return lst[0]
    
    lst2=[]
    
    for i in range(1, len(lst)):
        if i == 1:
            lst2.append(lst[i])
        else:
            lst2.append(lst[i] + lst2[-1])
    
    return sumSummation(lst2)
            
    


if __name__ == "__main__":
    lst = []
    lst = [1,3]
    for i in range(pow(10,8)):
        if i in [0,1]:
            pass
        else:
            lst.append(lst[-1] + lst[-2])

    # print(sumSummation(lst)%1000000007)

    print(lst[-1]%1000000007)