## Problem
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

```
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
```

## How to Solve

## My Solution
```python
# Runtime: 48 ms, faster than 35.91% of Python online submissions for Average of Levels in Binary Tree.
# Memory Usage: 16.4 MB, less than 52.41% of Python online submissions for Average of Levels in Binary Tree.

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None: return []
        res = []
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            if node:
                if len(res) <= level:
                    res.insert(level, [])
                res[level].append(node.val)
                queue.append((node.right, level + 1))
                queue.append((node.left, level + 1))
        res = map(lambda x: float(sum(x))/len(x), res)
        return res
```

## Compare: Runtime
- <details><summary> code </summary><pre>

  ``` python
  # sample 24 ms submission
  class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from collections import deque
        res = []
        queue = deque()
        if not root:
            return res
        queue.append(root)
        
        while queue:
            size = len(queue)
            levelsum = 0.0
            for _ in range(size):
                currentNode = queue.popleft()
                levelsum += currentNode.val
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            res.append(levelsum/size)
        return res
  ```
  </pre></details>
  
## Compare: Memory
- <details><summary> code </summary><pre>

  ``` python
  # sample 16084 kb submission
  class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return 0
        else:
            nodes=[root]
            avs=[root.val]
            while nodes!=[]:
                nodes=[y for x in nodes for y in (x.left, x.right) if y ]
                if nodes!=[]:
                    
                    a=float(sum([y.val for y in nodes]))/float(len(nodes))
                    avs.append(a)
            return avs
  ```
  </pre></summary>