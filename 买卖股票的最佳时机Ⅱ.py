# 122. 买卖股票的最佳时机 II

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        # dp[i][j] 表示第i天的最大利润, j = 0 表示不持有股票, j = 1 表示持有股票
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
        return dp[-1][0]
    

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices)) # 7
