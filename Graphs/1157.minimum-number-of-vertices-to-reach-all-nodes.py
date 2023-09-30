
def find_smallest_set(n, edges):
    src = []
    tar = []

    for e in edges:
        if not (e[0] in tar or e[0] in src):
            src.append(e[0])
        if e[1] not in tar:
            if e[1] in src:
                tar.append(e[1])
                src.remove(e[1])
            else:
                tar.append(e[1])
                
    return src

def find_smallest_set2(n, edges):
    indegree = [0]*n
    
    for e in edges:
        indegree[e[1]] += 1
    
    s = []
    for i in range(n):
        if indegree[i] == 0:
            s.append(i)
    
    return s



if __name__ == "__main__":
    n = 6
    edges = [[0,1],[2,1],[3,1],[1,4],[2,4], [5,3], [0,5]]

    # edges = [[0,1], [2,0]]

    print(find_smallest_set(n, edges))
    print(find_smallest_set2(n, edges))

