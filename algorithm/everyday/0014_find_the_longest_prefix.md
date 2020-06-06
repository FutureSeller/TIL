## Find the longest common prefix of all strings.
문자열 배열(string array)이 주어지면, 제일 긴 공통된 접두사(prefix)의 길이를 찾으시오.

Given an array of strings, find the longest common prefix of all strings.

예제)

Input: [“apple”, “apps”, “ape”]
Output: 2 // “ap”

Input: [“hawaii”, “happy”]
Output: 2 // “ha”

Input: [“dog”, “dogs”, “doge”]
Output: 3 // “dog”

``` javascript
const makeTrie = (input) => {
  const trie = {};
  let trieNode = trie;
  for (let char of input) {
    trieNode[char] = {};
    trieNode = trieNode[char];
  }
  return trie;
}

function solve(array) {
  if (!array) return 0;

  const trie = makeTrie(array[0]);
  let depth = array[0].length;

  for (let i=1; i < array.length; i += 1) {
    const value = array[i];
    let triePtr = trie, j = 0;
    while (j < depth) {
      const char = value[j];
      if (!(char in triePtr)) {
        depth = j;
        break;
      }
      triePtr = triePtr[char];
      j += 1;
    }
  }
  return depth;
}

const data = [
  { input: ['apple', 'apps', 'ape'], expected: 2 },
  { input: ['hawaii', 'happy'], expected: 2 },
  { input: ['dog', 'dogs', 'doge'], expected: 3 },
  { input: ['dog', 'cat'], expected: 0 },
  { input: ['', 'dog'], expected: 0 }
];

data.forEach(({input, expected}) => {
  const actual = solve(input);
  if (actual !== expected) {
    throw new Error('wrong answer');
  }
});
```