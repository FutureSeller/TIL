"""
그저, bruteforce
"""
# n, m = map(int, input().split())
# numbers = list(map(int, input().split()))
# numbers.sort()

# N = len(numbers)
# answer = 0
# for i in range(N):
#     for j in range(i + 1, N):
#         for k in range(j + 1, N):
#             value = numbers[i] + numbers[j] + numbers[k]
#             if value <= m and abs(answer - m) > abs(value -m):
#                 answer = value
# print(answer)

"""
DFS
"""
class BlackJack:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target
        self.max_num = 0
        self.stack = []
        self.dfs(0)
    
    def dfs(self, begin):
        if len(self.stack) == 3:
            if sum(self.stack) <= self.target:
                self.max_num = max(self.max_num, sum(self.stack))
            return

        for i in range(begin, len(self.numbers)):
            self.stack.append(self.numbers[i])
            self.dfs(i + 1)
            self.stack.pop()
    
    def get_max_num(self):
        return self.max_num

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
print(BlackJack(numbers, m).get_max_num())