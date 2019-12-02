## arr[0]부터 시작하여 모든 원소를 들린 다음 다시 arr[0]로 도착할 수 있는지 찾으시오

정수 배열 arr이 있습니다. arr안의 각 원소의 값은 다음 원소의 인덱스입니다. 
이렇게 서로 이어지는 원소들의 배열이 있을때, 
arr[0]부터 시작하여 모든 원소를 들린 다음 다시 arr[0]로 도착할 수 있는지 찾으시오.

단, 시간복잡도는 O(n), 공간복잡도는 O(1).

```
예제)

Input: [1, 2, 4, 0, 3]
Output: True
// 1 -> 2 -> 4 -> 3 -> 0 -> 1

Input: [1, 4, 5, 0, 3, 2]
Output: False
// 1 -> 4 -> 3 -> 0 -> 1
// arr[2], arr[5]를 들리지 않았습니다.

Input: [1, 2, 2, 0]
Output: False
// 1 -> 2 -> 2 -> 2 -> …
// arr[0]로 돌아오지 못합니다.
```

``` javascript
// 쓸 데 없이 Cycle 찾으려 복잡하게 만든 녀석
// 문제를 대충 읽고, 잘못 이해했었음. 
// Cycle 찾는게 아니라 arr[0]으로 돌아와야함.
function solveUsingTwoPointerAndBitwiseOps(input) {
  let slow = 0
  let fast = 0
  let idx = 0
  let bitmask = 1 << input.length
  while (idx < input.length) {
    slow = input[slow]
    fast = input[input[fast]]
    
    bitmask |= 1 << slow
    bitmask |= 1 << fast

    if (slow === fast) {
      return (Math.pow(2, input.length + 1) - 1) === bitmask
    }
    idx += 1
  }
  return false
}

/* input[0]으로 Cycle이 생기는 시점에 검사하면 됨 */
function solve(input) {
  let idx = 0
  let value = 0
  while (idx < input.length) {
    value = input[value]
    if (value === 0) {
      break
    }
    idx += 1
  }
  return value === 0 && idx === input.length - 1
}

const data = [
  { input: [1, 2, 4, 0, 3], expected: true },
  { input: [1, 4, 5, 0, 3, 2], expected: false },
  { input: [1, 2, 2, 0], expected: false },
  { input: [0], expected: true },
  { input: [0,0], expected: false },
]

data.forEach(({input, expected}) => {
  const actual = solve(input)
  if (actual !== expected) {
    throw new Error('wrong answer')
  }
})
```