
def find_town_judge(N, trust):
    if N ==1 and len(trust)==1:
        return -1
    if N==1 and len(trust)==0:
        return 1
    
    count = [0] * N

    for i in trust:
        count[ i[0] - 1] -= 1
        count[ i[1] -1 ] += 1
    # print(count)
    for j in range(N):
        if count[j]==N-1:
            return j+1
        else:
            continue
    
    return -1



if __name__ == "__main__":
    # N = 4 
    # trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

    N = 1; trust = []

    print(find_town_judge(N, trust))