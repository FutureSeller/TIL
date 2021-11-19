리모트만 날리고 로컬을 날리는 걸 자꾸 까먹어서, 한번에 날리는 bash를 작성한 뒤 남겨놓는다.

```sh
$ git fetch --prune
$ git branch -vv | grep "gone]" | awk '{print $1}' | xargs git branch -D
```
