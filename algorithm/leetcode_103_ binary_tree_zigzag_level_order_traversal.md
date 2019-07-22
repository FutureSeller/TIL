## Problem
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

```
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
```

## How to Solve
TBD

## My Solution
```python
# Runtime: 16 ms, faster than 90.85% of Python online submissions for Binary Tree Zigzag Level Order Traversal.
# Memory Usage: 12.1 MB, less than 63.43% of Python online submissions for Binary Tree Zigzag Level Order Traversal.
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        res = []
        queue = [(root, 0)]
        while queue:
            (node, level) = queue.pop(0)
            if node:
                print (node.val, level)
            if node:
                if len(res) <= level:
                    res.insert(level, [])
                    
                if (level % 2) == 0:
                    res[level].insert(0, node.val)
                    
                else:
                    res[level].append(node.val)
                    
                queue.append((node.right, level + 1))
                queue.append((node.left, level + 1))
                                    
        return res
        
```

## Compare: Runtime
- <details><summary> code </summary><pre>

  ``` python
  # sample 4 ms submission
  class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def depth(root):
            if not root: return 0
            return 1 + max(depth(root.left), depth(root.right))
        def visit(root, d):
            if not root: return
            if d % 2:
                res[d] = [root.val] + res[d]
            else:
                res[d].append(root.val)
            visit(root.left, d+1)
            visit(root.right, d+1)
            return 
        
        res = [[] for _ in range(depth(root))]
        visit(root, 0)
        return res
  ```
  </pre></details>
  
## Compare: Memory
- <details><summary> code </summary><pre>

  ``` python
  # sample 11800 kb submission
  class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        leftToRight = True
        curLevel = [root]
        result = [[root.val]]
        
        
        while curLevel:
            curNodeValue = []
            nextLevel = []
            if leftToRight:
                for node in curLevel:   # curLevel should be reversed
                    if node.right:
                        nextLevel.append(node.right)
                        curNodeValue.append(node.right.val)
                    if node.left:
                        nextLevel.append(node.left)
                        curNodeValue.append(node.left.val)
                    
            else:
                for node in curLevel[::-1]:   # curLevel should be in order
                    if node.left:
                        nextLevel.append(node.left)
                        curNodeValue.append(node.left.val)
                    if node.right:
                        nextLevel.append(node.right)
                        curNodeValue.append(node.right.val)
            
            if curNodeValue:    
                result.append(curNodeValue)
            
            if leftToRight:
                curLevel = nextLevel
            else:
                curLevel = nextLevel[::-1]
                
            leftToRight = not leftToRight
            
        return result

  ```
  </pre></summary>