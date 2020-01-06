## Find an element in a rotated array in logn

정렬된 정수 배열이 있습니다. 이 배열의 모든 원소들을 오른쪽으로 랜덤하게 Z번 이동하였습니다.

예를 들면 [1, 2, 3, 4, 5] -> [3, 4, 5, 1, 2].

이런 배열과 정수 K 가 주어지면, 배열안에 K가 존재하는지 찾으시오.

존재한다면 배열의 인덱스, 존재하지 않다면 -1 을 리턴하시오.

시간복잡도 제한 O(log N).

```
input: [3, 4, 5, 1, 2], 4
output: 1

input: [2, 4, 5, 1], 3
output: -1

input: [4, 6, 7, 8, 1, 2, 3], 5
output: -1
```

```javascript
function solve(array, target) {
  let start = 0
  let end = 1
  while (array[end] < target) {
    start = end + 1
    end = 2 * start + 1
    if (end > array.length) {
      end = array.length - 1
      break
    }
  }
  while (start <= end && start < array.length) {
    const mid = start + Math.trunc((end - start) / 2)
    if (array[mid] < target) {
      start = mid + 1
    } else if (array[mid] > target) {
      end = mid - 1
    } else {
      return mid
    }
  }
  return -1
}

const data = [
  { input: [3, 4, 5, 1, 2], target: 4, expected: 1 },
  { input: [2, 4, 5, 1], target: 3, expected: -1 },
  { input: [4, 6, 7, 8, 1, 2, 3], target: 5, expected: -1 },
  { input: [1, 2, 3, 4, 5], target: 6, expected: -1 },
]

data.forEach(({input, target, expected}) => {
  const actual = solve(input, target)
  console.log(input, target, expected, actual)
  if (actual !== expected) {
    throw new Error('wrong answer')
  }
})
```
