def lcs(a, b):
    m, n = len(a), len(b)
    # dp[i][j] 表示 a[0:i] 和 b[0:j] 的最长公共子序列的长度
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    # 边界设定
    for i in range(m + 1):
        dp[i][0] = 0
    for j in range(n + 1):
        dp[0][j] = 0
        
    # 递推公式
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
    return dp[m][n]

if __name__ == '__main__':
    a = "abcde"
    b = "ace"
    print(lcs(a, b)) # 3