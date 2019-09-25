## Integer Palindrome
정수(int)가 주어지면, 팰린드롬(palindrome)인지 알아내시오. 
팰린드롬이란, 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어를 말합니다. 
단, 정수를 문자열로 바꾸면 안됩니다.

Given an integer, check if it is a palindrome.

예제)
Input: 12345
Output: False

Input: -101
Output: False

Input: 11111
Output: True

Input: 12421
Output: True

``` javascript
function solve(n) {
  let temp = n;
  let reversed = 0;
  while (temp > 0) {
    reversed = (reversed * 10) + (temp % 10);
    temp = Math.floor(temp/10);
  }
  return reversed === n;
}

const data = [
  { input: 12345, expected: false },
  { input: -101, expected: false },
  { input: 11111, expected: true },
  { input: 12421, expected: true },
  { input: 0, expected: true },
  { input: -0, expected: true }
];

data.forEach(({input, expected}) => {
  const actual = solve(input);
  if (actual !== expected) {
    throw new Error("wrong answer");
  }
});
```