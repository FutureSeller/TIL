### Deque
- a.k.a 양방향 큐: 앞 뒤로 요소를 추가하거나 지울 수 있음
- `list.append(something)`의 경우, O(1)이나, `list.insert(0, something)`의 경우, O(N)으로 매우 손해를 봄

``` python
from collections import deque

# insert element into maxHeap
nums = [5, 2, 3, 4]
dq = deque(nums)

dq.append(1) # list.append; [5, 2, 3, 4, 1]
dq.appendleft(0) # list.insert(0, 0); [0, 5, 2, 3, 4, 1]
dq.extend([10, 20]) # [0, 5, 2, 3, 4, 1, 10, 20]
dq.extendleft([-1, -2]) # [-2, -1, 0, 5, 2, 3, 4, 1, 10, 20]
dq.remove(0) # 값 삭제: [-2, -1, 5, 2, 3, 4, 1, 10, 20]
dq.pop() # [-2, -1, 5, 2, 3, 4, 1, 10]
dq.popleft() # [-1, 5, 2, 3, 4, 1, 10]
dq.rotate(1) # [10, -1, 5, 2, 3, 4, 1]
dq.rotate(-1) # [-1, 5, 2, 3, 4, 1, 10]
```
