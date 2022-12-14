from collections import deque
import sys
input = sys.stdin.readline

N = map(int, input().split())
CONTAINER = [[0] * N for _ in range(M)]

q = deque()
number_of_tomatoes = 0
number_of_blank = 0

for i in range(M):
    tomatos = list(map(int, input().split()))
    for j in range(N):
        if tomatos[j] == -1:
            number_of_blank += 1

        if tomatos[j] == 1:
            number_of_tomatoes += 1
            q.append((i, j, 0))
        CONTAINER[i][j] = tomatos[j]

if len(q) == 0:
    print(-1)
else:
    while q:
        x, y, day = q.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < M and 0 <= ny < N and CONTAINER[nx][ny] == 0:
                CONTAINER[nx][ny] = 1
                number_of_tomatoes += 1
                q.append((nx, ny, day + 1))
    if number_of_tomatoes + number_of_blank == N * M:
        print(day)
    else:
        print(-1)