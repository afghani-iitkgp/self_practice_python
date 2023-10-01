from typing import List


def maxArea_bruteforce(height : List[int]) -> int:
    max_area = 0

    n = len(height)

    for i in range(0, n-1):

        for j in range(i+1, n):
            area = min(height[i], height[j]) * (j - i)
            max_area = area if area > max_area else max_area
            print(max_area)

    return max_area

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]

    print(maxArea_bruteforce(height))