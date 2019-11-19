# Dockerfile
자세한 내용은 https://docs.docker.com/engine/reference/builder 해당 링크를 참고

#### `RUN` vs. `CMD` vs. `ENTRYPOINT`
- **RUN**
  - 새로운 layer 추가, 추가된 layer위에서 command 실행 
  - e.g., package 설치 or 빌드
- **CMD**
  - 컨테이너가 실행 될 때 명령어 및 값들을 전달하여 실행
  - 여러번 사용할 수 있지만 가장 마지막 CMD만 남음 (override)
  - `docker run`에 값을 전달하면 무시됨
  - 배포 시점 및 환경에 따라 command를 다양하게 지정해야하는 경우 유용
- **ENTRYPOINT**
  - 컨테이너가 시작되었을 때 스크립트 or command 실행
  - Dockerfile에서 단 한번만 사용할 수 있음
  - 지정한 명령을 언제나 실행하기 때문에 특정 루틴을 실행해야할때 유용하게 사용 가능

``` bash
$ cat Dockerfile
FROM ubuntu
ENTRYPOINT ["/bin/echo", "Hello"]
CMD ["world"]

$ docker run -it <image-name>
Hello world

$ docker run -it <image-name> ME
Hello ME
```

### Example: Redis
사실 좀 더 깔끔하게 만들 수 있을 것 같은데, 고치기 귀찮아져서 그대로 두었다.

#### 나름대로 혼자 정한 요구사항
- 컨테이너 자체가 Root 권한으로 돌기때문에 user를 생성하고 workdir을 한정함
- Redis의 버전을 `docker-compose`의 args나 사용자 입력으로 받도록 함
- ASAN을 붙인 버전을 base image 위에 붙임

``` Dockerfile
FROM ubuntu:16.04
 
ARG USER
RUN useradd -ms /bin/bash $USER

ARG REDIS_VERSION
ENV REDIS_VERSION ${REDIS_VERSION}

ARG HOME
WORKDIR $HOME

RUN apt-get -qq update \
     && apt-get install -y -qq wget gcc g++ make \
     && wget --no-verbose http://download.redis.io/releases/redis-${REDIS_VERSION}.tar.gz \
     && tar -xzf redis-${REDIS_VERSION}.tar.gz \
     && mv redis-${REDIS_VERSION} redis \
     && rm redis-${REDIS_VERSION}.tar.gz \
     && cd redis && make && cd

RUN chown -R $USER:$USER redis

USER $USER
```

#### Example: 위의 base image를 기준으로 ASAN을 붙인 Redis 컨테이너
``` Dockerfile
FROM redis_base:latest 

ARG USER
USER $USER

RUN cd redis && make distclean \
    && make CFLAGS=-fsanitize=address LDFLAGS=-fsanitize=address MALLOC=libc \
    && cd

ENTRYPOINT ["./redis/src/redis-server", "./redis/redis.conf"]
```

---
## Reference
- https://docs.docker.com/engine/reference/builder
- https://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint
- https://blog.leocat.kr/notes/2017/01/08/docker-run-vs-cmd-vs-entrypoint