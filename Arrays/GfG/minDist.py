def minDist(empArr, distArr):
    n = len(empArr)
    min_dist = 0
    on_left = 0
    on_right = 0


    for i in range(n):
        if empArr[i] == 1:
            on_left = i
            continue
        elif empArr[i] == 0:
            for j in range(i+1, n):
                if empArr[j] == 0:
                    if j == n-1:
                        min_dist +=  distArr[i] - distArr[on_left]
                    else:
                        continue
                elif empArr[j] == 1:
                    on_right = j
                    min_dist +=  min( (distArr[i] - distArr[on_left]) , (distArr[on_right] - distArr[i]))
                    break
    
    if empArr[n-1] == 0:
        min_dist += distArr[n-1] - distArr[on_left]

    

    return min_dist


if __name__ == "__main__":
    empArr = [1, 0, 0, 0, 1, 1, 0, 1, 0]
    distArr = [1, 2, 4, 7, 11, 13, 17, 22, 28]
    # empArr = [1, 0, 1]
    # distArr = [1, 5, 6]
    print(minDist(empArr, distArr))