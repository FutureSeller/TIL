import sys

N = int(sys.stdin.readline())
default_value = (1 << 21) - 1
bitmask = 0

for i in range(N):
    op = sys.stdin.readline().rstrip().split()
    if op[0] == 'add':
        position = int(op[1])
        bitmask |= 1 << (position)
    elif op[0] == 'remove':
        position = int(op[1])
        bitmask &= ~(1 << position)
    elif op[0] == 'check':
        position = int(op[1])
        if bitmask & 1 << position: print(1)
        else: print(0)
    elif op[0] == 'toggle':
        position = int(op[1])
        bitmask ^= 1 << position
    elif op[0] == "all":
        bitmask = default_value
    elif op[0] == "empty":
        bitmask = 0
        
