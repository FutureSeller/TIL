# JWT (JSON Web Token)

- JSON 객체를 사용하여 가볍고 self-contained 방식으로 정보를 전달해줌
  - 디지털 서명을 통해 검증 가능: secret + HMAC
  - public/private key pair using RSA or ECDSA
  - self-contained: 필요한 정보를 모두 담고 있음
    - 전달하고자하는 정보, signature, 검증에 필요한 정보들
  - 헤더에 넣을 수도 있고, URL의 파라미터로 전달 할 수도 있음 
- [RFC 7519](https://tools.ietf.org/html/rfc7519)

### 왜 생겨났는가? a.k.a. 세션 기반 인증의 문제점 + 모바일
- 세션 기반 인증의 문제점
  - 세션을 유지할 때, 서버 측에 무리를 줄 수 있음
  - 요새는 Framwork들이 잘 나와있지만, 확장 및 동기화가 어려울 수 있음
  - 쿠키에 박아서 내려줘야하므로 CORS를 신경쓰는게 번거로울 수 있음
- 그리고, HTTP는 근본적으로 Stateless 프로토콜임
  - 토큰 기반 인증에 잘 맞음 (stateless)
  - 서버 확장에 유리 (토큰만 검증하면 되니까)
  - 플랫폼간 권한을 공유할 수 있음 (authorization 까지 잡을 수 있음)
  - **모바일에서 사용하기 편해짐 (API 헤더에 넣어서 사용해주면 됨)**

### 사용하는 목적
- Authorization (회원 인증)
  - 서버가 클라이언트에게서 요청을 받을 때마다, 토큰을 검증
  - 권한이 있는지 확인하여 작업을 처리
  - **서버에서 세션을 유지할 필요가 없음**
- Information Exchange
  - 서명되어있어 무결성을 검증할 수 있음

### 구조

```
[Header].[Payload].[Signature]
```

#### Header
- Base64Url로 encoding됨
- Properties
  - `alg`: 해싱 알고리즘; 서명에 사용될 알고리즘; HMAC SHA256 or RSA
  - `typ`: 토큰의 타입; JWT

#### Payload
- 토큰에 담을 정보가 들어있음
- claim 들로 구성되어 있음; key:value pair
  - registered
    - 토큰에 대한 정보를 담기위한 클레임
    - e.g., iss(issuer), exp(expiration time), sub(subject) ...
  - public
    - 충돌이 방지된 이름을 가져야함. 보통 URI 형식으로 지음
    - e.g., `{ "https://example.com/jwt_claims/is_admin": true }`
  - private
    - 클라이언트와 서버간에 사용되는 클레임들
    - e.g., `{ "username": "FutureSeller" }`

``` json
{
  "iss": "example.com"
  "exp": "15820698234095",
  "https://example.com/jwt_claims/is_admin": true,
  "userId": "12394190238481324",
  "username": "FutureSeller"
}
```

자세한 내용은 [link](https://www.iana.org/assignments/jwt/jwt.xhtml) 를 참고

#### Signature
헤더에 정의된 서명부분의 해싱 알고리즘을 토대로 encoding된 헤더와 페이로드와 `secret`으로 서명을 생성함

```
signature = base64UrlEncode(
  HMACSHA256(
    base64UrlEncode(header) + '.' + base64UrlEncode(payload),
    secret
  )
)
```

```javascript
const crypto = require('crypto')
const signature = crypto.createHmac('sha256', 'secret')
  .update(encodedHeader + '.' + encodedPayload)
  .digest('base64')
  .replace('=', '')
```

이는 메시지의 무결성을 증명하는데 쓰이며, 보통 private key로 서명됨

### 클라이언트에서 JWT 보관하기 (feat. 어디에 토큰을 저장해야 할까요?)

#### 1. 로컬스토리지에 저장
- local/sessionStorage 객체에 접근이 되기때문에 XSS로 인해 도난 당할 위험이 있음
- 서버에 비동기적 요청을 할 때, 로컬스토리지에서 꺼내어 헤더에 토큰을 추가해줘야함

#### 2. 쿠키에 저장 (httpOnly + secure)
- httpOnly: JavaScript로 접근 및 확인을 못하도록 함
- secure: https 에서만 활성화되는 쿠키
- XSS를 예방할 수있으나 CSRF 문제가 있을 수 있음
- CSRF 토큰을 쓴다거나 레퍼러 체크를 한다거나 등등을 통해 해소

---
## Reference
- https://jwt.io
- https://blog.outsider.ne.kr/1160
- https://velopert.com/2389
