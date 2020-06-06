## Problem
Given an array nums and a value val, 
remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. 
It doesn't matter what you leave beyond the new length.


## How to Solve
- val와 다른 조건일 때, index를 증가시키며 해당 값을 저장
- 나머지 값이 어찌됐든 무시. 어차피 리턴되는 length를 기준으로 문제 채점 시 slice해줌

## My Solution
``` python
# Runtime: 16 ms, faster than 91.29% of Python online submissions for Remove Element.
# Memory Usage: 11.8 MB, less than 28.57% of Python online submissions for Remove Element.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        non_duplicated = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[non_duplicated] = nums[i]
                non_duplicated += 1
        return non_duplicated
```
