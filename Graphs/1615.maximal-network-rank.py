

def maximal_network_rank(n, roads):

    adj = [[] for _ in range(n)]

    for i in roads:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])

    print(adj)


    # calculate degrees of each node
    




if __name__ == "__main__":
    n = 5
    roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]

    maximal_network_rank(n, roads)