## Largest consecutive sum of elements
Given an integer array, find the largest consecutive sum of elements.
Time Complexity: O(n)

Example:
  Input: [-1, 3, -1, 5]
  Output: 7 // 3 + (-1) + 5

``` javascript
const solve = (array) => {
  if (array.length === 0) {
    return 0;
  }

  let currentMaxSum = array[0];
  let maxSum = array[0];

  for (let i = 1; i < array.length; ++i) {
    currentMaxSum = Math.max(currentMaxSum + array[i], array[i]);
    maxSum = Math.max(currentMaxSum, maxSum);
  }
  
  return maxSum;
}

const data = [
  { input: [-1, 3, -1, 5], expected: 7 },
  { input: [-5, -3, -1], expected: -1 },
  { input: [2, 4, -2, -3, 8], expected: 9 },
  { input: [], expected: 0 }
];

data.forEach(({ input, expected }) => {
  let actual = solve(input)
  if (actual !== expected) {
    throw `${input.join(',')} ${actual} !== ${expected}`
  }
})
```
