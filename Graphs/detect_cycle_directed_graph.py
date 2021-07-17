from collections import deque

class node:
    def __init__(self) -> None:
        self.status = False
        self.val = -1


def add_edge(adj, u, v):
    adj[u].append(v)


def DFS_backtracking(adj, visited, rec_stack, s, cycle):

    x = node()

    for v in adj[s]:
        if visited[v] == False:
            visited[v] = True
            rec_stack[v] = True

            x = DFS_backtracking(adj, visited, rec_stack, v, cycle)

            if x.status == True:
                cycle.append(s)
                if x.val == s:
                    x.status = False
                rec_stack[v] = False
                return x

        elif rec_stack[v] == True:
            x = node()
            cycle.append(s)
            x.status = True
            x.val = v
            
            return x

    rec_stack[s] = False
    return x


def detect_cycle_dfs(adj, V):
    visited = [False] * V
    rec_stack = [False] * V
    cycle = []

    for s in range(V):
        if visited[s]==False:
            visited[s] = True
            rec_stack[s] = True
            DFS_backtracking(adj, visited, rec_stack, s, cycle)

    print(cycle)
    return cycle
 


# Driver Code
if __name__ == "__main__":
    # V = 7
    # adj = [[] for i in range(V)]
    # add_edge(adj, 0, 1)
    # add_edge(adj, 2, 1)
    # add_edge(adj, 2, 3)
    # add_edge(adj, 3, 4)
    # add_edge(adj, 4, 5)
    # add_edge(adj, 4, 6)
    # add_edge(adj, 5, 3)
    # # add_edge(adj, 3, 4)


    # graph = [[0, 1], [0, 6], [1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [6, 7], [7, 5]]
    graph = [[0, 1], [0, 4], [1, 2], [2, 3], [3, 4],[4, 3]]
    V = 5
    
    adj = [[] for i in range(V)]

    for e in graph:
        add_edge(adj, e[0], e[1])


    print(detect_cycle_dfs(adj, V))
 
    # if detect_cycle(adj, V):
    #     print("Yes")
    # else: