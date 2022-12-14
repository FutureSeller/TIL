## Problem
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

## How to Solve
0. 조건
```
a. without extra space: space complexity O(1)
b. appear twice and others apper once! 두 번 혹은 한 번만 나옴
```
1. (n%N) -1
```
1%8-1 : 0
2%8-1 : 1
...
8%8-1 : -1 => python 에서 list[-1]은 last elem
```
2. 현재 Length만큼 더하면, 한 번 나올경우 최댓값 2 x Length
3. 즉, 2 x Length보다 크면 두 번 나온 것
4. 3의 경우, counter로 증가시킴. nums[:counter]만큼 반환

## My Solution
```python
# Runtime: 328 ms, faster than 84.94% of Python online submissions for Find All Duplicates in an Array.
# Memory Usage: 18.8 MB, less than 56.30% of Python online submissions for Find All Duplicates in an Array.

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        for n in nums:
            nums[n%length-1] += length
        w = 0
        for i in range(length):
            if nums[i] > 2*length:
                nums[w] = i + 1
                w += 1
        return nums[:w]
```

## Compare: Runtime
- extra space를 사용한 거 아닌가?
- <details><summary> code </summary><pre>

  ``` python
  # sample 300 ms submission
  class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        unique = set()
        duplicates = []
        for num in nums:
            if num not in unique:
                unique.add(num)
            else:
                duplicates.append(num)
        return duplicates
  ```
  </pre></details>
  
## Compare: Memory
- <details><summary> code </summary><pre>

  ``` python
  # sample 17460 kb submission 
  class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = 0
        l = len(nums)
        while pos < l:
            if nums[pos] < 0:
                pos = pos + 1
                continue
            val = nums[pos]
            if nums[val - 1] < 0:
                if nums[val - 1] == -1:
                    yield val
                nums[val - 1] -= 1
                pos = pos + 1
                continue
            if pos != val - 1:
                nums[pos] = nums[val - 1]
                nums[val - 1] = -1
            else:
                nums[val - 1] = -1
  ```
  </pre></summary>
