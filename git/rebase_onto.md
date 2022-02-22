## `git rebase --onto [newbase] [upstream] [branch]`

이런 명령어를 쓸일이 없으면 참 좋지만 생기게 될 줄 몰랐다. 이 명령어를 찾고 사용하게 된 시나리오는 아래와 같다.


### Step 1
`master`(production)를 기준으로 `develop`이라는 개발용 long-lived 브랜치가 있고, 각각의 하나의 큰 기능의 집합인 `feature/p2`가 있다.
`feature/p2`에 묶여 나갈 기능 중, 세부 구현인 `feature/wishes`라는 브랜치가 존재한다.

```
o master
|
|___ o - o - o - o develop
                 |
                 |___ o - o - o - o feature/p2
                                  |
                                  |___ o - o - o - o feature/wishes
```

### Step 2
이 와중에 `feature/wishes`라는 세부 구현은 `feature/p2`에 포함되지 않기로 했고, `feature/p2`가 `develop`에 squash merge가 되었다. (브랜치는 살아있다.)

```
o master
|
|___ o - o - o - o - o' develop
                 |
                 |___ o - o - o - o feature/p2
                                  |
                                  |___ o - o - o - o feature/wishes
```

### Step 3
다음 배포 단위인 p3가 squash merge 된 develop을 base로 따졌다.

```
o master
|
|___ o - o' develop
     |   |
     |   |___ o - o - o feature/p3
     |
     |___ o - o - o - o feature/p2
                      |
                      |___ o - o - o - o feature/wishes
```


## 자, 내가 해야할 일은... feature/wishes를 develop 위에 쌓아야한다.

`git rebase --onto [newbase] [upstream] [branch]`

`upstream`에 없는 `branch`의 커밋들을 `newbase` 브랜치에 적용한다. 쉽게 얘기하면 base를 `newbase`로 바꾸고, branch - upstream의 커밋들을 새로운 base위에 쌓아준다. 

Step3의 상황에서 develop이라는 녀석을 base로 삼고, feature/p2와 feature/wishes의 작업의 diff만을 따서 develop에 얹어 주는 것(onto)이다. 

```
$ git rebase --onto develop feature/p2 feature/wishes
```

