def knapsack(w, total = 5):
    """
    :type w: list
    :rtype: int
    """
    dp = [[0 for i in range(total + 1)] for j in range(len(w) + 1)]
    for idx in range(1, len(w) + 1):
        for jdx in range(1, total + 1):
            if w[idx - 1][1] > jdx:
                dp[idx][jdx] = dp[idx-1][jdx]
            else:
                dp[idx][jdx] = max(dp[idx-1][jdx], w[idx - 1][0] + dp[idx - 1][jdx - w[idx - 1][1]])
    for row in dp:
        print(row)


knapsack([(100, 3), (20, 2), (60, 4), (40, 1)])
