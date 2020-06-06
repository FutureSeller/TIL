## Merge intersecting intervals
간격(interval)로 이루어진 배열이 주어지면, 겹치는 간격 원소들을 합친 새로운 배열을 만드시오. 
간격은 시작과 끝으로 이루어져 있으며 시작은 끝보다 작거나 같습니다.

Given a list of intervals, merge intersecting intervals.

예제)
Input: {{2,4}, {1,5}, {7,9}}
Output: {{1,5}, {7,9}}

Input: {{3,6}, {1,3}, {2,4}}
Output: {{1,6}}

``` javascript
const START = 0;
const END = 1;

const isOverlapped = (a, b) => a[START] <= b[START] && a[END] >= b[START];
const compare = (prev, next) => prev[START] > next[START];

function solve(input) {
  if (input.length < 2) {
    return input;
  }
  const sorted = [...input].sort(compare);
  const result = [sorted[0]];
  for (let idx = 1; idx < sorted.length; idx += 1) {
    const peek = result[result.length - 1];
    const cursor = sorted[idx];
    if (isOverlapped(peek, cursor)) {
      peek[END] = Math.max(peek[END], cursor[END]);
    } else {
      result.push(cursor);
    }
  }
  return result;
}

const data = [
  { input: [[2,4], [1,5], [7,9]], expected: [[1,5], [7,9]] },
  { input: [[3,6], [1,3], [2,4]], expected: [[1,6]]},
  { input: [[6,8], [1,9], [2,4], [4,7]], expected: [[1,9]]},
  { input: [[5,8], [2,4], [1,3], [6,9]], expected:[[1,4], [5,9]]}
];

data.forEach(({input, expected}) => {
  const actual = solve(input);
  if (JSON.stringify(actual) !== JSON.stringify(expected)) {
    throw new Error('wrong answer');
  }
});
```