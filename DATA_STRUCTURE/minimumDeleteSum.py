def Solution(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(len(s1) - 1, -1, -1):
        dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])
    for j in range(len(s2) - 1, -1, -1):
        dp[len(s1)][j] = dp[len(s1)][j+1] + ord(s2[j])

    for i in range(len(s1) - 1, -1, -1):
        for j in range(len(s2) - 1, -1, -1):
            if s1[i] == s2[j]:
                a = dp[i+1][j+1]
                dp[i][j] = dp[i+1][j+1]
            else:
                b = dp[i+1][j]
                c = dp[i][j+1]
                dp[i][j] = min(dp[i+1][j] + ord(s1[i]),
                               dp[i][j+1] + ord(s2[j]))

    return dp[0][0]


if __name__ == '__main__':
    s1 = "sea"
    s2 = "eat"
    ret = Solution(s1, s2)
    print(ret)
