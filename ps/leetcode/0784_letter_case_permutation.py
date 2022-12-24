class Solution:
  def letterCasePermutation(self, s):
    result = []
    
    def dfs(index, substring, result):
      if len(substring) == len(s):
        result.append(substring)
        return

      if s[index].isalpha():
        dfs(index + 1, substring + s[index].swapcase(), result)
        dfs(index + 1, substring + s[index], result)
      dfs(0, '', result)

    return result
