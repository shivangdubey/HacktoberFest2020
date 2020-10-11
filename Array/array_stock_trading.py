'''
Problem Statement: Given an array of numbers consisting of daily
stock prices, calculate the maximum amount of profit that can be
made from buying on one day and selling on another day.
'''

# Solution-1: Brute-Force approach
# TC: O(n^2)
# SC: O(1)

def stock_trading(prices):
    max_profit = 0
    for i in range(len(prices) - 1):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]

    return max_profit


# Solution-2:
# TC: O(n)
# SC: O(1)

def stock_trading_optimal(A):
    max_profit = 0.0
    min_price = float('inf')
    for price in A:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit 

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(stock_trading_optimal(A))
