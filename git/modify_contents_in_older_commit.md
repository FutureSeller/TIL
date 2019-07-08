## Current Status
```
$ git log
commit 0d7a...
Author: FutureSeller <f.s3ll3r@gmail.com>
Date:   Mon Jul ...

    dummydummy

commit a85c...
Author: FutureSeller <f.s3ll3r@gmail.com>
Date:   Mon Jul ...

    update README.md

commit 90fe...
Author: FutureSeller <f.s3ll3r@gmail.com>
Date:   Mon Jul ...

    ...

commit 2563...
Author: FutureSeller <f.s3ll3r@gmail.com>
Date:   Mon Jul ...
    ...
```

- commit `a85c...`에서 README.md를 업데이트했는데 오타가 발견된 상황
- `a85c..`보다 상위 commit에서 수정된 적 없음
- 새로운 commit을 만들어서 history를 어지럽히고 싶지 않음

## Commands
``` bash
$ git rebase -i a85c~
pick a85c... update README.md --> edit a85c... update README.md
pick 0d7a... dummydummy

(... 오타 수정 ...)

$ git add /path/to/README.md
$ git commit --amend
$ git rebase --continue
$ git push -f
```

## 주의할 점
- 여러명이 협업하는 환경에선 되도록 추천하지 않음: forced-push로 인해 side-effect가 생길 수 있음
- pull request를 통해 코드리뷰에서 걸러지는게 가장 바람직함
