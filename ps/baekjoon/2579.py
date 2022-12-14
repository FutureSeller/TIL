import sys
input = sys.stdin.readline

N = int(input())
STAIRS = list(map(int, sys.stdin.readlines()))

dp = [[0] * 2 for _ in range(N)]
dp[0][0] = STAIRS[0]

for i in range(1, len(STAIRS)):
    if i == 1:
        dp[i][0] = dp[i-1][0] + STAIRS[i]
        dp[i][1] = STAIRS[i]
    else:
        dp[i][0] = dp[i-1][1] + STAIRS[i]
        dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + STAIRS[i]

print(max(dp[N-1][0], dp[N-1][1]))