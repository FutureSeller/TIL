import sys

int(sys.stdin.readline())
inputs = list(map(int, sys.stdin.readlines()))

dp = [0] * 101
dp[0], dp[1], dp[2] = 1, 1, 1

for value in inputs:
  for i in range(3, value):
    dp[i] = dp[i - 2] + dp[i - 3]

  print(dp[value-1])