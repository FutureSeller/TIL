## Problem
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

```
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
```

## How to Solve
1. 
2. reverse_linked_list.md와 동일
```
1. 이전 노드, 현재 노드,  다음 노드를 가르키는 포인터 필요
2. 현재 노드의 next를 이전 노드로 링크
3. 이전 노드를 현재 노드로 옮김
4. 현재 노드를 다음 노드로 옮김
```

## My Solution
``` python
# Runtime: 16 ms, faster than 86.07% of Python online submissions for Reverse Linked List II.
# Memory Usage: 12 MB, less than 52.16% of Python online submissions for Reverse Linked List II.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n: return head
        distance = n - m + 1
        if m == 1:
            return self.reverse(head, distance)
        else:
            hptr = head
            while m > 1:
                prev = head
                head = head.next
                m -= 1
            reversed = self.reverse(head, distance)
            prev.next = reversed
            return hptr

    def reverse(self, head, distance):
        end = head
        prev = None
        while distance > 0:
            next = head.next
            head.next = prev
            prev = head
            head = next
            distance -= 1
        next = head
        end.next = next
        return prev
```

## Compare: Runtime
- 카운팅할때 '-' 보다 '+'를 사용하는게 속도측면에서 큰 이득이 있는 것 같음
- <details><summary> code </summary><pre>

  ``` python
  # sample 4 ms submission
  class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # corner case
        if not head or not head.next or m == n: return head 
        
        count = 1
        dummy = ListNode(None)
        dummy.next = head
        cur, pre = head, dummy 
        
        while count <= m - 1:
          count += 1
          cur = cur.next
          pre = pre.next
        
        store1, store2 =  pre, cur  # m-1, m
        cur = cur.next # m+1
        pre = pre.next # m
        count += 1
        
        while count <= n:
          temp =  cur.next
          cur.next = pre
          pre, cur = cur, temp
          count +=  1
        store2.next = cur 
        store1.next = pre
          
        return dummy.next
  ```
  </pre></summary>

## Compare: Memory
- <details><summary> code </summary><pre>

  ``` python
  # sample 11524 kb submission
  class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(None)
        start.next = head
        headm = head
        headm_prev = start
        for i in range(m-1):
            headm_prev = headm
            headm = headm.next
        curr = headm.next
        currhead = headm
        pm = m
        while pm < n:
            print(pm, currhead.val, curr.val)
            curr_next = curr.next
            curr.next = currhead
            currhead = curr
            curr = curr_next
            pm += 1
        headm.next = curr
        headm_prev.next = currhead
        return start.next
  ```
  </pre></summary>
