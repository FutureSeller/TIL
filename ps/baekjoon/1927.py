import heapq
import sys

N = int(sys.stdin.readline())

numbers = []

for _ in range(N):
  v = int(sys.stdin.readline())
  if v == 0:
    if not numbers: print(0)
    else: print(heapq.heappop(numbers))
  else:
    heapq.heappush(numbers, v)
