from collections import defaultdict





def Result(w, path, indices):  # given w is a vertex in a cycle, find the edge with the largest index in this cycle
    prev, curr = w, path[w]
    M = indices[(curr, prev)]
    while curr != w:
        prev, curr = curr, path[curr]
        M = max(M,indices[(curr, prev)])

    return M

def DFS(v, e, path, indices):
    for w in e[v]:
        if path[v] == w:  # if predecessor of v is w, it's bad
            continue

        if path[w] != 0:  # the cycle is found
            path[w] = v   # complete the cycle
            return Result(w, path, indices)

        path[w] = v
        temp = DFS(w, e, path, indices)
        if temp:          # in case it is a dead end and returns nothing
            return temp
        path[w] = 0


def main(edges):
    e = defaultdict(set)  # e[x] is the set of all vertices adjacent to x
    indices = {}                      # key is edge, value is indices in the list 'edges'
    for i,p in enumerate(edges):
        if p[1] in e[p[0]]:
            return p                  # if one edge appears twice in 'edges', return tha latter one
        e[p[0]].add(p[1])
        e[p[1]].add(p[0])
        indices[(p[0],p[1])] = indices[(p[1],p[0])] = i

    path = {x:0 for x in e}           # record the path in DFS
    return DFS(1, e, path, indices)



############################################################################3333333


from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        k = self.main(edges)
        return edges[k]
    
            
    def Result(self, w, path, indices):  # given w is a vertex in a cycle, find the edge with the largest index in this cycle
        prev = w
        curr = path[w]
        M = indices[(curr, prev)]

        while curr != w:
            prev = curr
            curr = path[curr]
            M = max(M,indices[(curr, prev)])
        print(M)
        return M

    def DFS(self, v, e, path, indices):
        for w in e[v]:
            if path[v] == w:  # if predecessor of v is w, it's bad
                continue

            if path[w] != 0:  # the cycle is found
                path[w] = v   # complete the cycle
                return self.Result(w, path, indices)

            path[w] = v
            temp = self.DFS(w, e, path, indices)

            if temp:          # in case it is a dead end and returns nothing
                return temp
            path[w] = 0


    def main(self, edges):
        e = defaultdict(set)  # e[x] is the set of all vertices adjacent to x
        indices = {}                      # key is edge, value is indices in the list 'edges'
        for i,p in enumerate(edges):
            if p[1] in e[p[0]]:
                return p                  # if one edge appears twice in 'edges', return tha latter one
            e[p[0]].add(p[1])
            e[p[1]].add(p[0])
            indices[(p[0],p[1])] = indices[(p[1],p[0])] = i

        path = {x:0 for x in e}           # record the path in DFS
        
        return self.DFS(1, e, path, indices)



if __name__ == "__main__":
    # edges = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]
    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    # edges = [[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]

    edges = [[1,2],[1,3],[2,3]]
    print(main(edges))

    ob = Solution()
    t = ob.findRedundantConnection(edges)
    print(t)



