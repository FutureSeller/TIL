## Problem
Given a linked list, rotate the list to the right by k places, where k is non-negative.

## How to Solve
0. 조건: k > 0
1. 사전에 거를 것: [], [1], k == 0
2. list 전체 길이를 구하고, cyclic list로 만듬
3. cyclic하기 때문에 k rotate == k % len(list) right rotate
4. cyclic하기 때문에 len(list) - (k % len(list)) -1 이 시작위치가됨

## My Solution
``` python
# Runtime: 24 ms, faster than 71.98% of Python online submissions for Rotate List.
# Memory Usage: 11.8 MB, less than 49.62% of Python online submissions for Rotate List.

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k < 1:
            return head

        count = 1
        current = head

        while current.next:
            current = current.next
            count += 1

        current.next = head
        mod = k % count

        current = head
        for i in range(count - mod -1):
            current = current.next

        head = current.next
        current.next = None

        return head
```

## Compare: Runtime
- <details><summary> code </summary><pre>

  ``` python
  # sample 4 ms submission
  class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1
        tail.next = head

        new_tail = head
        for i in xrange(n - 1 - k % n):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head
  ```
  </pre></summary>

## Compare: Memory
- <details><summary> code </summary><pre>

  ``` python
  # sample 11464 kb submission
  class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
                return head

        size = 0
        p = head
        while p:
            p = p.next
            size += 1

        k = k % size
        while k > 0:
            head = self.helper(head)
            k -= 1

        return head

    def helper(self, head):
        if not head or not head.next:
            return head

        p = head
        while p.next and p.next.next:
            p = p.next

        newHead = p.next
        newHead.next = head
        p.next = None

        print(newHead.val)
        return newHead
  ```
  </pre></summary>
