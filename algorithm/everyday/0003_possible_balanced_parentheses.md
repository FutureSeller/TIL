## Find possible balanced parentheses with N opening and closing brackets
정수 n이 주어지면, n개의 여는 괄호 "("와 n개의 닫는 괄호 ")"로 만들 수 있는 괄호 조합을 모두 구하시오. (시간 복잡도 제한 없습니다).
Given an integer N, find the number of possible balanced parentheses with N opening and closing brackets.

예제)
Input: 1
Output: ["()"]

Input: 2
Output: ["(())", "()()"]

Input: 3
Output: ["((()))", "(()())", "()(())", "(())()", "()()()"]

``` javascript
function solve(n) {
  const result = [];
  generate_balanced_parentheses("", 0, 0, n, result);
  return result;
}

function generate_balanced_parentheses(string, left, right, n, bucket) {
  if (left < n) {
    generate_balanced_parentheses(string + "(", left + 1, right, n, bucket);
  }
  if (right < left) {
    generate_balanced_parentheses(string + ")", left, right + 1, n, bucket);
  }
  if (left === n && right === n) {
    bucket.push(string);
  }
}

console.log(solve(4));
```