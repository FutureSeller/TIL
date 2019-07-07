## Cookie
- 서버가 클라이언트에 전송, 클라이언트에 저장되는 키와 값(Pair)
- 동일한 서버에 재 요청시 저장된 데이터를 함께 전송
- 서버가 `Set-Cookie`헤더를 통해 클라이언트로 전송: `Set-Cookie: yummy_cookie=choco`
- 목적: 세션 관리, 개인화, 트래킹
- 저장되는 정보
  - 이름: `yummy_cookie`
  - 값: `choco`
  - 만료 날짜: `Expires=Wed, 21 Oct 2015 07:28:00 GMT;`
  - 경로 정보: `Path=/Cookie`, `Domain=test.org`
- 구분
  - 만료 기간에 따른 구분
    - 세션 쿠키: Expires 혹은 Max-Age를 명시하지 않을 경우, 클라이언트 종료 시 삭제됨
    - 영속적인 쿠키: Expires, Max-Age 이후에 만료되는 쿠키 
  - Secure & HttpOnly
    - Secure: HTTPS 프로토콜 상에서 요청할 경우에만 전송됨
    - HttpOnly: `document.cookie`에 접근 불가. 서버에게 전송되기만 함
- Scope
  - `Domain`
    - 쿠키가 전송되게 될 호스트들
    - 명시되지 않으면 서브도메인 포함안됨
    - 명시될 경우, 서브도메인들은 항상 포함됨
    - `Domain=test.org`면 `a.test.org`등에 대해서도 전송됨
  - `Path`
    - Cookie  헤더를 전송하기 위해 URL 내에 반드시 존재하는 URL 경로
    - "/(%2f)"가 구분자
    - 지정된 경로의 하위경로들은 모두 매치됨
    - `Path=/Cookie`면 `/Cookie/a, Cookie/a/b`등에 대해서도 전송됨
- ETC
  - First-party cookie: 현재 window의 도메인과 쿠키의 도메인이 같음
  - Third-party cookie: 도메인이 다름
  - Do-Not-Track: DNT 헤더. ```navigator.doNotTrack; // 0 or 1```

## Session
- 방문자가 웹 서버에 접속해 있는 상태의 Unit
- 일정 시간동안 클라이언트의 일련의 요구를 하나의 상태로 보고, 일정하게 유지시킴
- "서버"에서 Unique한 id를 생성한 뒤 저장되며, 서버에서 검증 필요
- 클라이언트의 "쿠키"를 사용하여 세션 id를 저장한 뒤, 서버의 값과 비교함

---
## Questions
- Q1. 왜 이름이 쿠키죠?
  - 프로그램이 수신 후 변경하지 않은 채 반환하는 패킷인 매직 쿠키에서 비롯됨
- Q2. 왜 필요한가? 
  - HTTP는 Connectionless & Stateless: 서버가 Client를 식별할 수 있는 방법이 필요
  - 만약 없으면? 페이지를 이동할 때마다 로그인 해야함
- Q3. Cookie vs Session. 무엇이 다른가?
  - 저장 위치: 클라리언트 vs 서버
  - 라이프 사이클
    - 쿠키: 명시된 만료날짜 혹은 클라이언트가 종료될 때
    - 세션: 클라이언트가 접속을 끊었을 때, 혹은 서버의 로직에 따라 달라질 수 있음

## Reference
- https://developer.mozilla.org/ko/docs/Web/HTTP/Cookies
- https://ko.wikipedia.org/wiki/HTTP_%EC%BF%A0%ED%82%A4
