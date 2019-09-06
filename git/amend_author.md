commit할 때, 동일한 혹은 local author로 두고 싶은 데 global(default) author로 commit한 걸 자주 깨달음

``` bash
$ git commit --amend --author <FutureSeller f.3ll3r@gmail.com>

# 혹은
$ git config user.name FutureSeller
$ git config user.email f.s3ll3r@gmail.com
$ git commit --amend --reset
```
