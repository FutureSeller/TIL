# from collections import deque
# import sys
# input = sys.stdin.readline  

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# N, M = map(int, input().split())
# ice = [[int(x) for x in row.rstrip().split()] for row in sys.stdin.readlines()]
# attack_surface = [[0] * M for _ in range(N)]
# visited = [[False] * M for _ in range(N)]

# def reset_visited():
#     for index in range(N * M):
#         visited[index // M][index % M] = False

# def rearrange_attack_surface():
#     for index in range(N * M):
#         i = index // M
#         j = index % M
#         if i == 0 or j == 0: continue
#         if i == N - 1 or j == M - 1: continue

#         count = 0
#         for k in range(4):
#             x = dx[k] + i
#             y = dy[k] + j
#             if ice[x][y] == 0: count += 1
#         attack_surface[i][j] = count

# def get_ice_amount_bfs(row, col, visited):
#     queue = deque()
#     queue.append((row, col))

#     while queue:
#         _row, _col = queue.popleft()
#         if visited[_row][_col]: continue
#         visited[_row][_col] = True

#         for k in range(4):
#             x = dx[k] + _row
#             y = dy[k] + _col
#             if 1 <= x < N and 1 <= y < M and ice[x][y] != 0:
#                 queue.append((x, y))

# def get_ice_mountain_count():
#     reset_visited()
#     answer = 0
#     for index in range(N * M):
#         i = index // M
#         j = index % M
#         if i == 0 or j == 0: continue
#         if i == N - 1 or j == M - 1: continue

#         if visited[i][j]: continue
#         if ice[i][j] == 0: 
#             continue
#         get_ice_amount_bfs(i, j, visited)
#         answer += 1
#     return answer

# def go_attack():
#     for index in range(N * M):
#         i = index // M
#         j = index % M
#         if i == 0 or j == 0: continue
#         if i == N - 1 or j == M - 1: continue

#         temp = ice[i][j]
#         if temp == 0: continue
#         sub = temp - attack_surface[i][j]
#         ice[i][j] = sub if sub > 0 else 0

# def main():
#     rearrange_attack_surface()
#     amount = get_ice_mountain_count()
#     if amount >= 2:
#         print(0)
#     elif amount == 0:
#         print(0)
#     else:
#         year = 0
#         while True:
#             year += 1
#             go_attack()
#             rearrange_attack_surface()
#             amount = get_ice_mountain_count()
#             if amount == 0:
#                 print(0)
#                 break
#             if amount >= 2:
#                 print(year)
#                 break

# main()


from collections import deque
import sys
input = sys.stdin.readline  

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
ice = [[int(x) for x in row.rstrip().split()] for row in sys.stdin.readlines()]
year = 0

def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if ice[nx][ny] == 0:
                    if ice[x][y]:
                        ice[x][y] -= 1
                else:
                    visited[nx][ny] = 1
                    q.append([nx, ny])

while True:
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ice[i][j] and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    if cnt == 0:
        year = 0
        break
    if cnt > 1:
        break
    year += 1

print(year)