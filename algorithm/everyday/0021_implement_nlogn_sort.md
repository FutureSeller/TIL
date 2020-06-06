## Implement an O(nlogn) time complexity sorting algorithm

O(n log n)시간 복잡도를 가진 정수 배열 정렬 알고리즘을 구현하시오.

Implement an O(n log n) time complexity sorting algorithm.

```
예제)
Input: [3, 1, 5, 6]
Output: [1, 3, 5, 6]
```

```javascript
function heapify(array, N, i) {
  const left = 2 * i + 1;
  const right = 2 * i + 2;
  let largest = i;

  if (left < N && array[largest] < array[left]) {
    largest = left;
  }

  if (right < N && array[largest] < array[right]) {
    largest = right;
  }

  if (largest !== i) {
    const temp = array[i];
    array[i] = array[largest];
    array[largest] = temp;
    heapify(array, N, largest);
  }
}

function heapSort(array) {
  const N = array.length;
  const PIVOT = 0;
  const sortedArray = [...array];

  for (let i = Math.floor(N / 2) - 1; i >= 0; --i) {
    heapify(sortedArray, N, i);
  }

  for (let i = N - 1; i >= 0; --i) {
    const temp = sortedArray[PIVOT];
    sortedArray[PIVOT] = sortedArray[i];
    sortedArray[i] = temp;
    heapify(sortedArray, i, PIVOT);
  }

  return sortedArray;
}

const data = [
  { input: [3, 1, 5, 6], expected: [1, 3, 5, 6] },
  { input: [6, 5, 4, 3, 2, 1], expected: [1, 2, 3, 4, 5, 6] }
];

data.forEach(({ input, expected }) => {
  const actual = heapSort(input);
  if (actual.join(",") !== expected.join(",")) {
    throw new Error("wrong answer");
  }
});
```
