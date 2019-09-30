## Problem
Given two strings s and t , write a function to determine if t is an anagram of s.

## My Solution
``` javascript
const isAnagram = function(s, t) {
  if (s.length !== t.length) {
    return false;
  }
  const counter = new Array(26).fill(0);
  for (let idx = 0; idx < s.length; idx += 1) {
    counter[s.charCodeAt(idx) - 97] += 1;
    counter[t.charCodeAt(idx) - 97] -= 1;
  }
  return counter.every(v => v === 0);
};
```
