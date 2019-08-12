# HTTP Methods

## Methods
### GET
- 특정 리소스를 가져오도록 요청

### HEAD
- 어떤 헤더들이 반환되는지 요청
- 리소스를 GET으로 요청하는 경우, 어떤 헤더들이 반환되는지 요청

### POST
- 데이터를 서버로 보내는 방법 중 하나
- Content-Type
  - application/x-www-form-urlencoded 
  - application/form-data
  - text/plain

### PUT
- 새로운 자료를 만들거나, 기존의 자료 replace
- 응답: 201 Created, 204 No Content

### PATCH
- 부분적인 수정

### DELETE: 특정 리소스를 삭제
- 응답: 200 OK, 202 Accepted, 204 No Content

### OPTIONS
- 리소스와 통신하기 위한 옵션을 확인

### TRACE
- 서버에 Loopback 메시지 호출

### CONNECT
- 목적 리소스로 식별되는 서버로의 터널을 맺음

## Feature
- Safe: read-only operation (GET, HEAD, OPTIONS)
- Idempotent: 멱등성. 여러번 요청해도 동일한 결과값
- Cacheable: 응답이 캐싱이 가능한가 (GET, HEAD)

| Method | Req.body | Res.body | Safe | Idempotent | Cacheable | Allow in forms |
| - | - | - | - | - | - | - |
| GET | N | Y | Y | Y | Y | Y
| POST | Y | Y | N | N | △ | Y
| PUT |  Y | N | N | Y | N | N
| PATCH | Y | Y | N | N | N | N
| DELETE | N | N | N | Y | N | N
| OPTIONS | N | Y | Y | Y | N | N
| HEAD | N | N | Y | Y | Y | N
| TRACE | N | N | N | Y | N | N
| CONNECT | N | Y | N | N | N | N

## Questions
#### Q1. Safe && Idempotent하면 다 가능하지 않을까? OPTIONS는 왜?
- OPTIONS는 그저 사용가능한 methods만 반환해주기때문에
- HTTP caching is in terms of representations

#### Q2. non-Idempotent한데 POST는 조건에 따라 할 수도 있다고 한다. 어느 조건에서?
- idempotent 한데, GET으로 요청할 수 없는 경우 (search API, param이 엄청 많다거나)

## Status code [#](#status)
- 1XX: 정보 응답
- 2XX: 성공 응답
- 3XX: 리다이렉션
- 4XX: 클라이언트 에러 응답
- 5XX: 서버 에러 응답

---
## Appendix

### Status Code <a name='status'>
<details><summary> details </summary>
<dl>
<dt> 100 Continue </dt>
<dt> 101 Switching Protocol </dt>
<dt> 200 OK </dt>
<dt> 201 Created </dt>
<dt> 202 Accepted </dt>
<dt> 203 Non-Authoritative Information </dt>
<dt> 204 No Content </dt>
<dt> 205 Reset Content </dt>
<dt> 206 Partial Content </dt>
<dt> 300 Multiple Choice </dt>
<dt> 301 Moved Permanently </dt>
<dt> 302 Found </dt>
<dt> 303 See Other </dt>
<dt> 304 Not Modified </dt>
<dt> 305 Use Proxy </dt>
<dt> 306 Unused </dt>
<dt> 307 Temporary Redirect </dt>
<dt> 308 Permanent Redirect </dt>
<dt> 400 Bad Request </dt>
<dt> 401 Unauthorized </dt>
<dt> 402 Payment Required </dt>
<dt> 403 Forbidden </dt>
<dt> 404 Not Found </dt>
<dt> 405 Method Not Allowed </dt>
<dt> 406 Not Acceptable </dt>
<dt> 407 Proxy Authentication Required </dt>
<dt> 408 Request Timeout </dt>
<dt> 409 Conflict </dt>
<dt> 410 Gone </dt>
</dl>
</details>

## Reference
- https://developer.mozilla.org/ko/docs/Glossary/safe
- https://developer.mozilla.org/ko/docs/Web/HTTP/Methods
