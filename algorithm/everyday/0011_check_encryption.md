## Check if two strings can be encrypted 1 to 1
길이가 같은 두 문자열(string) A 와 B가 주어지면, A 가 B 로 1:1 암호화 가능한지 찾으시오.

Given two strings of equal length, check if two strings can be encrypted 1 to 1.

예제)
Input: “EGG”, “FOO”
Output: True // E->F, G->O

Input: “ABBCD”, “APPLE”
Output: True // A->A, B->P, C->L, D->E

Input: “AAB”, “FOO”
Output: False

``` javascript
function solve(plain, encrypted) {
  const cipher = Object.create(null);
  for (let idx = 0; idx < plain.length; idx += 1) {
    const plainChar = plain[idx];
    if (cipher[plainChar] === undefined) {
      cipher[plainChar] = encrypted[idx];
    } else if (cipher[plainChar] !== encrypted[idx]) {
      return false;
    }
  }
  return true;
}

const data = [
  { input: ['EGG', 'FOO'], expected: true },
  { input: ['ABBCD', 'APPLE'], expected: true },
  { input: ['AAB', 'FOO'], expected: false }
];

data.forEach(({input, expected}) => {
  const [plain, encrypted] = input;
  const actual = solve(plain, encrypted);
  if (actual !== expected) {
    throw new Error('wrong answer');
  }
});
```