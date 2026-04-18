def maxProfit(prices):
    n = len(prices)
    lMin = prices[0]
    lMax = prices[0]
    res = 0
    i = 0
    while i < n - 1:
        while i < n - 1 and prices[i] >= prices[i + 1]:
            i += 1
        lMin = prices[i]
        while i < n - 1 and prices[i] <= prices[i + 1]:
            i += 1
        lMax = prices[i]
        res += lMax - lMin
    return res