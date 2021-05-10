from collections import defaultdict           
    
def DFS_travel(adj, s, visited, p, lst):
    # visited[s] = True
    # k = 0
    for i in adj[s]:
        if visited[i]==False:
            visited[i] = True
            lst.append(i)
            DFS_travel(adj, i, visited, s, lst)
            # if k != i:
            #     print(i)
            #     lst.append(i)
            # elif k == i:
            #     return lst
        elif i != p:
            # print("cycle is there = ", [i, s])
            # print(i)
            # lst.append(i)
            return lst
    
    return lst
        
def DFS_cycle(adj, s, visited, p, cycle):

    for i in adj[s]:
        if visited[i] == False:
            visited[s] = True
            result = DFS_cycle(adj, i, visited, s, cycle)
            if result == 'FINISHED':
                return 'FINISHED'
            elif result != 'NOCYCLE':
                cycle.append(s)

                if result == s:
                    return 'FINISHED'
                else:
                    return result

        elif (i != p):
    
            cycle.append(s)
            return i

    return 'NOCYCLE'

def DFS_cycle2(adj, s, visited, p, cycle):

    for i in adj[s]:
        if visited[i]==False:
            visited[i] = True
            k = DFS_cycle2(adj, i, visited, s, cycle)
            
            if (k == "stop"):
                return "stop"
            
            elif (k != 'no') and (k != s):
                cycle.append(s)
                return k

            elif (k == s):
                cycle.append(s)
                return "stop"



        elif (visited[i]==True) and (i != p):
            cycle.append(s)
            return i
    
    return "no"


def find_last_edge(cycle_lst):
    cycle_lst.append(cycle_lst[0])
    n = len(cycle_lst)
    E = defaultdict(list)

    for i in range(n-1):
        if cycle_lst[i] < cycle_lst[i+1]:
            a = cycle_lst[i]
            b = cycle_lst[i+1]
        else:
            a = cycle_lst[i+1]
            b = cycle_lst[i]

        E[a].append(b)




def has_cycle(adj, visited, s, p):
    # visited[s] = True

    for i in adj[s]:
        if visited[i] == False:
            visited[i] = True
            t = has_cycle(adj, visited, i, s)
            if t== True:
                return True

        elif i != p:
            return True
    
    return False

def find_redundant_connection(edges):


    graph = defaultdict(list)
    v_set = set()
    N = len(edges)
    visited2 = [False] * (N+1)

    # Create graph edge wise edge and check the cycle at every addition of the edge.
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        v_set.add(e[0])
        v_set.add(e[1])

        # V = max(v_set)

        visited = [False] * (N+1)       

        # for s in v_set:
        #     if visited2[s]==False:
        #         visited2[s] = True
        visited[1]=True
        if (has_cycle(graph, visited, 1, -1)):
            return e
        

    return []


if __name__ == "__main__":
    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    # edges = [[1, 2], [2, 3], [1, 3], [2, 4], [4, 5], [5, 6]]

    # edges = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]
    edges = [[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]
    # edges = [[1,2], [1,3], 
    #          [2,4], [2,5], 
    #          [3,6], [3,14], 
    #          [5,10],
    #          [6,7], [6,8], [6,9],
    #          [8,13],
    #          [9,11], [9,12], [9,13],
    #          [14,15], [14,16], [14,17],
    #          [15,19], [15,20], 
    #          [16,18]]

    # edges = [
    #          [1,2], [1,6], 
    #          [2,3], [2,5], 
    #          [3,4], [3,14], 
    #          [6,7], [6,8], [6,9],
    #          [7,13], [7,14],
    #          [9,10], [9,11], [9, 12],
    #          [14,15], [14,16], [14,17],
    #          [16,18]
    #          ]

    # print(find_redundant_connection_dfs(edges))

    # edges = [[1,2], [1,5], [2,3], [2,4], [4,6], [5,6]]
    adj = defaultdict(list)
    V_set = set()

    # for e in edges:
    #     adj[e[0]-1].append(e[1]-1)
    #     adj[e[1]-1].append(e[0]-1)
    #     V_set.add(e[0]-1)
    #     V_set.add(e[1]-1)
    
    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
        V_set.add(e[0])
        V_set.add(e[1])
    
    # print(V_set)
    V = len(V_set)
    # print(adj)
    visited = [0] * (V+1)
    # print(visited)
    lst = []

    # print(DFS_travel(adj, 1, visited, -1, lst))
    # print(lst)

    # DFS_cycle(adj, 1, visited, -1, lst)
    # DFS_cycle2(adj, 1, visited, -1, lst)


    print(find_redundant_connection(edges))
    #print(lst)

    #find_last_edge(lst)