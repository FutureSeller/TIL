# HSTS (HTTP Strict Transport Security)

#### 나오게 된 배경
- HTTP 요청을 받고 HTTPS로 리다이렉트하고 싶음
- 강제로 `302 Redirect` 응답을 내려줄 수 있음
- 리다이렉트 이전의 암호화되지 않은 버전의 요청을 핸들링해야하므로 MITM의 잠재적 위험이 있음

#### Content
- HSTS는 웹 사이트가 브라우저에게 HTTP로 연결하면 안되고 HTTPS로 자동으로 변경해야함을 알림
- 맨 처음 HTTPS로 접근하면 서버는 `Strict-Transport-Security` 헤더를 응답시에 내려줌
- 브라우저가 해당 정보를 기록하여 자동으로 HTTPS를 사용하도록 변경
- 헤더에 명시된 만료시간(expiration time)이 지나면, 갱신이 필요함

#### Example
모든 서브도메인을 포함해 최대 1년간 HTTPS로 접근하도록 함

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

---
## Reference
- https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Strict-Transport-Security
- https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security