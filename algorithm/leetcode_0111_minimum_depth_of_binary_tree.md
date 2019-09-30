## Problem
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

```
Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
```


## How to Solve
TBD

## My Solution
```python
# Runtime: 28 ms, faster than 93.37% of Python online submissions for Minimum Depth of Binary Tree.
# Memory Usage: 14.7 MB, less than 43.83% of Python online submissions for Minimum Depth of Binary Tree.
class Solution(object):
    def minDepth(self, root):
        if root is None: return 0
        queue = [(root, 1)]
        while queue:
            (node, level) = queue.pop(0)
            if node:
                if node.left is None and node.right is None:
                    return level
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        return -1
```

## Compare: Runtime
- <details><summary> code </summary><pre>

  ``` python
  # sample 16 ms submission
  class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))

  ```
  </pre></details>
  
## Compare: Memory
- <details><summary> code </summary><pre>

  ``` python
  # sample 14204 kb submission
  class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        stack = []
        stack.append((root, 1))
    
        while stack:
            node, cur_depth = stack.pop(0)
            
            if not node.left and not node.right:
                return cur_depth
            
            if node.left:
                stack.append((node.left, cur_depth + 1))
            
            if node.right:
                stack.append((node.right, cur_depth + 1))
        
  ```
  </pre></summary>