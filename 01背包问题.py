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
    # 生成更复杂的测试数据
    import random
    N = 10
    W = 20
    weight = [random.randint(1, 10) for i in range(N)]
    value = [random.randint(1, 10) for i in range(N)]

    # 为数据简单可视化
    print("物品重量：", end='')
    for i in range(N):
        print(weight[i], end=' ')
    print()
    print("物品价值：", end='')
    for i in range(N):
        print(value[i], end=' ')
    print()
    print("背包容量：", W)
    print(knapsack(N, W, weight, value))

    # 写出具体的放入背包的物品
    # 从最后一个物品开始，如果knapsack(i, j, weight, value) > knapsack(i - 1, j, weight, value)，
    # 则说明第i个物品放入背包后的最大价值大于不放入第i个物品的最大价值，所以第i个物品放入背包
    # 然后把背包的容量减去第i个物品的重量，继续判断第i-1个物品是否放入背包
    i = N
    j = W
    while i > 0:
        if knapsack(i, j, weight, value) > knapsack(i - 1, j, weight, value):
            print("第", i, "个物品放入背包")
            j -= weight[i - 1]
        i -= 1
        
