``` bash
# 
$ git rev-parse HEAD
$ git rev-parse --verify HEAD

# 약간의 응용
$ git show-ref | grep $(git rev-parse HEAD)
d919ecd254fd3a10997ab4801f11c412b2dd2152 refs/heads/master
d919ecd254fd3a10997ab4801f11c412b2dd2152 refs/remotes/origin/HEAD
d919ecd254fd3a10997ab4801f11c412b2dd2152 refs/remotes/origin/master
```
