## Problem
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
```
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
```

## How to Solve
Recursive, post-order traverse

## My Solution
```python

# Runtime: 24 ms, faster than 64.10% of Python online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 12.7 MB, less than 6.98% of Python online submissions for Binary Tree Level Order Traversal.

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        def helper(node, res, level):
            if node.left:
                helper(node.left, res, level+1)
            if node.right:
                helper(node.right, res, level+1)
            if node:
                try: res[level]
                except: res[level] = []
                res[level].append(node.val)

        if root is None: return []
        
        res = {}
        helper(root, res, 0)
        retval = []
        for (idx, val) in enumerate(res):
            retval.append(res[idx])
        return retval
```

## Compare: Runtime
- <details><summary> code </summary><pre>

  ``` python
  # sample 4 ms submission
  class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        solution = []
        treeDict = {}
        
        level = 0
        
        def traverse(node, level):
            try:
                treeDict[level]
            except:
                treeDict[level] = []
            if node:
                treeDict[level].append(node.val)
                traverse(node.left, level+1)
                traverse(node.right, level+1)
        
        traverse(root, 0)
        
        for level in treeDict:
            if treeDict[level] != []:
                solution.append(treeDict[level])
            
        return solution

  ```
  </pre></details>
  
## Compare: Memory
- <details><summary> code </summary><pre>

  ``` python
  # sample 11964 kb submission
  # Definition for a binary tree node.
  class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        values = []
        currentNodes = [root]
        nextNodes = []

        while len(currentNodes) or len(nextNodes) or len(values):
            if not len(currentNodes):
                currentNodes = nextNodes[:]
                nextNodes = []
                result.append(values)
                values = []
            node = currentNodes.pop(0)
            if node:
                values.append(node.val)
                nextNodes += [node.left, node.right]

        return result
  ```
  </pre></summary>