# PM2

> 응용 프로그램을 온라인으로 관리하고 유지하는데 도움이 되는 데몬 프로세스 매니저

## 배경
- Node.js는 기본적으로 싱글 스레드;
- Node.js 애플리케이션은 단일 CPU 코어에서 실행되기 때문에 CPU의 멀티코어 시스템은 사용할 수 없음
- 클러스터(Cluster) 모듈을 통해 단일 프로세스를 멀티 프로세스(Worker)로 늘릴 수 있는 방법을 제공
- 애플리케이션을 실행하면 처음에는 마스터 프로세스만 생성 > CPU 개수만큼 워커 프로세스를 생성하고 마스터 프로세스와 워커 프로세스가 각각 수행해야 할 일들을 구현
- 워커 프로세스에 문제가 생겼을 때, 변경을 반영할 때 어떤 식으로 재시작을 처리할지 프로세스를 관리해주는 매니저
- graceful shutdown!

## Commands

### 실행 방법
``` bash
$ pm2 start app.js 
$ pm2 start bashscript.sh

# --name <app_name>: 이름을 명시함
# --watch: watch하다가 파일변경이 있으면 응용 프로그램을 재실행
# --max-memory-restart <200MB>: 앱 재실행을 위한 메모리 임계점
# --log <log_path>: 로깅할 경로
# -- arg1 arg2 arg3: 기타 인자를 넘기는 방법
# --restart-delay <ms>: 자동으로 재실행 시 주어져야할 delay
# --time: 로그에 time prefix를 붙임
# --no-autorestart: 자동 재실행을 막음
# --cron <cron_pattern>
# --no-daemon
```

### 프로세스 관리 방법
``` bash
$ pm2 restart app_name
$ pm2 reload app_name
$ pm2 stop app_name
$ pm2 delete app_name

# app_name 대신 all이나 id 값을 넘길 수 있음
```

### 프로세스 리스팅
```bash
$ pm2 [list | ls | status]
```

### 로그 출력
```bash
$ pm2 logs
```

### 터미널 기반의 대쉬보드
```bash
$ pm2 monit
```

나머지 내용은 https://pm2.keymetrics.io/docs/usage/quick-start/#cheatsheet 를 참고

---
## Reference
- https://engineering.linecorp.com/ko/blog/pm2-nodejs/
- https://pm2.keymetrics.io/docs/usage/quick-start/
