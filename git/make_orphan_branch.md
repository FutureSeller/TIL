하나의 repo에 branch를 따서 이것저것 테스트하다보니, 
branch에 master의 commit이 딸려있는게 너무 보기 불편했다.

### Scenario
- RCCar repo에 dev-router라는 empty branch를 생성해보자.
- master: [RCCar](http://github.com/FutureSeller/RCCar)
- branch: [dev-router](https://github.com/FutureSeller/RCCar/commit/076c70cfd40b6a6c8d69908112a4ee8e1a2da91d)

``` bash
$ git checkout --orphan dev-redux
$ git rm --cached -r .
$ git commit --allow-empty -m "initial commit for orphan branch"
$ git push -u origin dev-router
```

이 것에 대해 좀 더 자세하게 알아보려면 
[Git 저장소에서 비어있는 새 브랜치 만들기](https://blog.outsider.ne.kr/1054)를 참고하면 좋을 것 같다.