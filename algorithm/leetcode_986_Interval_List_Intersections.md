## Problem 
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that is either empty, 
or can be represented as a closed interval.
For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

## How to Sovle
1. each list of closed intervals는 *disjoint* (매우 중요함) |--A--|--B--|와 같은 경우가 없다는 것
2. START를 기준으로 이미 정렬되어 있음
3. 겹치는 경우의 수는 4가지 
```
# a. A가 B에 포함됨
|--- B ---|
 |-- A --|

# b. A의 START가 B의 interval내에 존재
|--- B ---|
     |-- A --|

# c. a와 b의 역
```

4. a&&b를 표현해보자면 `a[START] >= b[START] and a[START] <= b[END]`
5. c는`b[START] >= a[START] and b[START] <= a[END]`
6. intersection을 표현해보자면 `[max(A[START], B[START]), min(A[END], B[END])`
7. 리스트를 어떻게, 언제까지 traversing 것인가?
```
# a. exit condition: 리스트들의 index(혹은 포인터) 중, 어느 하나가 length를 넘어설 경우
# b. index를 증가시키는 방법은 아래와 같다 (i = index of A, j = index of B)
if A[[i]END] < B[j][END]: i+=1
else: j += 1

Why? 
list는 이미 START를 기준으로 정렬되어 있는 상태이고
한 interval에 여러개의 intersection이 존재할 수 있음

       v1        v2   v3
A : |--A1--|    |---A2----| |--| ...
B :   |-B1-| |-B2-| |-B3-| ....

위와 같이 v2, v3과 같이 하나의 A의 interval에서  intersection 두 개가 나오는 경우,
A2 interval을 여러번 참조해야하고 B2,B3,Bn에 대해 A2와 비교할 수 있어야 함
따라서  interval의 END를 보고 작은 쪽의 index를 증가시켜줘야함
```

## My Solution
``` python
# Runtime: 128 ms, faster than 69.72% of Python online submissions for Interval List Intersections.
# Memory Usage: 12.5 MB, less than 53.98% of Python online submissions for Interval List Intersections.

class Solution(object):
    def intervalIntersection(self, A, B):
        result = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            overlap_a = A[i][0] >= B[j][0] and A[i][0] <= B[j][1]
            overlap_b = B[j][0] >= A[i][0] and B[j][0] <= A[i][1]

            if overlap_a or overlap_b:
                result.append([
                    max(A[i][0], B[j][0]),
                    min(A[i][1], B[j][1])
                ])
    
            if B[j][1] < A[i][1]:
                j += 1
            else:
                i += 1
        return result
```


## Compare: Runtime
- 알고리즘 자체는 크게 다를 게 없음
- <details><summary> code </summary><pre>

  ``` python
  # 104 ms submission
  class Solution(object):
      def intervalIntersection(self, A, B):
          i, j = 0, 0
          res = []
          while i<len(A) and j<len(B):
              a, b = A[i], B[j]
              if a.end < b.start: i += 1
              elif b.end < a.start: j += 1
              elif a.end >= b.end:
                  b.start = max(a.start, b.start)
                  res.append(b)
                  j += 1
              else:
                  a.start = max(a.start, b.start)
                  res.append(a)
                  i += 1
          return res
  ```
  </pre></details>
  
## Compare: Memory
- 사실 어떤 점에서 아래 코드가 더 이득인지 잘 모르겠다.
- <details><summary> code </summary><pre>

  ``` python
  # 12124 KB
  class Solution(object):
    def intervalIntersection(self, A, B):
        if len(A) == 0 or len(B) == 0:
            return []
        p1 = 0
        p2 = 0
        raw = []
        while p1 < len(A) and p2 < len(B):
            itvA = A[p1]
            itvB = B[p2]
            a = max(itvA[0], itvB[0])
            b = min(itvA[1], itvB[1])
            if a <= b:
                raw.append([a, b])
            if itvA[1] < itvB[1]:
                p1 += 1
            elif itvA[1] > itvB[1]:
                p2 += 1
            else:
                p1 += 1
                p2 += 1
        if len(raw) == 0:
            return []
        merged = [raw[0]]
        for itv in raw:
            if itv[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], itv[1])
            else:
                merged.append(itv)
        return merged
  ```
  </pre></summary>
