import sys
input = sys.stdin.readline

N, S = map(int, input().split())

numbers = list(map(int, input().rstrip().split()))
visited = [False] * N
count = 0

def dfs(begin, total, selected):
    global count
    if begin >= N: 
        return
    if total == S and selected > 0:
        count += 1

    for i in range(begin, N):
        if not visited[i]:
            visited[i] = True
            dfs(i, total + numbers[i], selected + 1)
            visited[i] = False

dfs(0, 0, 0)
print(count) # 부분 수열의 합 개수