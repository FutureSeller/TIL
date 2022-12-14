## Reverse all the words in the given string
주어진 string 에 모든 단어를 거꾸로 하시오.
Reverse all the words in the given string.

예제)
Input: “abc 123 apple”
Output: “cba 321 elppa”

``` javascript
function solveSimplest(input) {
  const reverse = (word) => word.split('').reverse().join('');
  const words = input.split(' ');
  const result = [];
  for (const word of words) {
    result.push(reverse(word));
  }
  return result.join(' ');
}

function solveUsingStack(input) {
  const stack = [];
  const reverse = (stack) => {
    let word = '';
    while (stack.length) {
      word += stack.pop();
    }
    return word;
  }

  let result = '';
  for (const char of input) {
    if (char === ' ') {
      result += `${reverse(stack)}${char}`;
    } else {
      stack.push(char)
    }
  }
  result += `${reverse(stack)}`;
  return result;
}

const data = [
  { input: "abc 123 apple", expected: "cba 321 elppa" },
  { input: " a  bc d ", expected: " a  cb d " },
  { input: "  abc  ", expected: "  cba  " },
  { input: "a", expected: "a" },
  { input: "", expected: "" }
];

const assertEqual = (actual, expected) => {
  if (actual !== expected) {
    throw new Error('wrong answer');
  }
}

data.forEach(({input, expected}) => {
  const actualSimplest = solveSimplest(input);
  const actualUsingStack = solveUsingStack(input);
  assertEqual(actualSimplest, expected);
  assertEqual(actualUsingStack, expected);
});

/*
-----------
input: abc 123 apple
        simplest: 0.252ms
        stack: 0.112ms
-----------
input:  a  bc d
        simplest: 0.022ms
        stack: 0.008ms
-----------
input:   abc
        simplest: 0.015ms
        stack: 0.006ms
-----------
input: a
        simplest: 0.009ms
        stack: 0.004ms
-----------
input:
        simplest: 0.020ms
        stack: 0.003ms
*/
```