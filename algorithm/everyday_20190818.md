## Find two indexes of the array element that sums to the target number
정수 배열과 타겟 숫자가 주어지면, 합이 타겟값이 되는 두 원소의 인덱스를 찾으시오.
단, 시간복잡도 O(n) 여야 합니다.

Given an array of integers and a target integer, 
find two indexes of the array element that sums to the target number.

예제)
Input: [2, 5, 6, 1, 10], 타겟 8
Output: [0, 2] // 배열[0] + 배열[2] = 8

``` javascript
function solve(array, target) {
  const invertedMap = Object.create(null);
  for (let idx = 0; idx < array.length; idx += 1) {
    const value = array[idx];
    if (invertedMap[value] !== undefined) {
      return [invertedMap[value], idx];
    }
    if (invertedMap[target - value] === undefined) {
      invertedMap[target - value] = idx;
    }
  }
  return [-1, -1];
}

const data = [
  { 
    input: { 
      array: [2,5,6,1,10],
      target: 8
    },
    expected: [0,2]
  },
  { 
    input: { 
      array: [2,5,6,1,10],
      target: 13
    },
    expected: [-1,-1]
  }, 
  {
    input: { 
      array: [2],
      target: 2
    },
    expected: [-1,-1]
  },
  {
    input: { 
      array: [2,1,3,2],
      target: 4
    },
    expected: [1,2]
  },
  {
    input: { 
      array: [2,1,1,2],
      target: 4
    },
    expected: [0,3]
  }
];

data.forEach(({input, expected}) => {
  const { array, target } = input;
  const actual = solve(array, target);
  if (JSON.stringify(actual) !== JSON.stringify(expected)) {
    throw new Error(`wrong answer: ${actual} ${expected}`);
  }
});
```