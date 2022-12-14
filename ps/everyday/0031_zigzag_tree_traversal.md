# Zigzag Traversal

이진 트리가 주어지면 루트 노드부터 레벨별로 프린트 하시오. 
프린트 방식은 홀수 레벨은 왼쪽에서 오른쪽으로, 짝수 레벨은 오른쪽에서 왼쪽으로 프린트 하시오. 루트노드는 레벨 1입니다. 예제를 보시오.

```
   1
  / \
 2   3
/ \ / \
4 5 6 7

프린트: 1, 3, 2, 4, 5, 6, 7
```

```javascript
function solve(input) {
  const result = []

  let start = 0
  let end = 1
  let level = 0

  while (start < input.length) {
    if (level % 2) {
      result.push.apply(result, input.slice(start, end).reverse())
    } else {
      result.push.apply(result, input.slice(start, end))
    }
    level += 1
    start = end
    end = end * 2 + 1
  }

  return result.filter(Boolean)
}

const data = [
  { input: [1,2,3,4,5,6,7], expected: [1,3,2,4,5,6,7] },
  { input: [1,undefined,3], expected: [1,3] },
  { input: [1,undefined,undefined,4,5,6,7,8,9], expected: [1,4,5,6,7,9,8] }
]

data.forEach(({ input, expected }) => {
  const actual = solve(input)
  if (actual.join(',') !== expected.join(',')) {
    throw new Error('wrong answer')
  }
})

```
