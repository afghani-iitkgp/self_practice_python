"""
Check if a key is present in every segment of size k in an array.
Input : 
arr[] = { 3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3} 
x = 3 
k = 3 
Output : Yes 
There are 4 non-overlapping segments of size k in the array, 
{3, 5, 2}, {4, 9, 3}, {1, 7, 3} and {11, 12, 3}. 3 is present all segments.
"""

def find_x_in_k_windowSize(arr : list, x : int, k : int, n : int) -> bool :
    i = 0
    c = 0
    t = []

    while (c<n):
        if c+k <= n:
            for i in range(c, c+k):
                if (arr[i] == x):
                    t.append(True)
                    break
                elif i==c+k-1:
                    t.append(False)
                    break
                # elif IndexError:
                #     t.append(False)
                #     break
        else:
            for i in range(c, n):
                if (arr[i] == x):
                    t.append(True)
                    break
                elif i == n-1:
                    t.append(False)
                    break
            
        c += k


    if False in t:
        return False
    else:
        return True







if __name__ == "__main__":
    arr = [ 3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3 ,8, 3, 9, 8, 3]
    # arr = [3, 5, 2, 4, 9]
    x, k = 3, 3
    n = len(arr)

    if ( find_x_in_k_windowSize(arr, x, k, n) ):
        print("Yes")
    else:
        print("Not found in all")
