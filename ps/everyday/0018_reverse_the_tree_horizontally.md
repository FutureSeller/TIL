# Reverse the tree horizontally
이진 트리를 루트 노드를 기준으로 좌우반전 하시오.

이 문제는 구글이 Homebrew 창시자에게 낸 문제로 유명합니다.

Given a binary tree root node, reverse the tree horizontally. 

``` javascript
const clone = (node) => JSON.parse(JSON.stringify(node))

const printTreebyLevelOrder = (node) => {
  const result = []
  const queue = [node]
  while (queue.length) {
    const size = queue.length
    for (let i=0; i<size; ++i) {
      const temp = queue.shift()
      if (temp) {
        result.push(temp.value)
        queue.push(temp.left)
        queue.push(temp.right)
      }
    }
  }
  return result
}

const reverse = (node) => {
  if (!node) { return null }
  const temp = clone(node)
  let left = null
  let right = null
  if (temp.left) {
    left = reverse(temp.left)
  }
  if (temp.right) {
    right = reverse(temp.right)
  }
  temp.left = right
  temp.right = left
  return temp
}

// Tree 만드는 코드 짜기 귀찮아서 manual하게 트리 만듬
const data = [{
  input: {
    value: 1,
    left: {
      value: 2,
      left: { value: 4 },
      right: { value: 5 }
    },
    right: {
      value: 3,
      left: { value: 6 },
      right: { value: 7 }
    }
  },
  expected: '1,3,2,7,6,5,4'
}]

data.forEach(({input, expected}) => {
  const actual = reverse(input)
  const obj2Arr = printTreebyLevelOrder(actual)
  if (obj2Arr.join(',') !== expected) {
    new Error('wrong answer')
  }
})
```