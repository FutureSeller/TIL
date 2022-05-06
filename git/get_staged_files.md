종종 `git reset --soft HEAD^`를 통해서 되돌리고 커밋을 다시 쌓는 경우가 생기는데, 
staged file 이름들을 가지고 restore하는게 귀찮아서 리스트를 가져오는 방법을 찾아봄.

```bash
$ git diff --name-only --cached
```
