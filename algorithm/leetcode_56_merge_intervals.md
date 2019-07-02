## Problem
Given a collection of intervals, merge all overlapping intervals.

## How to Solve
0. 주어진 Input의 lenght가 2보다 작으면 merge할 필요가 없다. (Input의 type은 [[int, int]])
1. Input이 정렬되어있다는 보장이 없으므로, START를 기준으로 sorting 한다.
2. START를 기준으로 정렬된 상태에서 바로 앞뒤의 Interval들의 배치는 다음과 같다.
  ```
1. Merge 될 수 없음 (1, 2의 위치는 바뀔 수 없음, START를 기준으로 정렬했기 때문)
  | --- 1 --- |  | - 2 - |
  
2. Merge 될 수 있음
  2-1. Merge 될 수 있음 (1이 2를 포함할 때)
    | --- 1 --- |
      | - 2 - |
    
  2-2. Merge 될 수 있음 (1.end == 2.start)
    | --- 1 --- | - 2 - |
  
  2-3. Merge 될 수 있음 (1.start <= 2.start  && 1.end >= 2.start)
    | --- 1 --- |
            | - 2 - |
```

3. 2의 배치들을 기준으로 Merge 된 Interval을 구하는 방법은 다음과 같다.
```
1. Input을 길이만큼 순회할 때, START를 기준으로 정렬했기 때문에 [1].start는 [2].start보다 항상 작거나 같다. (START는 [1].start로 고정)
2. Merge가 될 수 있는 경우일 때, END는 max([1].end, [2].end)가 된다.
```


## My Solution
``` python
# Runtime: 68 ms, faster than 80.70% of Python online submissions for Merge Intervals.
# Memory Usage: 14.1 MB, less than 79.22% of Python online submissions for Merge Intervals.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        START, END = 0, 1
        if len(intervals) < 2:
            return intervals
        result = []
        intervals.sort(key=lambda x: x[START])
        tmp = intervals[0]
        for idx in range(1, len(intervals)):
            inst = intervals[idx]
            if tmp[END] >= inst[START] and tmp[START] <= inst[START]:
                tmp[END] = max(inst[END], tmp[END])
            else:
                result.append(tmp)
                tmp = inst
        result.append(tmp)
        return result
```

## Compare: Runtime
- 알고리즘 자체는 크게 다르지 않음.
- <details><summary> code </summary><pre>

  ``` python
  class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        if intervals == []:
            return []
        start = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals:
            if interval[0] > end:
                merged.append([start, end])
                start = interval[0]
                end = interval[1]
            else:
                if interval[1] > end:
                    end = interval[1]
        merged.append([start, end])
        return merged
  ```
  </pre></details>
  
## Compare: Memory
- 추가적인 변수 선언 없이, 주어진 Input을 그대로 사용 + del을 사용해 merge된 부분 삭제
- <details><summary> code </summary><pre>

  ``` python
  class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        i=0
        while i<len(intervals):
            if i+1<len(intervals) and intervals[i][1]>=intervals[i+1][0]:
                intervals[i][1]=max(intervals[i][1],intervals[i+1][1])
                del intervals[i+1]
                continue
            i+=1
        return intervals
  ```
  </pre></summary>
