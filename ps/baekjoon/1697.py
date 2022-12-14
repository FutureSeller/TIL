from collections import deque
import sys
input = sys.stdin.readline  

MAX_VALUE = 100000
n, k = map(int, input().split())

total_trial = []

def bfs(begin):
    visited = {}
    queue = deque()
    queue.append((begin, 0))
    

    while queue:
        value, step = queue.popleft()
        if value == k: 
            print(step)
            break
        if value in visited: continue
        if value > MAX_VALUE: continue

        visited[value] = True

        queue.append((value - 1, step + 1))
        queue.append((value * 2, step + 1))
        queue.append((value + 1, step + 1))

if n == k:
    print(0)
elif n >= k:
    print(n - k)
else:
    bfs(n)
