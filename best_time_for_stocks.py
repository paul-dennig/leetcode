def maxProfit(prices):
    days = len(prices)
    profits = [0] * days
    for i in range(days):
        todays_profit = [a - prices[i] for a in prices[i:days]]
        max_daily_profit = max(todays_profit)
        if max(todays_profit) > 0:
            profits[i] = max_daily_profit
    print(profits)
    return max(profits)

print(maxProfit([7, 1, 5, 3, 6, 4]))
