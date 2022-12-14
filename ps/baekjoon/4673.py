dp = [True for i in range(10001)]

def mark(n):
    if dp[n] == False:
        return

    temp = n
    while temp < 10000:
        num_list = list(map(int, str(temp)))
        temp = temp + sum(num_list)
        if temp > 10000:
            break
        dp[temp] = False

i = 1
for i in range(1, 10001):
    mark(i)
    
for i in range(1, 10001):
    if dp[i]:
        print(i)
