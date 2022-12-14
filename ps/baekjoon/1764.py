import sys
N, M = map(int, sys.stdin.readline().split())

names = {}

for i in range(N):
  v = sys.stdin.readline().rstrip()
  names[v] = True

n = []
for _ in range(M):
  n.append(sys.stdin.readline().rstrip())

n.sort()
count = 0
p = []
for _ in range(M):
  if n[_] in names:
    count += 1
    p.append(n[_])

print(count)
for _ in p:
  print(_)
