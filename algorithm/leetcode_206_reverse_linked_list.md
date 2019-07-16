## Problem
Reverse a singly linked list.

## How to Solve
1. 이전 노드, 현재 노드,  다음 노드를 가르키는 포인터 필요
2. 현재 노드의 next를 이전 노드로 링크
3. 이전 노드를 현재 노드로 옮김
4. 현재 노드를 다음 노드로 옮김

## My Solution
``` python
# Runtime: 20 ms, faster than 89.87% of Python online submissions for Reverse Linked List.
# Memory Usage: 13.5 MB, less than 76.98% of Python online submissions for Reverse Linked List.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
```

## Compare: Runtime
- 사실 어떤 차이가 있는지 모르겠음
- <details><summary> code </summary><pre>

  ``` python
  # sample 4 ms submission
  class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        prev = None
        curr = head
        
        while curr is not None:
            next_node = curr.next
            
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
  ```
  </pre></summary>

## Compare: Memory
- 사실 이것도 무슨 차이인지 잘 모르겠음
- <details><summary> code </summary><pre>

  ``` python
  # sample 13272 kb submission
  class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head

        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_

        return prev
  ```
  </pre></summary>
