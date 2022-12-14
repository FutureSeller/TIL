1~N 까지 있는 정수 배열에 원소 하나가 없어졌습니다. 없어진 원소의 값을 구하시오.

Given an integer array of 1~N except one number, find the missing integer.

```javascript
function solve(input) {
  const totalSum = ((input.length + 1) * (input.length + 2)) / 2
  const reduced = input.reduce((acc, cur) => cur + acc, 0)
  return totalSum - reduced
}

const data = [
  { input: [1,2,3,4,5,6,8,9], expected: 7 }
]

data.forEach(({ input, expected }) => {
  const actual = solve(input)
  if (actual !== expected) {
          console.log(actual, expected)
    throw new Error('wrong answer')
  }
})
```
