HEAD에 있는 내용에 추가하거나 고칠 때, rebase를 써서 squash나 edit을 쓰긴 귀찮음
간단한 amend로 해결

``` bash
$ echo "a" >> README.md
$ git add README.md
$ git commit --amend
$ git push -f
```
