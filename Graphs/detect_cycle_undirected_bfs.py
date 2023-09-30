'''
Detect cycle in an undirected graph using BFS.
We do BFS traversal of the given graph. For every visited vertex 'v', if there is an adjacent 'u' such that 'u' is already visited 
and 'u' is not parent of 'v', then there is a cycle in the graph. If we don't find such an adjacent for any vertex, we say that there is no cycle.
The assumption of this approach is that there are no parallel edges between any tow vertices.

'''

from collections import deque

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


def BFS_traversal_for_cycle_detection(adj, s, V, visited):
    parent = [-1] * V

    q = deque()

    visited[s] = True
    q.append(s)
    ll =[[]]


    while len(q) > 0:
        u = q.pop()

        for v in adj[u]:
            if visited[v]==False:
                visited[v] = True
                q.append(v)
                parent[v] = u

            elif parent[u] != v:
                #print([v, u])
                pass

                #return True

    return ll



def detect_cycle(adj, V):
    visited = [False] * V

    for i in range(V):
        if visited[i]==False:
            x = BFS_traversal_for_cycle_detection(adj, i, V, visited)
            if x:
                return x
    
    return False

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