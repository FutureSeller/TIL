## Problem
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? 
You may assume the returned list does not count as extra space.

## How to Solve
1. Cyclic Sort 사용
2. 현재 index에 해당하는 값이 원래 있어야할 위치에 있는 가를 확인
3.a. 없다면, swap 한 뒤 다시 2로 돌아감
3.b. 있다면, index 증가
4. 중복된 값이 있더라도, index가 증가하기 때문에 그 위치에 그대로 남음
5. 해당 array를 다시 돌면서 각 index 해당 값이 존재하는지 확인

## My Solution
```python
# Runtime: 380 ms, faster than 15.74% of Python online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 18.8 MB, less than 95.67% of Python online submissions for Find All Numbers Disappeared in an Array.

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        idx = 0
        while idx < len(nums):
            j = nums[idx] - 1
            if nums[idx] != nums[j]:
                nums[idx], nums[j] = nums[j], nums[idx]
            else:
                idx += 1
        res = []
        for idx in range(len(nums)):
            if nums[idx] != idx+1:
                res.append(idx+1)
        return res
```

## Compare: Runtime
- 아주 단순한 아이디어. list -> set -> list 이용
- <details><summary> code </summary><pre>

  ``` python
  # sample 292 ms submission
  class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return_list = list(range(1,len(nums)+1))
        for i in nums:
            return_list[i-1] = 0
        return_list = list(set(return_list))
        if 0 in return_list:
            return_list.remove(0)
        return return_list
  ```
  </pre></details>
  
## Compare: Memory
- <details><summary> code </summary><pre>

  ``` python
  # sample 17780 kb submission
  class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            if n > 0:
                while n > 0:
                    tmp = nums[n-1]
                    nums[n-1] = -1
                    n = tmp
        res = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                res.append(i+1)
        return res
  ```
  </pre></summary>
