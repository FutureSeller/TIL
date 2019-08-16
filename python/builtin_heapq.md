### Heapq
- 추가적으로 내부를 건드릴 이유가 없다면 꽤나 유용한 heapq
- minheap만 되기 때문에, maxheap으로 쓰려면 음수로 변환하여 사용하면 됨
- 쉽게 정렬가능 or kth element 같은 것들을 구하기 용이함

``` python
import heapq

# insert element into maxHeap
nums = [5, 2, 3, 4]
maxHeap = []
for num in nums:
  heapq.heappush(maxHeap, -num)
print maxHeap # [-5, -4, -3, -2]

"""
-5 | -5 | -5 | -5 
   | -2 | -3 | -4
   |    | -2 | -3
   |    |    | -2
"""

# pop maximum value
print -heapq.heappop(maxHeap) # 5

# peek maximum value
print -maxHeap[0] # 4

# heapify list into minheap
nums = [5, 2, 3, 4]
heapq.heapify(nums) 
print nums # minHeap: [2, 3, 4, 5]

# heapify list into maxheap
nums = [5, 2, 3, 4]
tmp = map(lambda x: -x, nums)
heapq.heapify(tmp)
print nums # inverted maxHeap: [-5, -4, -3, -2]
```

- `__lt__`: primitive한 것이 아닌 object 들에 대해 heapq의 ordering 방식을 전달해주는 방법
``` python
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # self is less than others에 대한 조건
  def __lt__(self, other):
    return self.distance() > other.distance()
    
  def distance(self):
    return (self.x * self.x) + (self.y * self.y)
    
  def stringify(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')
    
result = []
heappush(result, Point(1, 1))
heappush(result, Point(3, 1))
for p in result:
  p.stringify()

# [3, 1]
# [1, 1]
```
