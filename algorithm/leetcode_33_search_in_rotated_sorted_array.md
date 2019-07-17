## Problem
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

```
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

## How to Solve
0. 조건
```
a. runtime : O(log n) --> binary search
b. 기존에 오름차순 정렬 된 것이, rotated 된 것
```
1. len(array) < 1: return -1
2. binary search: (not rotated) sorted array
```
target: 5
input: | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
         ^           ^           ^
        low         mid         high

a. array[mid] == target: return mid
b. target이 low와 mid 사이에 위치할 경우
  - 왼쪽 subarray만 탐색하면 되므로 high = mid - 1
c. 1의 반대 상황
  - 오른쪽 subarray만 탐색하면 되므로 low = mid + 1
```
3. binary search: (rotated) sorted array
```
target: 5
input: | 4 | 5 | 6 | 0 | 1 | 2 | 3 |
         ^           ^           ^
        low         mid         high

a. array[mid] == target: return mid
b. array[low]와 array[mid] 값 비교가 선행되어야함
- rotate 되어있어 array[mid]가 더 작은 값일 수 있음
c. array[low] <= array[mid]: 
  - low --> mid에 해당하는 subarray는 오른차순 정렬된 상태
  - target이 low와 mid 사이에 위치할 경우: high = mid - 1
  - target이 low와 mid 사이에 없을 경우: low = mid + 1
d. array[low] > array[mid]: rotate된 상태
  - mid --> high에 해당하는 subarray는 오름차순 정렬된 상태
  - target이 mid와 high 사이에 위치할 경우: low = mid + 1
  - target이 범위 밖에 있을 경우: high = mid - 1
e. while문을 빠져나오게 되는 조건: low < high
  - low > high일 수 없고, low == high인 경우밖에 없음
  - low나 high 둘 중 하나가 고정된 상태로 나머지 값이 +1 혹은 -1되기 때문
  - 따라서, low가 high 값을 넘어설 순 없음
```


## My Solution
``` python
# Runtime: 28 ms, faster than 74.60% of Python online submissions for Search in Rotated Sorted Array.
# Memory Usage: 11.8 MB, less than 76.68% of Python online submissions for Search in Rotated Sorted Array.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 1: return -1

        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2

            if nums[mid] == target: return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target and nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target and nums[high] >= target:
                    low = mid + 1
                else:
                    high = mid -1
                    
        if nums[high] == target:
            return high
        else:
            return -1
```

## Compare: Runtime
- <details><summary> code </summary><pre>

  ``` python
  # sample 8 ms submission
  class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        revised binary search
        """
        l, r = 0, len(nums) - 1

        while l<=r:
            middle = (l+r)/2
            if nums[middle] == target:
                return middle

            if nums[middle] >= nums[l]:
                if target >= nums[l] and target <= nums[middle]:
                    r = middle - 1
                else:
                    l = middle + 1
            else:
                if target <= nums[r] and target >= nums[middle]:
                    l = middle + 1
                else:
                    r = middle - 1
        return -1
  ```
  </pre></details>
  
## Compare: Memory
- <details><summary> code </summary><pre>

  ``` python
  # sample 11604 kb submission
  class Solution:
    # @param {integer[]} numss
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
  ```
  </pre></summary>
