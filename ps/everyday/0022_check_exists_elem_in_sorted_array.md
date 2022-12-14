## Given a sorted integer array and an integer N, check if N exists in the array.

정렬(sort)된 정수 배열과 정수 n이 주어지면, 배열안에 n이 있는지 체크하시오. 시간복잡도를 최대한 최적화하시오.

Given a sorted integer array and an integer N, check if N exists in the array.

```
예제)
Input: [1, 2, 3, 7, 10], 7
Output: true

Input: [-5, -3, 0, 1], 0
Output: true

Input: [1, 4, 5, 6, 8, 9], 10
Output: false
```

```javascript
// My log(N) solution
function solve(sortedArray, start, end, target) {
  const mid = start + Math.trunc((end - start) / 2);
  const medium = sortedArray[mid];
  if (medium === target) {
    return true;
  }
  return medium > target
    ? solve(sortedArray, start, mid, target)
    : solve(sortedArray, mid, end, target);
}

const data = [
  { input: [1, 2, 3, 7, 10], target: 7, expected: true },
  { input: [-5, -3, 0, 1], target: 0, expected: true },
  { input: [1, 4, 5, 6, 8, 9], target: 10, expected: false }
];

data.forEach(({ input, target, expected }) => {
  const actual = solve(input, 0, input.length - 1, target);
  if (actual !== expected) {
    throw new Error("wrong answer");
  }
});
```
