# 121. 买卖股票的最佳时机
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

# 暴力法
# 时间复杂度：O(n^2)
def maxProfit(prices) -> int:
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            max_profit = max(max_profit, prices[j] - prices[i])
    return max_profit


# 动态规划
# 时间复杂度：O(n)
def maxProfit(prices) -> int:
    if not prices:
        return 0
    # dp[i][j] 表示第i天的最大利润
    # j = 0 表示不持有股票
    # j = 1 表示持有股票
    dp = [[0 for i in range(2)] for j in range(len(prices))]
    # 边界设定
    # 第0天不持有股票，利润为0
    dp[0][0] = 0
    # 第0天持有股票，利润为 -prices[0]
    dp[0][1] = -prices[0]
    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], -prices[i])
    return dp[len(prices) - 1][0]


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices)) # 5

