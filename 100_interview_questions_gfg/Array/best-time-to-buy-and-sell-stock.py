from typing import List

'''
Type I: At most one transaction is allowed
Given an array prices[] of length N, representing the prices of the stocks on different days, the task is to find the maximum profit possible for buying and selling the stocks on 
different days using transactions where at most one transaction is allowed.

Note: Stock must be bought before being sold.

'''

def maxProfit_type1(prices: List) -> int:
    n = len(prices)
    
    max1 = 0

    for i in range(n-1):    
        max2 = 0
        for j in range(i+1, n):
            if (prices[j] - prices[i]) > max2:
                max2 = prices[j] - prices[i]

        max1 = max2 if max1 < max2 else max1


    return max1





'''
Type II: Infinite transactions are allowed
Given an array price[] of length N, representing the prices of the stocks on different days, the task is to find the maximum profit possible for buying and selling the stocks on 
different days using transactions where any number of transactions are allowed.
'''

def maxProfit_type2(A: List) -> int:
    buy_index = []
    sell_index = []

    n = len(A)

    for i in range(1, n-1):
        if A[i] > A[i+1] and A[i] > A[i-1]:
            sell_index.append(i)
        elif A[i] < A[i+1] and A[i] < A[i-1]:
            buy_index.append(i)

        elif i==1:
            if A[0] > A[1]:
                sell_index.append(0)
            elif A[0] < A[1]:
                buy_index.append(0)
        elif i==n-2:
            if A[-1] > A[-2]:
                sell_index.append(n-1)
            elif A[-1] < A[-2]:
                buy_index.append(n-1)
        
    
    profit = 0
    buy_price = None
    sell_price = None

    for i in range(n):
        if buy_price is not None and i in sell_index:
            sell_price = A[i]
        elif i in buy_index:
            buy_price = A[i]

        if sell_price is not None and buy_price is not None:
            print(buy_price, " ", sell_price)
            profit += sell_price - buy_price
            buy_price = None
            sell_price = None

    # print(profit)

    return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    # prices = [7, 6, 4, 3, 1]
    prices = [7, 1, 5, 3, 6, 4, 8, 6, 5]
    # prices = [1, 2, 3, 4, 5]


    print(maxProfit_type2(prices))