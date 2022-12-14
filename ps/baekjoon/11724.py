import sys

N, M = map(int, sys.stdin.readline().split())
root = [0] * N
for i in range(N):
  root[i] = i

def find(x):
  if x != root[x]:
    root[x] = find(root[x])
  return root[x]

def union(x, y):
  x = find(x)
  y = find(y)

  if x != y:
    root[x] = y

root_dict = {}
for _ in range(M):
  x, y = map(int, sys.stdin.readline().split())
  if x == y: continue
  union(x-1, y-1)

for i in range(len(root)):
  x = find(root[i])
  root[i] = x

print(len(set(root)))
