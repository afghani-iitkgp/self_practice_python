from collections import deque

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)





# Driver Code
if __name__ == "__main__":
    V = 4
    adj = [[] for i in range(V)]
    add_edge(adj, 0, 1)
    add_edge(adj, 1, 2)
    add_edge(adj, 2, 0)
    add_edge(adj, 2, 3)

    print(detect_cycle(adj, V))
 
    # if detect_cycle(adj, V):
    #     print("Yes")
    # else:
    #     print("No")