하나의 repo에 branch를 따서 이것저것 테스트하다보니, untracked 된 파일들이 쌓이기 시작함.
이를 없애기 위해 방법을 모색하다가 아래 command를 알게됨.

``` bash
# remove untracked directories & files
$ git clean -fd  

# Don’t actually remove anything, just show what would be done
# 현재 해당 파일인 clean.md는 untracked된 상태. 
# 당장 삭제하진 않고 위의 cmd 실행 시 어떤 결과가 나올지 알려줌.
$ git clean -n   
Would remove clean.md
```