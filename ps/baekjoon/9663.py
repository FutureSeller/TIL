N = int(input())

ans = 0
board = [0] * N
visited = [False] * N

def check(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == abs(x - i):
            return False
    return True

def n_queens(depth):
    global ans
    if depth == N:
        ans += 1
        return
    
    for i in range(N):
        if visited[i] == False:
            board[depth] = i

            if check(depth):
                visited[i] = True
                n_queens(depth + 1)
                visited[i] = False

n_queens(0)
print(ans)