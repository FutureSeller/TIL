import sys
stdin = sys.stdin

N = int(stdin.readline())
blue = 0
white = 0
board = [[0] * N for _ in range(N)]

for i in range(N):
    tiles = list(map(int, stdin.readline().rstrip().split()))
    for j in range(len(tiles)):
        board[i][j] = tiles[j]

def traverse(start, end, size):
    global blue, white
    if size == 0:
        return board[start][end]

    a = traverse(start, end, size // 2)
    b = traverse(start, end + size, size // 2)
    c = traverse(start + size, end, size // 2)
    d = traverse(start + size, end + size, size // 2)

    if a == b == c == d:
        return a
    else:
        blue += [a,b,c,d].count(1)
        white += [a,b,c,d].count(0)
        return -1


value = traverse(0, 0, N // 2)
if value == 1: blue += 1
elif value == 0: white += 1
else: pass

print(white)
print(blue)
