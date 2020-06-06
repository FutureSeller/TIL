## Problem
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
```
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
```

## How to Solve
DFS 사용

## My Solution
```python
# Runtime: 24 ms, faster than 64.59% of Python online submissions for Binary Tree Level Order Traversal II.
# Memory Usage: 12.1 MB, less than 94.40% of Python online submissions for Binary Tree Level Order Traversal II.
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        res = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res
```

## Compare: Runtime
- <details><summary> code </summary><pre>

  ``` python
  # sample 8 ms submission
  from collections import deque

  class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        order = []
        if root is None:
            return order
        
        que = deque()
        que.append((root, 1))
        
        while len(que):
            node, depth = que.popleft()
            
            if node is not None:
                if len(order) < depth:
                    order.append([])
                                 
                
                order[depth-1].append(node.val)

                que.append((node.left, depth+1))
                que.append((node.right, depth+1))
        
        order.reverse()
        return order
  ```
  </pre></details>
  
## Compare: Memory
- <details><summary> code </summary><pre>

  ``` python
  # sample 11912 kb submission
  class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        cur_level = [root]
        res = []
        while cur_level:
            nxt_level = []
            tmp_res = []
            for node in cur_level:
                if node.left:
                    nxt_level.append(node.left)
                if node.right:
                    nxt_level.append(node.right)
                tmp_res.append(node.val)
            cur_level = nxt_level
            res.append(tmp_res)
        return res[::-1]
  ```
  </pre></summary>