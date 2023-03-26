# 01背包问题

def knapsack(N, W, weight, value):
    # 定义二维数组dp[i][j]表示前i个物品放入容量为j的背包中的最大价值
    dp = [[0 for i in range(W + 1)] for j in range(N + 1)]

    # 边界设定
    # 0个物品放入容量为j的背包中的最大价值为0
    for j in range(W + 1):
        dp[0][j] = 0
    # 前i个物品放入容量为0的背包中的最大价值为0
    for i in range(N + 1):
        dp[i][0] = 0
    # 递推公式
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            # 如果第i个物品的重量大于背包的容量j，那么第i个物品不能放入背包中
            if j < weight[i - 1]:
                dp[i][j] = dp[i - 1][j]
            # 如果第i个物品的重量小于等于背包的容量j，那么第i个物品可以放入背包中,
            # 但是放不放取决于放入第i个物品后的最大价值和不放入第i个物品的最大价值谁大
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])
    return dp[N][W]


if __name__ == '__main__':
    N = 3
    W = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    print(knapsack(N, W, weight, value))