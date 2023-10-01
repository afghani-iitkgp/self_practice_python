
def all_paths_from_src_to_dest(graph):
    dest = len(graph) - 1
    lst = [0]
    path = []
    dfs_backtracking(graph, 0, dest, lst, path)
    return path

def dfs_backtracking(graph, s, dest, lst, path):
    # base condition:
    if s == dest:
        path.append(lst.copy())
        print("lst = ", lst)
        print(path)
    
    for i in graph[s]:
        lst.append(i)
        # print(lst)
        dfs_backtracking(graph, i, dest, lst, path)
        lst.pop()
    

if __name__ == "__main__":

    # graph = [[1,3,4],[2,3,4],[3],[4],[]]
    graph = [[1,3],[2],[3],[]]
    print(all_paths_from_src_to_dest(graph))
