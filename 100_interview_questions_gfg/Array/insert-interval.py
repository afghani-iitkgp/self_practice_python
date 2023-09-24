from typing import List

def insert(intervals, newInterval):
    n = len(intervals)
    result = []
    i = 0

    while (i < n):
        if (intervals[i][1] < newInterval[0]):
            result.append(intervals[i])
            i += 1
    
    print(i)

    x = min(intervals[i][0], newInterval[0])

    while (i < n) and (intervals[i][0] <= newInterval[1]):
        i += 1
    
    # if intervals[i][0] == newInterval[1]:
    #     y = intervals[i][1]
    # else:
    y = max(intervals[i-1][1], newInterval[1])

    result.append([x, y])

    while (i < n):
        result.append(intervals[i])
        i += 1
    

    return result



def insert2(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)

    # Add all the intervals ending before new_interval starts
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # Merge all overlapping intervals to one considering new_interval
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval = [ min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1]) ]
        
        i += 1

    result.append(new_interval)  # Add the union of intervals we got

    # Add all the rest
    while i < n:
        result.append(intervals[i])
        i += 1

    return result     


def insert_needcode(intervals, newInterval):
    result = []
    n = len(intervals)

    for i in range(n):
        if intervals[i][1] < newInterval[0]:         # Insert those intervals which are less than newInterval.start
            result.append(intervals[i])
        elif intervals[i][0] > newInterval[1]:       # Insert those intervals which are greater than newInterval.end
            result.append(newInterval)
            result.append(intervals[i : ])
            return result
        else:
            x = min(intervals[i][0], newInterval[0])
            y = max(intervals[i][1], newInterval[1])
            newInterval = [x, y]
    
    result.append(newInterval)

    return result


def insert_whileloop(intervals, newIntervals):
    pass


if __name__ == "__main__":
    # Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    # Output: [[1,5],[6,9]]


    # Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    # Output: [[1,2],[3,10],[12,16]]
    intervals = [[1,3],[6,9]] 
    newInterval = [2,5]

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] 
    newInterval = [4,8]
    
    # intervals = [[1,5]]
    # newInterval = [6, 8]

    # print(insert2(intervals, newInterval))
    print(insert_needcode(intervals, newInterval))