이진탐색트리안에 X보다 크고 Y보다 작은 모든 노드 값을 프린트 하시오.

Given a binary search tree, print all node values that are bigger than X and smaller than Y.

```javascript
// https://www.digitalocean.com/community/tutorials/js-binary-search-trees
class Node {
  constructor(val) {
    this.val = val
    this.right = null
    this.left = null
  }
}

class BST {
  constructor() {
    this.root = null
  }

  add(val) {
    const newNode = new Node(val)
    if (!this.root) {
      this.root = newNode
      return this
    };
    let current = this.root

    const addSide = side => {
      if (!current[side]) {
        current[side] = newNode
        return this
      }
      current = current[side]
    }

    while (true) {
      if (val === current.val) {
        return this
      }
      if (val < current.val) addSide('left')
      else addSide('right')
    }
  }
}


function solve(input, x, y, result) {
  if (input === null) return

  const { val } = input

  if (x < val) {
    solve(input.left, x, y, result)
  }

  if (y > val) {
    solve(input.right, x, y, result)
  }


  if (x <= val && y >= val) {
    result.push(val)
  }

  return result
}

const data = [
  {
    input: [5, 2, 12, 1, 3, 9, 21, 19, 25],
    x: 10,
    y: 20,
    expected: [12, 19]
  },
  {
    input: [4, 8, 12, 20, 22],
    x: 1,
    y: 10,
    expected: [4, 8]
  },
  {
    input: [4, 8, 12, 20, 22],
    x: 23,
    y: 24,
    expected: []
  }
]

data.forEach(({ input, x, y, expected }) => {
  const tree = new BST()
  input.forEach(value => tree.add(value))

  const actual = solve(tree.root, x, y, [])
  if (JSON.stringify(actual.sort()) !== JSON.stringify(expected)) {
    throw new Error('wrong answer')
  }
})
```
