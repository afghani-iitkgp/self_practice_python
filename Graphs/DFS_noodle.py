
def dfs_recur(adjList, vertex, visited, parent):
    for i in adjList:
        if visited[i] == False:
            parent.append(i)
            dfs_recur(adjList, i, visited, parent)
    

def dfs(adjList):
    adjList = {}
    adjList["A"] = ["B"]
    adjList["B"] = ["D", "E"]
    
    V = len(adjList)
    visited = [False * V]
    s = "A" # starting node
    parent = ["A"]

    dfs_recur(adjList, s, visited, V, parent)

    return parent
    
