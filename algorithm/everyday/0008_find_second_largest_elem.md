## Find the second largest element in an integer array
정수 배열(int array)이 주어지면 두번째로 큰 값을 프린트하시오.
Given an integer array, find the second largest element.

예제)
Input: [10, 5, 4, 3, -1]
Output: 5

Input: [3, 3, 3]
Output: Does not exist.

``` javascript
function solve(input) {
  let first = Number.MIN_SAFE_INTEGER;
  let second = Number.MIN_SAFE_INTEGER;

  for (const number of input) {
    if (number > first) {
      second = first
      first = number;
    } else if (number > second && number !== first) {
      second = number;
    }
  }

  return second === Number.MIN_SAFE_INTEGER ? undefined : second;
}

const data = [
  { input: [10,5,4,3,-1], expected: 5 },
  { input: [3,3,3], expected: undefined },
  { input: [3], expected: undefined },
  { input: [3,1], expected: 1 }
];

data.forEach(({input, expected}) => {
  const actual = solve(input);
  if (actual !== expected) {
    throw new Error("wrong answer");
  }
});
```
