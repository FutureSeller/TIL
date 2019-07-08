가끔씩 띄워진 container들을 다 내리거나, local repository의 이미지들을 다 지우고싶을 때가 있을 때 사용한다.

### Commands
``` bash
$ docker rm -f $(docker ps -aq)
$ docker rmi $(docker images -aq)
```
