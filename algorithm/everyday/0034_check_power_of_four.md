주어진 정수가 4의 거듭제곱인지 확인하시오.

Given an integer, check if it is a power of 4.

```javascript
function solve(input) {
  return !!input && !(input & 1) && !(input & 0xAAAAAAAA)
}

const data = [
  { input: 4, expected: true },
  { input: 16, expected: true },
  { input: 32, expected: false },
  { input: 2, expected: false },
  { input: 15, expected: false },
  { input: 17, expected: false },
  { input: 1, expected: false },
  { input: 0, expected: false },
]

data.forEach(({ input, expected }) => {
  const actual = solve(input)
  if (actual !== expected) {
    throw new Error('wrong anwser')
  }
})
```
