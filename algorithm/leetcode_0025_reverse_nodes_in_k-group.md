## Problem
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

```
Example: Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:
- Only constant extra memory is allowed.
- You may not alter the values in the list's nodes, only nodes itself may be changed.
```

## How to Solve
0. 주어진 조건: k는 positive integer, min = 1, max = len(list)
1. k가 min(=1)일 경우, group이 자기자신이므로 list를 그대로 반환
2. 예시: k개의 list를 reverse한다고 가정 (leetcode_206 사용)
```
input: k = 2, list=(1 -> 2 -> 3 -> 4 -> 5 -> NULL)

[Step 0]. Initial State
-------------------------------
None     1 -> 2 -> 3 -> 4 -> 5
^        ^                   |
previous current          None
-------------------------------


[Step 1]. k=2만큼만 reverse함
-------------------------------
Step 0's current
  |        Step 0's previous
  ---      |
     |     |
2 -> 1 -> None
^
previous
           3 -> 4 -> 5 -> None
           ^
           current
-------------------------------

[Step 2]. 쪼개진 두개의 list를 연결해야함
-------------------------------
  Step 0's current
     |
2 -> 1 ----|
^          |
previous   |
           3 -> 4 -> 5 -> None
           ^
           current
------------------------------
- step0의 current를 저장해놔야 함. reversed된 sublist의 마지막 노드 
- reversed된 sublist의 마지막 노드의 next -> Step 2's current

[Step 3]. previous 이동
-------------------------------
2 -> 1 ----|
     ^     |
previous   |
           3 -> 4 -> 5 -> None
           ^
           current
-------------------------------
- 다음 reverse할 sublist를 기준으로 previous는 이미 reversed된 sublist의 마지막 노드

[Step 4]. Step 1, 2 반복
-------------------------------
         Step 3's current
                |
2 -> 1 ----|    |
           4 -> 3 ----|
                      5 -> None
           ^          ^
           previous   current
-------------------------------

[Step 5]. 남은 item의 갯수가 k보다 작으므로 반환
```

## My Solution
``` python
# Runtime: 20 ms, faster than 100.00% of Python online submissions for Reverse Nodes in k-Group.
# Memory Usage: 13.4 MB, less than 42.65% of Python online submissions for Reverse Nodes in k-Group

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1 or head is None: return head
        count = 0
        current = head
        while current:
            current = current.next
            count += 1
        
        current, previous = head, None
        while True:
            sublist_start = previous
            sublist_end = current
            if count < k: 
                break
            i = 0
            while current and i < k:
                next = current.next
                current.next = previous
                previous = current
                current = next
                i += 1
                count -= 1
            if sublist_start:
                sublist_start.next = previous
            else:
                head = previous
            sublist_end.next = current
            if current is None: 
                break
            previous = sublist_end
        return head
```

## Compare: Runtime
- <details><summary> code </summary><pre>

  ``` python
  # sample 20 ms submission
  class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
        if not head.next:
            return head

        pointer = a = head
        first = 1
        previous = pointer
        while pointer:
            ans,next_start = self.reverse(pointer,k)
            if first == 1 :
                final_ans = ans
                first = 0
            else:
                previous.next = ans
            previous = pointer
            pointer = next_start

        return final_ans

    def reverse(self,a,k):
        count = 0
        r = a
        while r and count < k:   # use r to locate the range
            r = r.next
            count += 1
        print(count,"count")
        print(k,"k")
        if count == k:
            first = a
            second = a.next
            a.next = None
            while k > 1:
                third = second.next
                second.next = first
                first = second
                second = third
                k = k - 1

            return first,second
        else:
            return a,r
  ```
  </pre></summary>

## Compare: Memory
- <details><summary> code </summary><pre>

  ``` python
  # sample 13032 kb submission 
  class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next
  ```
  </pre></summary>
