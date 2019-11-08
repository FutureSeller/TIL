## SOP(Same Origin Policy)
- Origin == 출처 == (protocol, host, port)
- example: http://store.company.com/dir/page.html

| URL | Outcome | Reason |
| - | - | - |
| http://store.company.com/dir2/other.html | . | .
| https://store.company.com/page.html	| X | Protocol
| http://store.company.com:81/dir/page.html	 | X | Port
| http://news.company.com/dir/page.html	| X | Host

- 문서나 스크립트가 다른 출처의 리소스와 통신하는 것을 제한
- Inherited Origins: `about:blank`, `javascript:`
  - 해당 URL로 navigate하게한 Origin을 상속받음
  - 명시적으로 Origin이 포함되어있지 않기 때문
- Change Origin
  - `document.domain`을 조작(super-domain까지만)
  - `document.domain = "company.com";`

## CORS(Cross Origin Resource Sharing)
- "교차 출처 리소스 공유"
  - SOP에 의해 다른 Origin의 리소스와 통신하는 것을 제한하고 있음
  - 다른 Origin의 리소스가 필요할 경우 사용
  - e.g., `<img src="a resource from other origin">`
- Spec으로 정의되어 있음: https://www.w3.org/TR/cors, https://fetch.spec.whatwg.org
- How (Basic)
  - 허가된 출처 집합을 서버로부터 받아올 수 있도록 하는 HTTP 헤더를 추가
    - `Access-Control-Allow-Origin: *`: 모든 Origin으로부터 접근 가능
    - `Access-Control-Allow-Origin: http://....`: 정의된 Origin 들만 허용
  - `preflight`: 요청에 대한 응답을 하기에 안전한지 결정하기 위함
    - 조건: `PUT`, `DELETE` 등의 요청이 있을 때.
    - Ping from Client: `OPTIONS`를 통해 지원중인 메소드들 내려받음 및 헤더들을 내려받음
      - `Origin: http://foo.example`
      - `Access-Control-Request-Method: POST`
      - `Access-Control-Request-Headers: ....`
    - Pong from Server: 사용가능한 메소드 및 `credentials` 등 헤더들을 적절히 내려줌
      - `Access-Control-Allow-Origin`
      - `Access-Control-Allow-Method` 등
    - Actual Requset from Client
      - `Access-Control-*`관련 헤더들을 포함하지 않음
- 인증을 이용한 요청
  - "credentialed"(인증된) 요청: 대표적으로 쿠키를 볼 것이냐.
  - 기본적으로 cross-site 실행에서, 인증 관련 정보를 전송하지 않음 (trust의 문제)
  - 쿠키와 함께 요청이 호출되도록 하려면 (`XMLHttpRequest`)
    - Client: `withCredentials: true`로 요청을 해야함
    - Server: Valid하다면 `Access-Control-Allow-Credentials: true` 헤더를 내려줌

## Appendix
- CORS of `fetch` 
  - default: CORS를 허용하지 않음 `mode: 'no-cors'`
    - 허용하려면 요청 시 `mode: 'cors'`를 넣어줘야함.
    - e.g., `fetch('domain', { mode: 'cors'})`
  - credentials
    - default: https://www.chromestatus.com/feature/4539473312350208
      - 과거: default는 `omit`
      - 현재: default는 `same-origin`
    - crocss origin에 허용하려면 `fetch('cross-domain', { credentials: 'include' })`
    - same origin에 허용하려면 `fetch('same-origin, { crendentials: 'same-origin' })`
    - 원하지 않는 다면 `fetch('same-origin, { crendentials: 'omit' })`

---
## Reference
- https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
- https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy
- https://fetch.spec.whatwg.org/#cors-protocol
- https://developer.mozilla.org/ko/docs/Web/API/Fetch_API/Fetch%EC%9D%98_%EC%82%AC%EC%9A%A9%EB%B2%95