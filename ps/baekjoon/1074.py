N, r, c = map(int, input().split())

trial = N - 1
answer = 0

while trial:
  base = 2 ** trial
  if r >= base:
    r -= base
    answer += base * (2 ** (trial+1))
  if c >= base:
    c -= base
    answer += base * (2 ** trial)
  trial -= 1

if r > 0:
  answer += 2
if c > 0:
  answer += 1

print(answer)