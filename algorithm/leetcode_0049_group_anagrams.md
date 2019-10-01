## Description
Given an array of strings, group anagrams together.

```
Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

## My Solution
``` javascript
const groupAnagrams = function(strs) {
    const getSortedAnagram = (s) => {
        const counter = new Array(26).fill(0);
        for (let idx = 0; idx < s.length; idx += 1) {
            counter[s.charCodeAt(idx) - 97] += 1;
        }
        return counter.reduce((acc, curVal, curIdx) => {
            return acc + `${String.fromCharCode(curIdx)}${curVal}`
        }, '')
    };

    let count = 0;
    const groupMap = {};
    const result = [];
    for (let idx = 0; idx < strs.length; idx += 1) {
        const sortedAnagram = getSortedAnagram(strs[idx]);
        if (groupMap[sortedAnagram] === undefined) {
            groupMap[sortedAnagram] = count;
            count += 1
        }

        const hashIdx = groupMap[sortedAnagram];
        if (result[hashIdx] === undefined) {
            result[hashIdx] = [];
        }
        result[hashIdx].push(strs[idx]);
    }
    return result;
};
```
