'''
Set Matrix Zero
Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.
'''

def setMatrixZero(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    zero_idx = []

    for i in range(n_rows):
        for j in range(n_cols):
            if matrix[i][j] == 0:
                zero_idx.append([i, j])


    # Setting zero 
    for a, b in zero_idx:
        for i in range(n_rows):
            matrix[i][b] = 0
        for j in range(n_cols):
            matrix[a][j] = 0

    return matrix



if __name__ == "__main__":
    matrix = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
        ]
    
    # matrix = [
    #     [0,1,2,0],
    #     [3,4,5,2],
    #     [1,3,1,5]
    #     ]

    matrix = [[1]]
    

    matrix2 = setMatrixZero(matrix)

    from pprint import pprint

    pprint(matrix)
