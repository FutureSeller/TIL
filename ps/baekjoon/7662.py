import sys
import heapq

T = int(sys.stdin.readline())

class DualPriorityQueue:
    def __init__(self, n):
        self.min_heap = []
        self.max_heap = []
        self.visited = [False] * n
    
    def add(self, value, idx):
        heapq.heappush(self.min_heap, (value, idx))
        heapq.heappush(self.max_heap, (-value, idx))
        self.visited[idx] = True
    
    def remove(self, ops):
        if ops == -1:
            while self.min_heap and self.visited[self.min_heap[0][1]] == False:
                heapq.heappop(self.min_heap)

            if self.min_heap:
                self.visited[self.min_heap[0][1]] = False
                heapq.heappop(self.min_heap)
        else:
            while self.max_heap and self.visited[self.max_heap[0][1]] == False:
                heapq.heappop(self.max_heap)

            if self.max_heap:
                self.visited[self.max_heap[0][1]] = False
                heapq.heappop(self.max_heap)

    def print(self):
        while self.min_heap and self.visited[self.min_heap[0][1]] == False:
            heapq.heappop(self.min_heap)

        while self.max_heap and self.visited[self.max_heap[0][1]] == False:
            heapq.heappop(self.max_heap)

        if not self.min_heap or not self.max_heap:
            print("EMPTY")
        else:
            print(-self.max_heap[0][0], self.min_heap[0][0])

for _ in range(T):
    N = int(sys.stdin.readline())
    q = DualPriorityQueue(N)
    for i in range(N):
        operator, operand = sys.stdin.readline().rstrip().split()
        operand = int(operand)

        if operator == "I":
            q.add(operand, i)
        if operator == "D":
            q.remove(operand)

    q.print()
