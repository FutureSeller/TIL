development 말고 production으로 빌드된 결과물을 로컬에서 보고싶을 경우가 종종 생긴다.
혹은 간단한 웹서버를 띄울 일이 생기기 마련이다.

```bash
base_directory=public

npx http-server ${base_directory}
```

위와 같이 입력 후, http://localhost:8080 에 접속하면 된다.
