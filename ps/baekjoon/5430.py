from collections import deque
import sys
stdin = sys.stdin

T = int(stdin.readline())

while T > 0:
    P = stdin.readline().rstrip()
    N = stdin.readline().rstrip()
    ARR = stdin.readline().rstrip().replace("[", "").replace("]","")

    if not N and "D" in P:
        print("error")
        continue
    
    dq = deque(list(map(int, ARR.split(','))) if ARR else [])
    move_forward = True

    for ch in P:
        if ch == "R": 
            move_forward = not move_forward
        else:
            if not dq:
                print("error")
                break

            if move_forward:
                dq.popleft()
            else: 
                dq.pop()
    else:
        print("[", end="")
        while len(dq) > 1:
            if move_forward:
                print(dq.popleft(), end=",")
            else:
                print(dq.pop(), end=",")
        
        if dq:
            print(dq.pop(), end="")
        print("]")

    T -= 1
