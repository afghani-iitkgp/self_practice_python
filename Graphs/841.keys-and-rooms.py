def bfs_find_keys(adjlist):
    n = len(adjlist)
    s = 0
    que = [s]
    visited = [False] * n
    visited[s] = True

    while  len(que) > 0:
        u = que[0]
        que.pop(0)

        for v in adjlist[u]:
            if visited[v]==False:
                visited[v] = True
                que.append(v)

    if False in visited:
        return False
    else:
        return True






if __name__ == "__main__":
    #adjlist= [[1,3],[3,0,1],[2],[0]]
    adjlist= [[0],[0]]

    print(bfs_find_keys(adjlist))
