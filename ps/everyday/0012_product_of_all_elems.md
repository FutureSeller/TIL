## Product of all element values without itself
정수로된 배열이 주어지면, 각 원소가 자신을 뺀 나머지 원소들의 곱셈이 되게하라.
단, 나누기 사용 금지, O(n) 시간복잡도

Given an integer array, make each element a product of all element values without itself.

예제)

input: [1, 2, 3, 4, 5]
output: [120, 60, 40, 30, 24]

``` javascript
function solve(input) {
  if (input.length < 2) {
    return input;
  }
  const answer = new Array(input.length).fill(1);
  let prev = input[0];
  for (let i=1; i < answer.length; i += 1) {
    answer[i] = prev;
    prev = prev * input[i];
  }
  prev = input[input.length-1];
  for (let i=answer.length - 2; i >= 0; i -= 1) {
    answer[i] *= prev;
    prev = prev * input[i];
  }
  return answer;
}

const data = [
  { input: [1,2,3,4,5], expected: [120,60,40,30,24] },
  { input: [2,2,3,4,5], expected: [120,120,80,60,48] },
  { input: [2,-2,3,-4,5], expected: [120,-120,80,-60,48] },
  { input: [1,2,0,4,5], expected: [0,0,40,0,0] },
  { input: [1,1,1,1,1], expected: [1,1,1,1,1] },
];

data.forEach(({input, expected}) => {
  const actual = solve(input);
  if (JSON.stringify(actual) !== JSON.stringify(expected)) {
    throw new Error('wrong answer');
  }
});
```