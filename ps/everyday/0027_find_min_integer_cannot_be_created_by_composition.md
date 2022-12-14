# Find the smallest positive integer that cannot be created by adding elements in the array

정렬된 양수(positive integer) 배열이 주어지면, 배열 원소들의 합으로 만들수 없는 가장 작은 양수를 구하시오.

단, 시간복잡도는 O(n) 이여야 합니다.


Given an array of positive integers, find the smallest positive integer that cannot be created by adding elements in the array.

```
input: [1, 2, 3, 8]
output: 7
```

```javascript
function solve(input) {
  let min = 1

  for (const value of input) {
    if (value > min) {
      break
    } else {
      min += value
    }
  }

  return min
}


const data = [
  { input: [], expected: 1 },
  { input: [2], expected: 1 },
  { input: [1], expected: 2 },
  { input: [1,2,3,8], expected: 7 },
  { input: [1,1,2,3,8], expected: 16 },
]

data.forEach(({ input, expected }) => {
  const actual = solve(input)
  if (actual !== expected) {
    throw new Error('wrong answer')
  }
})

```
