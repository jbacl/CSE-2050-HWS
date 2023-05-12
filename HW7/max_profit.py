##### TODO 1 #####
from re import L


def price_to_profit(L):
    profit = []
    for i in range(len(L)):
        if i == 0:
            profit.append(0)
        else:
            profit.append(L[i] - L[i-1])
    return profit



# brute force solution
def max_profit_brute(L):
    """Finds maximum profit. Assumes L is a list of profits (i.e. change in price every day), not raw prices"""
    n = len(L)
    max_sum = 0 # assume we can at least break even - buy and sell on the same day

    # outer loop finds the max profit for each buy day
    for i in range(n):
       # total profit if we bought on day i and sold on day j
        total = L[i]
        if total > max_sum: max_sum = total
        
        for j in range(i+1, n): 
            total += L[j] # total profit if we sell on day j
                          # we assume L[j] is the profit if we bought on day j-1 and sold on day j
                          # i.e., L is the change in value each day, relative to the day before
            if total > max_sum: max_sum = total

    return max_sum


##### TODO 2 #####
# you'll need a helper function or default parameters here
def max_profit(L, left=0, right=None):  # O(nlogn)
    # BASE CASE
    if right == None:
        right = len(L) - 1
    #    Only 1 item? Max profit is easy - it's the profit if we bought the day before and sold today
    if right == left:
        return L[right]
    median = (left+right) // 2
    # DIVIDE into three problems and CONQUER:
    #    find the max profit if we buy and sell in the left (recursive call)
    left_val = max_profit(L, left, median)
    #    find the max profit if we buy and sell in the right (recursive call)
    right_val = max_profit(L, median+1, right)
    #    find the max profit if we buy in the left and sell in the right (requires a separate function)
    total = max_profit_crossing(L, left, right, median)
    # COMBINE subproblems into the solution for this level of recursion
    #    Which of the above three scenarios gives the best profit?
    return max(left_val, right_val, total)

##### TODO 3 #####
def max_profit_crossing(L, left, right, median):
   # O(n): Max profit if we sell on the median?
    left_max = L[median]
    i1 = 0
    for x in range(median, left-1, -1):
        i1 += L[x]
        if i1 > left_max:
            left_max = i1
    right_max = L[median+1] 
   # O(n): Max profit if we buy on the median?
    i2 = 0
    for j in range(median+1, right+1):
        i2 += L[j]
        if i2 > right_max:
            right_max = i2
    total = right_max + left_max
    return max(left_max, right_max, total)
   # O(1): Max profit if we buy before and sell after?
   