## Move all the 0s to the right of the array
정수 배열(int array)이 주어지면 0이 아닌 정수 순서를 유지하며
모든 0을 배열 오른쪽 끝으로 옮기시오.
단, 시간복잡도는 O(n), 공간복잡도는 O(1)여야 합니다.

Given an integer array, move all the 0s to the right of the array
without changing the order of non-zero elements.

예제)
Input: [0, 5, 0, 3, -1]
Output: [5, 3, -1, 0, 0]

Input: [3, 0, 3]
Output: [3, 3, 0]

``` javascript
function equals(actual, expected) {
  if (JSON.stringify(actual) !== JSON.stringify(expected)) {
    throw new Error("wrong answer");
  }
}

function solveUsingSwap(input) {
  if (input.length < 2) {
    return input;
  }

  let zeroIdx = input.indexOf(0);
  if (zeroIdx === input.length - 1) {
    return input;
  }
  let idx = zeroIdx;
  while (idx < input.length) {
    if (input[idx] !== 0) {
      let temp = input[zeroIdx];
      input[zeroIdx] = input[idx];
      input[idx] = temp;
      zeroIdx += 1;
    }
    idx += 1;
  }
  return input;
}

function solveUsingCount(input) {
  let count = 0;
  for (let idx = 0; idx < input.length; idx += 1) {
    if (input[idx] !== 0) {
      input[count] = input[idx];
      count += 1;
    }
  }
  while (count < input.length) {
    input[count] = 0;
    count += 1;
  }
  return input;
}

const data = [
  { input: [0,5,0,3,-1], expected: [5,3,-1,0,0] },
  { input: [3,0,3], expected: [3,3,0] },
  { input: [1,9,8,4,0,0,2,7,0,6,0,9], expected: [1,9,8,4,2,7,6,9,0,0,0,0] },
  { input: [0,1], expected: [1,0] },
  { input: [0,0,0,0,0,0,0,0,0,1], expected: [1,0,0,0,0,0,0,0,0,0] }
];

data.forEach(({input, expected}) => {
  const actualSwapped = solveUsingSwap(input);
  const actualCounted = solveUsingCount(input);
  equals(actualSwapped, expected);
  equals(actualCounted, expected);
});
```
