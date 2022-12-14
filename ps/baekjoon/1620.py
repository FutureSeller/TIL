from collections import OrderedDict
import sys

N, M = map(int, sys.stdin.readline().split())

pokemon = OrderedDict()
names = []

for idx in range(0, N):
  name = sys.stdin.readline().rstrip()
  names.append(name)
  pokemon[name] = idx

for _ in range(M):
  name = sys.stdin.readline().rstrip()
  if name not in pokemon:
    print(names[int(name)-1])
  else:
    print(pokemon[name] + 1)
