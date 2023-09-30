
def find_centre_of_star_graph(edges):
    count = {}

    for e in edges:
        count[e[0]] = 0
        count[e[1]] = 0
    # print(count, end="  ")

    N = 0
    for e in edges:
        count[e[0]] += 1
        count[e[1]] += 1
        N += 1
    # print(count, end="  ")

    for k,v in count.items():
        if v==N:
            centre = k
        elif v==1:
            continue
        else:
            centre = -1
    
    return centre

        
        



if __name__ == "__main__":
    # edges = [[1,2],[5,1],[1,3],[1,4]]
    edges = [[1,2],[2,3],[4,2]]
    print(find_centre_of_star_graph(edges))