## Problem
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

## How to Solve
0. 주어진 조건: intervals는 start를 기준으로 이미 정렬되어 있다.
1. 이번엔 반대로, Merge 할 수 없는 조건을 생각해보자.
```
a. newInterval의 start가 intervals[idx]의 end보다 클 때 (|--- intervals[idx] ---| |--- newIntervals ---|)
b. newInterval의 end가 intervals[idx]의 start보다 작을 때 (|---newIntervals---| |--- intervals[idx] ---|)
c. a와 b를 제외하고 나머지 경우에 merge가 가능하다.
```
2. (1.a)의 interval은 merge된 결과의 좌측에 위치해야한다.
3. (1.b)의 interval은 merge된 결과의 우측에 위치해야한다.
4. 나머지의 경우, merge가 가능하므로 start와 end의 range를 키워나가면 됨. start = min(..), end = max(..)
5. 3-5-4의 list를 concat함

## My Solution
```python
# Runtime: 52 ms, faster than 98.77% of Python online submissions for Insert Interval.
# Memory Usage: 15.3 MB, less than 49.63% of Python online submissions for Insert Interval.

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        left = []
        right = []
        start = newInterval[0]
        end = newInterval[1]
        for idx in range(len(intervals)):
            l_start = intervals[idx][0]
            l_end = intervals[idx][1]
            if l_end < start:
                left.append(intervals[idx])
            elif l_start > end:
                right.append(intervals[idx])
            else:
                start = min(start ,l_start)
                end = max(end, l_end)
        return left + [[start,end]] + right
```

## Compare: Runtime
- <details><summary> code </summary><pre>

  ``` python
  # 40 ms submission
  class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not len(intervals):
            return [newInterval]
        ret = []
        affected = []
        cur = 0
        index_to_insert = -1
        while cur < len(intervals):
            if intervals[cur][1] < newInterval[0]:
                ret.append(intervals[cur])
            elif intervals[cur][0] <= newInterval[1]:
                if index_to_insert == -1:
                    index_to_insert = cur
                affected.append(intervals[cur])
            else:
                ret.append(intervals[cur])
            cur += 1
        
        merged_int = [0,0]
        merged_int[0] = min(affected[0][0], newInterval[0]) if affected else newInterval[0]
        merged_int[1] = max(affected[-1][1], newInterval[1]) if affected else newInterval[1]
        
        cur = 0
        total_unaffected = len(ret)
        while cur < len(ret):
            if ret[cur][0] > merged_int[1]:
                if cur > 0:
                    ret = ret[:cur] + [merged_int] + ret[cur:]
                else:
                    ret = [merged_int] + ret
                break
            cur += 1
        if cur == len(ret):
            ret += [merged_int]

        return ret
  ```
  </pre></details>
  
## Compare: Memory
- <details><summary> code </summary><pre>

  ``` python
  # 14944 kb submission
  class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        if len(intervals) == 0:
            return [newInterval]
        s = newInterval[0]
        t = newInterval[1]
        if s<=intervals[0][0] and t>=intervals[-1][1]:
            return [newInterval]
        if len(intervals) == 1:
            if intervals[0][0] > t:
                return [newInterval, intervals[0]]
            elif intervals[0][1] < s:
                return [intervals[0], newInterval]
            else:
                return [[min(s,intervals[0][0]), max(t,intervals[0][1])]]
        res = []
        i = 0
        while i < len(intervals):
            v = intervals[i]
            if v[1] < s: # 当前区间v直接添加入res
                res.append(v)
            else:
                if v[0] > t:
                    break
                s = min(v[0], s)
                t = max(v[1], t)
            i += 1
        res.append([s,t])
        res += intervals[i:]
        return res
  ```
  </pre></summary>
