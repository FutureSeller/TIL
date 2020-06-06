## Problem
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is simply X + II. 
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

## How to Solve
0. 해당 문제 자체의 문제점
```
- Input이 이상해도 답을 가져올 수 있다. 예를 들면 입력값으로 "IIIV"이 주어졌다면?
- Roman: `You would not put more than one smaller number in front of a larger number to subtract. For example, IIV would not mean 3`
- Run Code로 돌려보면.. `Your input "IIIV". Output None. Expected 6.`
- 해당 문제는 입력 값이 항상 valid하다고 가정하는 듯하다.
```
1. 입력 값이 항상 valid하다고 가정
2. 특정 idx의 Roman이 idx+1의 Roman보다 크면 덧셈, 작으면 뺄셈을 수행하면 된다.
3. 마지막 값은 항상 더 해진다. idx+1이 존재하지 않아 뺄셈이 될 수 없기 때문이다.

## My Solution
``` python
# Runtime: 44 ms, faster than 68.21% of Python online submissions for Roman to Integer.
# Memory Usage: 11.8 MB, less than 27.95% of Python online submissions for Roman to Integer.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nummap = { 
            'I': 1, 
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        for idx in range(len(s)-1):
            if nummap[s[idx]] >= nummap[s[idx+1]]:
                res += nummap[s[idx]]
            else:
                res -= nummap[s[idx]]
        res += nummap[s[-1]]
        return res
```

## Compare: Runtime
- <details><summary> code </summary><pre>

  ``` python
  # sample 12 ms submission
  class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        out_int = 0
        table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)):
            out_int += table[s[i]]
            if i!=0 and table[s[i]]>table[s[i-1]]:
                out_int -= 2*table[s[i-1]]
                
        return out_int
  ```
  </pre></summary>

## Compare: Memory
- 사실 어떤 점에서 아래 코드가 더 이득인지 전혀 모르겠다...
- <details><summary> code </summary><pre>

  ``` python
  # sample 11440 kb submission
  class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        rm_dict = {"I":["V","X"],"V":[],"X":["L","C"],"L":[],"C":["D","M"],"D":[],"M":[]}
        val = 0
        i = 0
        while i < len(s)-1:
            if s[i+1] not in rm_dict[s[i]]:
                val = val + roman_dict[s[i]]
            else:
                val = val + roman_dict[s[i+1]] - roman_dict[s[i]]
                i += 1
            i += 1
           
        if i == len(s) - 1:
            val = val + roman_dict[s[len(s)-1]]
        return val
  ```
  </pre></summary>
