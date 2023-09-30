
from collections import defaultdict
from typing import List


def maximal_network_rank(n, roads):

    if len(roads)==0:
        return 0

    adj = [[] for _ in range(n)]

    for i in roads:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])

    # print(adj)

    deg = dict()
    for i in range(n):
        deg[i] = len(adj[i])
    # print(deg)

    #{k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
    sorted_deg = {k : v for k, v in sorted(deg.items(), key=lambda kv : kv[1], reverse=True)}
    print(sorted_deg)



    iter_obj = iter(sorted_deg)
    firstMaxKey = next(iter_obj)
    firstMaxVal = sorted_deg[firstMaxKey]
    secondMaxKey = next(iter_obj)
    secondMaxVal = sorted_deg[secondMaxKey]
    print("first key = {0} and second key = {1}".format(firstMaxKey, secondMaxKey))

    lst = []

    if secondMaxKey in adj[firstMaxKey]:
        lst.append([firstMaxKey, secondMaxKey, firstMaxVal+secondMaxVal-1])
    else:
        lst.append([firstMaxKey, secondMaxKey, firstMaxVal+secondMaxVal])

    while True:
        try:
            k = next(iter_obj)
            v = sorted_deg[k]

            if (v==secondMaxVal or v==secondMaxVal-1) and v>0:
                if k in adj[firstMaxKey]:
                    lst.append([firstMaxKey, k, firstMaxVal+v-1])
                else:
                    lst.append([firstMaxKey, k, firstMaxVal+v])
        except StopIteration:
            break
    

 
    t = defaultdict(list)
    for i in lst:
        t[i[-1]].append([i[0], i[1]])

    t = {k:v for k, v in sorted(t.items(), key=lambda x : x[0], reverse=True)}
    print(t)
        
    return next(iter(t))


def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
    if len(roads)==0:
        return 0

    adj = [[] for _ in range(n)]

    for i in roads:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])

    m = 0
    for i in range(n):
        x = len(adj[i])
        for j in range(i+1, n):
            y = len(adj[j])
            
            if i in adj[j]:
                z = 1
            else:
                z = 0
            
            m = max(m, (x + y - z))
    
    return m



if __name__ == "__main__":
    # n = 5
    # roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]

    # n = 8
    # roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]

    # n = 4
    # roads = [[0,1],[0,3],[1,2],[1,3]]

    # n = 2
    # roads = []

    n = 3
    roads = [[0,2], [1,2]]

    n = 5
    roads = [[2,3],[0,3],[0,4],[4,1]]

    print(maximal_network_rank(n, roads))
    print(maximalNetworkRank(n, roads))