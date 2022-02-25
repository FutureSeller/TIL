## git gc

>> `git gc`는 저장소에 필요없는 파일을 삭제하고 남은 파일을 압축하는 “Garbage Collection” 명령이다.
>> 직접 실행시켜도 되지만 Git이 자동으로 실행해준다.

이것도 사실 어쩌다가 터미널에 떠서 알게된 것. pull을 받는데 아래와 같이 `git help gc`라고 뜨는 것이 아닌가. 

```bash
# 저장소, 파일이름, 커밋해시는 적당히 아무 문자열로 바꾸었다

$ git pull --rebase
remote: Enumerating objects: 674, done.
remote: Counting objects: 100% (392/392), done.
remote: Compressing objects: 100% (89/89), done.
remote: Total 219 (delta 148), reused 178 (delta 118), pack-reused 0
Receiving objects: 100% (219/219), 31.07 KiB | 3.88 MiB/s, done.
Resolving deltas: 100% (148/148), completed with 61 local objects.
From https://github.com/XXXX/XXXX
   hash..hash  develop      -> origin/develop
   hash..hash  feature/p2.5 -> origin/feature/p2.5
   hash..hash  master       -> origin/master
Auto packing the repository in background for optimum performance.
See "git help gc" for manual housekeeping.
Updating hash1..hash2
Fast-forward
Auto packing the repository in background for optimum performance.
See "git help gc" for manual housekeeping.
 .github/workflows/1.yml         | 2 +-
 .github/workflows/2.yml            | 2 +-
 .github/workflows/3.yml                    | 2 +-
 4 files changed, 5 insertions(+), 5 deletions(-)
```

자세한 내용은 [운영](https://git-scm.com/book/ko/v2/Git%EC%9D%98-%EB%82%B4%EB%B6%80-%EC%9A%B4%EC%98%81-%EB%B0%8F-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B3%B5%EA%B5%AC#_git_gc)을 읽어보면 된다.

아주 대략적으로 몇몇개 문장들을 추려보자면,

- `git gc --auto`: git은 때가 되면 자동으로 "auto gc" 명령을 실행하는데, 이때 대부분 아무런 일도 일어나지 않는다.
  - Loose 개체가 너무 많거나, Packfile 자체가 너무 많으면 Git은 그제야 진짜로 git gc 명령이 일하게 한다.
  - Loose 개체가 7천 개가 넘거나 Packfile이 50개가 넘지 않으면 Git은 실제로 gc 작업을 실행하지 않는다.
- refs를 파일 하나로 압축
  - .git/refs에 있는 파일들이 사라지고, .git/packed-refs 파일로 압축
  - 이 상태에서 refs를 수정하면 파일을 수정하는게 아니라 refs/heads에 파일을 새로 만듬
  - git은 refs가 가리키는 sha-1을 찾을 때 먼저 refs를 찾고 없으면 packed-refs 파일에서 찾는다.


--- 

## Reference
- https://git-scm.com/book/ko/v2/%EB%B6%80%EB%A1%9D-C%3A-Git-%EB%AA%85%EB%A0%B9%EC%96%B4-%EA%B4%80%EB%A6%AC
- https://git-scm.com/book/ko/v2/Git%EC%9D%98-%EB%82%B4%EB%B6%80-%EC%9A%B4%EC%98%81-%EB%B0%8F-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B3%B5%EA%B5%AC#_git_gc
