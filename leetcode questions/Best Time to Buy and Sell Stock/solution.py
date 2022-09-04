def maxProfit(prices):
    if len(prices) == 1:
        return 0
    maxProfit = 0
    buyPrice = prices[0]
    for i in range(len(prices)-1):
        currentProfit = prices[i+1] - min(prices[i], buyPrice)
        if currentProfit < 0:
            continue
        else:
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            if currentProfit > maxProfit:
                maxProfit = currentProfit  
    return maxProfit     

print(maxProfit([7]))   
