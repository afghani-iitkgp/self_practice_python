from typing import List

class Node:
    def __init__(self):
        self.status = False
        self.val = -1


def recursion_dfs(adjList, s, visited, rec_stack, cycle):
    
    x = Node()
    visited[s] = True
    rec_stack[s] = True    

    for v in adjList[s]:
        if visited[v] == False:
            # visited[v] = True
            # rec_stack[v] = True
            x = recursion_dfs(adjList, v, visited, rec_stack, cycle)
            if x.status == True:
                cycle.append(s)
                if x.val == s:
                    # x.status = False
                    x = Node()
                    return x

            rec_stack[v] = False
            # return x

        elif rec_stack[v] == True:
            cycle.append(s)
            x.status = True
            x.val = v
            return x

    rec_stack[s] = False
    return x



def recursion_dfs2(adjList, s, visited, rec_stack, cycle):

    x = Node()
    visited[s] = True
    rec_stack[s] = True

    for v in adjList[s]:
        if visited[v]==False:
            x = recursion_dfs2(adjList, v, visited, rec_stack, cycle)

            if x.status == True:
                cycle.add(s)
                if x.val == v:  # If all vertices in cycle are captured then backtrack with appending
                    x.status = False
                    x.val = -1
                
                return x    # Backtrack once cycle is found 

        elif rec_stack[v] == True: 
            cycle.add(s)
            x.status = True
            x.val = v
            return x 
    
    rec_stack[s] = False    # Remove 's' from recursion stack once it is visited completely.

    return x

def add_edge(adjList, u, v):
    adjList[u].append(v)



def eventual_safe_nodes(adjList):
    V = len(graph)
    vertices = []
    visited = [False] * V
    cycle = set()

    adjList = [[] for _ in range(V)]

    for i, v_list in enumerate(graph):
        for j in v_list:
            if i==j:
                cycle.add(i)
                graph[i].remove(i)
    print(graph)

    for i, v_list in enumerate(graph):
        vertices.append(i)
        for j in v_list:
            if i==j:
                cycle.add(i)
            else:
                add_edge(adjList, i, j)

    print(adjList)



    for s in range(V):
        if visited[s] == False:
            # recursion_dfs(adjList, s, visited, rec_stack, cycle)
            rec_stack = [False] * V
            recursion_dfs2(adjList, s, visited, rec_stack, cycle)

    print(cycle)


    not_cycle = [i for i in range(V) if i not in cycle]
    return not_cycle


if __name__ == "__main__":
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]

    # graph = [[1,2], [2,3], [3], [4], [5,6], [0,6], [7,8], [], []]
    graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    # graph = [[1, 2], [2, 3], [5], [0], [1, 5], []]
    graph = [[0],[2,3,4],[3,4],[0,4],[]]
 
    
    print(eventual_safe_nodes(graph))