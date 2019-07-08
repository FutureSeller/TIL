## Problem
Given an array nums of n integers and an integer target, 
are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

## How to Solve
0. 조건
```
a. uniqueness: 중복된 quadruplet들이 없어야 함
b. a + b + c + d == target
```

1. two pointer: 2sum example
```
| - | - | - | - | - | - | - |
  ^                       ^
 left                   right

- 가정: input은 sorted array
- left, right의 방향을 강제할 수 있음
  - arr[left] + arr[right] == target: return [arr[left], arr[right]]
  - arr[left] + arr[right] > target: right -= 1
  - arr[left] + arr[right] < target: left += 1
```

2. two pointer: 3sum example
```
| - | - | - | - | - | - | - |
  ^       ^               ^
 base   left            right

- 가정: input은 sorted array
- base pointer를 그대로 두고, left와 right만 이동. 역시 방향을 강제할 수 있음
  - arr[base] + arr[left] + arr[right] == target: return [arr[base], arr[left], arr[right]]
  - arr[base] + arr[left] + arr[right] > target: right -= 1
  - arr[base] + arr[left] + arr[right] < target: left += 1

```

3. 1->2에서 base가 생겼듯이 기준점을 하나 씩 늘려가면 됨
4. Uniqueness. 중복 제거: 3sum example
```
| - | - | - | - | - | - | ...
  ^   ^   ^           ^
  a   b   k           c

- 가정: target = a + b + c, a == b == k ↔ a + b == b + k == a + k
- a 방문 시 a+b+x == target인 경우를 모두 찾음
- b 방문 시 a == b인지 확인 후, bypass

```


## My Solution
``` python
# Runtime: 812 ms, faster than 32.80% of Python online submissions for 4Sum.
# Memory Usage: 11.8 MB, less than 56.70% of Python online submissions for 4Sum.

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for idx in range(len(nums) - 3):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            summ = self.threeSum(nums[idx+1:], target - nums[idx])
            for s in summ:
                res.append([nums[idx]] + s)
        return res
                
    def threeSum(self, nums, target):
        res = []
        print (nums)
        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                found = nums[idx] + nums[left] + nums[right] - target
                if found == 0:
                    res.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                elif found > 0:
                    right -=1
                else:
                    left += 1
        return res         
```

## Compare: Runtime
- `take advantages of sorted`라는 부분이 인상적임
  - `target < nums[i] * N or target > nums[-1]*N`: (이미 정렬되어있기 때문에)
  - `target < nums[i]*4`: target이 될 수 있는 min보다 작음
  - `target > nums[-1]*4`: target이 될 수 있는  max보다 큼
- <details><summary> code </summary><pre>

  ``` python
  # sample 44 ms submission
  class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        for i in range(len(nums)-3):
            if  i!=0 and nums[i] == nums[i-1]:
                continue
            if target < nums[i]*4 or target > nums[-1]*4:  # take advantages of sorted list
                break
            target_for_3sum = target - nums[i]
            self.threeSum_withtarget(nums[i+1:], target_for_3sum, nums[i], results)
            # for res in res_3sum:
            #     results.append([nums[i]] + res)
        return results

    def threeSum_withtarget(self, nums, target, comb, res):
        # res = []
        N = len(nums)
        if N < 3: return
        # nums.sort() # already sorted


        for i in range(N-2): # j k for last

            new_target = target - nums[i]
            l, r = i+1, N-1
            if  i!=0 and nums[i] == nums[i-1]:
                continue
            if target < nums[i]*3 or target > nums[-1]*3:  # take advantages of sorted list
                break
            while l<r:
                cur_sum = nums[l] + nums[r]
                if cur_sum > new_target:
                    r -= 1 #move r
                elif cur_sum < new_target:
                    l += 1# move l
                else: # equal to target
                    res.append([comb, nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                    l += 1
        return
  ```
  </pre></summary>

## Compare: Memory
- fourSum에서 list를 안만드는 방법
- <details><summary> code </summary><pre>

  ``` python
  # sample 11500 kb submission
  class Solution(object):
    def fourSum(self, nums, tg):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()

        return self.n_sum(nums, tg, 4)

    def n_sum(self, nums, tg, N):
        res = []
        if N == 2:
            l, r = 0, len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s == tg:
                    res.append([nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s > tg:
                    r -= 1
                else:
                    l += 1
        else:
            for i, n in enumerate(nums):
                if i and nums[i-1] == n:
                    continue
                if (i and nums[i-1] * N > tg):
                    break
                res += [[n]+r for r in self.n_sum(nums[i+1:], tg-n, N-1)]
        return res
  ```
  </pre></summary>
