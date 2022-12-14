## Find the Nth largest element in the array
정수 배열(int array)과 정수 N이 주어지면, N번째로 큰 배열 원소를 찾으시오.

Given an integer array and integer N, find the Nth largest element in the array.

예제)

Input: [-1, 3, -1, 5, 4], 2
Output: 4

Input: [2, 4, -2, -3, 8], 1
Output: 8

Input: [-5, -3, 1], 3
Output: -5

``` javascript
const partition = (array, left, right) => {
  const pivot = array[left];
  let i = left;
  let j = right;
  while (i < j) {
    while(pivot < array[j]) {
      j -= 1;
    }
    while (i < j && pivot >= array[i]) {
      i += 1;
    }
    const temp = array[j];
    array[j] = array[i];
    array[i] = temp;
  }
  array[left] = array[j];
  array[j] = pivot;
  return j;
};

const quickSelect = (array, left, right, k) => {
  if (k < 0 || left > right) return undefined;
  if (left === right) return array[left];

  const idx = partition(array, left, right);
  if (k === idx) {
    return array[idx];
  } else if (k < idx) {
    return quickSelect(array, left, idx - 1, k);
  } else {
    return quickSelect(array, idx + 1, right, k);
  }
};

const data = [
  { input: [[-1, 3, -1, 5, 4], 2], expected: 4 },
  { input: [[2, 4, -2, -3, 8], 1], expected: 8 },
  { input: [[-5, -3, 1], 3], expected: -5 },
  { input: [[], 1], expected: undefined },
  { input: [[1], 1], expected: 1 },
  { input: [[-1, -1], 2], expected: -1 }
];

data.forEach(({input, expected}) => {
  const [array, k] = input;
  const actual = quickSelect(array, 0, array.length - 1, array.length - k);
  if (actual !== expected) {
    throw new Error('wrong answer');
  }
});
```