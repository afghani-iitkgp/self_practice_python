from typing import List 


def trappingRainWater(height):
    n = len(height)
    left_maxList = [0] * n 
    right_maxList = [0] * n

    l_max = 0
    r_max = 0

    for l in range(0, n):
        if height[l] > l_max:
            l_max = height[l]
            print(l, l_max)
        
        left_maxList[l] = l_max


    print(left_maxList)

    for r in range(n-1, -1, -1):
        if height[r] > r_max:
            r_max = height[r]
            print(r, r_max)

        right_maxList[r] = r_max

    print(right_maxList)

    water_trapped = 0
    for i in range(0, n):
        w = min(right_maxList[i], left_maxList[i]) - height[i]
        water_trapped += w
        # print(water_trapped)
    

    return water_trapped




if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [4,2,0,3,2,5]

    print(trappingRainWater(height))


