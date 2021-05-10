import os
import math


def finalInstances(instances, averageUtil):
    # Write your code here
    
    # base case
    if len(averageUtil) == 0:
        return instances
    if instances == 0:
        return 0
    # if instances == 1:
    #     finalInstances(instances, averageUtil[1:])
    #     return instances
    
    
    if averageUtil[0] < 25:
        if instances%2==0:
            instances = instances/2
        else:
            instances = int(instances/2) + 1
        
        if len(averageUtil)>11:
            averageUtil = averageUtil[11:]
            finalInstances(instances, averageUtil)
            return instances
        else:
            return instances
        
    elif ((averageUtil[0] >=25) and (averageUtil[0] <=60) ):
        averageUtil = averageUtil[1:]
        finalInstances(instances, averageUtil)
        return instances
        
    elif averageUtil[0] > 60:
        if (instances<100000000):
            instances = int(instances)*2
            if len(averageUtil)>11:
                averageUtil = averageUtil[11:]
                finalInstances(instances, averageUtil)
            else:
                return instances
        else:
            averageUtil = averageUtil[1:]
            finalInstances(instances, averageUtil)
    
    
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # instances = int(input().strip())

    # averageUtil_count = int(input().strip())
    instances = 1

    averageUtil = [5,10,80]


    # for _ in range(averageUtil_count):
    #     averageUtil_item = int(input().strip())
    #     averageUtil.append(averageUtil_item)

    result = finalInstances(instances, averageUtil)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
