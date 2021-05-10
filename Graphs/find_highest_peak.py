
from typing import List

def highestPeak(isWater: List[List[int]]) -> List[List[int]]:
    Row = len(isWater)
    Col = len(isWater[0])
    
    A = [ [0 for _ in range(Col)] for _ in range(Row)]
    
    for i in range(Row):
        for j in range(Col):
            if isWater[i][j] == 0:
                A[i][j] = 2
            elif isWater[i][j] == 1:
                A[i][j] = 0
    
    print(A)
                
    for i in range(Row):
        for j in range(Col):
            if A[i][j] == 2 or A[i][j]==1:
                continue
            elif A[i][j] == 0:
                if i>0 and A[i-1][j] != 0:
                    A[i-1][j] = 1

                if i<Row-1 and A[i+1][j] != 0:
                    A[i+1][j] = 1

                if j>0 and A[i][j-1] != 0:
                    A[i][j-1] = 1

                if j<Col-1 and A[i][j+1] != 0:
                    A[i][j+1] = 1
    
    return A

class Node:
    def __init__(i, j, val, visited):
        self.i = i
        self.j = j
        self.val = val
        self.visited = visited


from collections import deque

def highest_peak2(A):
    q = queue()
    m = len(A)
    n = len(A[0])

    for i in A:
        for j in i:
            if A[i][j] == 0:
                u = Node(i, j, 0, False)
                
                continue
            elif A[i][j] == 1:
                u = Node(i, j, 0, True)
                q.append(u)
    
    while (len(q) > 0):
        s = q.pop()

        if i>0:
            u = Node(i-1, j, )


                


if __name__ == "__main__":
    isWater = [[0,0,1],[1,0,0],[0,0,0]]
    isWater = [[0,1, 0]]
    #isWater = [[0,1,0,1], [0,0,0,1]]
    isWater = [ 
                [0,0,0,0,0,0,1,0],
                [0,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,0],
                [0,0,1,0,0,0,0,0]
            ]

    # print(highestPeak(isWater))
    A = highestPeak(isWater)
    A_exp = [[2,1,2,3,2,1,0,1],[1,0,1,2,3,2,1,2],[2,1,2,3,4,3,2,3],[3,2,3,4,5,4,3,4],[4,3,3,4,4,3,2,3],[4,3,2,3,3,2,1,2],[3,2,1,2,2,1,0,1],[2,1,0,1,2,2,1,2]]
    for i in A:
        print(i)
    
    print("*" * len(A))

    for i in A_exp:
        print(i)
    