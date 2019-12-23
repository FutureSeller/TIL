## Shift all elements in the array K times

정수 배열과 정수 k가 주어지면 모든 원소를 k칸씩 앞으로 옮기시오.

Given an array and an integer K, shift all elements in the array K times.

```
input: [1, 2, 3, 4, 5], k = 2
output: [3, 4, 5, 1, 2]

input: [0, 1, 2, 3, 4], k = 1
output: [1, 2, 3, 4, 0]
```

```javascript
// using es6 features
function simplest(array, k) {
  return [...array.slice(k, array.length), ...array.slice(0, k)];
}

const gcd = (a, b) => {
  return b === 0 ? a : gcd(b, a % b);
};

// using a juggling algorithm
function solve(array, k) {
  const N = array.length;
  const end = gcd(N, k);

  for (let start = 0; start < end; ++start) {
    const temp = array[start];
    let head = start;
    while (true) {
      let nextStep = head + k;
      if (nextStep >= N) {
        nextStep = nextStep - N;
      }
      if (nextStep === start) {
        break;
      }
      array[head] = array[nextStep];
      head = nextStep;
    }
    array[head] = temp;
  }

  return array;
}

const data = [
  { input: [1, 2, 3, 4, 5], k: 2, expected: [3, 4, 5, 1, 2] },
  { input: [0, 1, 2, 3, 4], k: 1, expected: [1, 2, 3, 4, 0] },
  { input: [0, 1, 2, 3, 4, 5], k: 3, expected: [3, 4, 5, 0, 1, 2] }
];

data.forEach(({ input, k, expected }) => {
  const actual = solve(input.slice(), k);
  if (JSON.stringify(actual) !== JSON.stringify(expected)) {
    throw new Error(`wrong answer: ${actual}, ${expected}`);
  }
});
```
