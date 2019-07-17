## Problem
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.
You may assume no duplicate exists in the array.

## How to Solve
0. 이상한 점
```
leetcode_33 문제에서와 동일한 조건인데, 이해가 안되는 testcase에 의해 fail했었음
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. 

- 문제의 tc [3,2,1]
- 어떻게 rotate해야 [1,2,3] -> [3,2,1]이 되는 걸까?
- [1,2,3]으로 가능한 rotate의 경우의 수: [1,2,3], [2,3,1], [3,1,2]
```

1. 찜짐함을 뒤로 하고 binary search 이용
```
a. 이미 오름차순으로 정렬되어있는 경우: return nums[0]
b. subarray의 오른쪽만 보고, 어느쪽으로 오름차순 정렬이 되어있는지 확인
: nums[m] <= nums[h]: 우측이 오름차순 (m=h)로 놓고 다음 턴에 좌측 subarray만 봄
| 4 | 5 | 1 | 2 | 3 |   
  l       m       h

: nums[m] > nums[h]: 좌측이 오름차순, 다음턴에 우측에 subarray만 봄
| 4 | 5 | 6 | 1 | 2 |   
  l       m       h
```


## My Solution
``` python
# Runtime: 16 ms, faster than 99.63% of Python online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 11.9 MB, less than 78.15% of Python online submissions for Find Minimum in Rotated Sorted Array.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return nums[-1]

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            if nums[lo] <= nums[hi]:
                return nums[lo]
            else:
                mid = (lo + hi) / 2
                if nums[mid] <= nums[hi]:
                    hi = mid
                else:
                    lo = mid + 1
```

## Compare: Runtime
- <details><summary> code </summary><pre>

  ``` python
  # sample 12 ms submission
  class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        low, high = 0, len(nums) - 1
        mid = (low + high) / 2

        while low < high:
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
            mid = (low + high) / 2

        return nums[mid]
  ```
  </pre></details>
  
## Compare: Memory
- <details><summary> code </summary><pre>

  ``` python
  # sample 11664 kb submission
  class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return min(nums)
        mid = len(nums) // 2
        if nums[0] > nums[mid]:
            return self.findMin(nums[:mid+1])
        if nums[mid+1] > nums[-1]:
            return self.findMin(nums[mid+1:])
        if nums[0] < nums[mid+1]:
            return nums[0]
        return nums[mid+1]
  ```
  </pre></summary>
