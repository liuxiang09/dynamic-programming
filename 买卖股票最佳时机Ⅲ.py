# 123. 买卖股票的最佳时机 III
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        # dp[i][j][0/1]表示第i天，已经交易了j次，手上没有/有股票的最大收益
        dp = [[[0, 0] for _ in range(3)] for _ in range(n)]
        for i in range(n):
            for j in range(1, 3):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                # 第i天，已经交易了j次，手上没有股票的最大收益
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                # 第i天，已经交易了j次，手上有股票的最大收益
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[n-1][2][0]


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2


if __name__ == '__main__':
    prices = [3,3,5,0,0,3,1,4]
    print(Solution().maxProfit(prices)) # 6
