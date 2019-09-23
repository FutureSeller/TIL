## Longest substring without duplicate characters
String이 주어지면, 중복된 char가 없는 가장 긴 서브스트링 (substring)의 길이를 찾으시오.
Given a string, find the longest substring that does not have duplicate characters.

예제)
Input: “aabcbcbc”
Output: 3 // “abc”

Input: “aaaaaaaa”
Output: 1 // “a”

Input: “abbbcedd”
Output: 4 // “bced”

``` javascript
function assertNumberEquals(actual, expected) {
  if (actual !== expected) {
    throw new Error('not equal');
  }
}

function solve(input) {
  if (input.length < 2) {
    return input.length;
  }

  let charFreqMap = {};
  let windowStart = 0;
  let windowEnd = 0;
  let maxLength = -1;

  for (; windowEnd < input.length; windowEnd += 1) {
    let rightChar = input[windowEnd];
    if (!charFreqMap[rightChar]) {
      charFreqMap[rightChar] = 0;
    }
    charFreqMap[rightChar] += 1;

    while (charFreqMap[rightChar] > 1) {
      let leftChar = input[windowStart];
      charFreqMap[leftChar] -= 1;
      windowStart += 1;
    }
    maxLength = Math.max(maxLength, windowEnd - windowStart +1);
  }

  return maxLength;
}

const data = [
  { input: "aabcbcbc", expected: 3 },
  { input: "aaaaaaaa", expected: 1 },
  { input: "abbbcedd", expected: 4 },
  { input: "", expected: 0 },
  { input: "a", expected: 1 }
]

data.forEach(({input, expected}) => {
  assertNumberEquals(solve(input), expected);
});
```
