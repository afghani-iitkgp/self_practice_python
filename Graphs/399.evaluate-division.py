from typing import List
import collections


def DFS_find(src, dest, adj, visited):

    t = -1.0

    for u in adj[src]:
        if u[0] not in visited:
            visited.add(u[0])

            if u[0] != dest:
                t = DFS_find(u[0], dest, adj, visited)
                
                if t != -1.0:
                    return t * u[1]
                

            elif u[0] == dest:
                return u[1]
    
    return -1.0






def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    
    adj = collections.defaultdict(list)
    vertices = set()

    # Create adjacency list:
    for i, j in zip(equations, values):
        adj[i[0]].append([i[1], j])
        adj[i[1]].append([i[0], 1.0/j])

        vertices.add(i[0])
        vertices.add(i[1])
    
    # print(adj)
    print(vertices)

    res = []

    for q in queries:
        visited = set()

        visited.add(q[0])

        if (q[0] not in vertices) or (q[1] not in vertices) :
            c = -1.0
        elif q[0] == q[1]:
            c = 1.0
        else:       
            c = DFS_find(q[0], q[1], adj, visited)
        
        res.append(c)
    
    return res


  


if __name__ == "__main__":
    """
    Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    Explanation: 
    Given: a / b = 2.0, b / c = 3.0
    queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
    return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
    """
    
    
    equations = [["a","b"], ["b","c"], ["b", "d"], ["b", "e"], ["c", "f"], ["f", "g"], ["e", "h"], ["e", "i"]]
    values = [2.0, 3.0, 4.0, 3.0, 5.0, 4.0, 6.0, 8.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["d","h"]]
    # queries = [["d","h"]]



    # equations = [["a","b"],["b","c"],["bc","cd"]]; values = [1.5,2.5,5.0]; queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

    equations = [["a","b"],["c","d"]]
    values = [1.0,1.0]
    queries = [["a","c"],["b","d"],["b","a"],["d","c"]]

    x = calcEquation(equations, values, queries)
    print(x)
