주어진 정수를 2진법으로 나타내었을때 1의 갯수를 리턴하시오.

Given an integer, count number of 1s in binary representation of an integer.

시간 복잡도: O(log n)


```
input: 6 // 110
output: 2

input: 13 // 1101
output: 3
```

```javascript
const solveUsingToString = (value) => value.toString(2).split('').filter(v => v === '1').length

function solve(input) {
  let count = 0
  while (input > 0) {
    count += input & 1
    input = input >>> 1
  }
  return count
}

const N = 10000
for (let i = 0; i < N; i++) {
  const actual = solve(i)
  if (actual !== solveUsingToString(i)) {
    throw new Error('wrong answer')
  }
}
```
