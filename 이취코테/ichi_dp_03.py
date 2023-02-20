def solution(N, T, P):
    dp = [0 for _ in range(N+1)]

    for i in range(N):
        for j in range(i+T[i], N+1):
            dp[j] = max(dp[j], dp[i] + P[i])

    return dp[-1]


T = [3, 5, 1, 1, 2, 4, 2]
P = [10, 20, 10, 20, 15, 40, 200]
solution(7, T, P)
