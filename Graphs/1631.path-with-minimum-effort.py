

def minimumEffortPath(heights):
    m, n = len(heights), len(heights[0])
    neibs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    
    beg = -1 
    end = max(max(heights, key=max))
    
    while beg + 1 < end:
        mid = (beg + end)//2
        visited = set()
        dfs(mid, 0, 0, visited, neibs)

        if (m - 1, n - 1) in visited:
            end = mid
        else:
            beg = mid
            
    return end



def dfs(LIMIT, x, y, visited, neibs):
    visited.add((x, y)) 
    for dx, dy in neibs:
        if 0<=dx+x<m and 0<=dy+y<n and (dx+x, dy+y) not in visited:
            if abs(heights[x][y] - heights[dx+x][dy+y]) <= LIMIT:
                dfs(LIMIT, dx+x, dy+y, visited, neibs)



def minimum_effort_path(A, visit, i, j, m, n, ):
    # Base condition
    if (i == m-1 and j == n-1 ):
        return "reached"

    neighbour = {}
    small = 0
    x, y = i, j


    if (j > 0 and visit[i][j-1]==False) :
        if small >= (A[i][j-1] - A[i][j]) :
            small = A[i][j-1] - A[i][j]
            x, y = i, j-1
            neighbour[str(x)+str(y)] = small
    
    if (j < n-1 and visit[i][j+1]==False) :
        if small >= (A[i][j+1] - A[i][j]) :
            small = A[i][j+1] - A[i][j]
            x, y = i, j+1
            neighbour[str(x)+str(y)] = small

    
    if (i > 0 and visit[i-1][j]==False):
        if small >= (A[i-1][j] - A[i][j]):
            small = A[i-1][j] - A[i][j]
            x, y = i-1, j
            neighbour[str(x)+str(y)] = small


    if (i < m-1 and visit[i+1][j]==False):
        if small >= (A[i+1][j] - A[i][j]) :
            small = A[i+1][j] - A[i][j]
            x, y = i, j-1
            neighbour[str(x)+str(y)] = small


    
    # To check whether it is stuck and then backtrack.
    if (x==i and y==j):
        return "stuck"
    
    else:
        t = minimum_effort_path(A, visit, x, y, m , n)

        if t == "stuck":
            pass
            
        elif t == "reached":
            return "reached" 




if __name__ == "__main__":

    heights = [
                [1,2,1,1,1],
                [1,2,1,2,1],
                [1,2,1,2,1],
                [1,2,1,2,1],
                [1,1,1,2,1]
            ]

    heights = [[1,2,2],[3,8,2],[5,3,5]]

    m = len(heights)
    n = len(heights[0])

    visit = [ [False] * n for _ in range(m)]

    # minimum_effort_path( heights, visit,  0, 0, m, n )
    print(minimumEffortPath(heights))
    