from collections import deque
import sys
input = sys.stdin.readline  

F, S, G, U, D = map(int, input().split())

def bfs(begin, target):
    answer = -1
    visited = {}
    queue = deque()
    queue.append((begin, 0))

    while queue:
        value, step = queue.popleft()
        if value == target:
            answer = step
            break
        if value in visited: continue
        if value < 1 or value > F: continue
        
        visited[value] = True
        queue.append((value + U, step + 1))
        queue.append((value - D, step + 1))
        
    return answer

if S == G:
    print(0)
else:
    value = bfs(S, G)
    if value == -1:
        print("use the stairs")
    else:
        print(value)
