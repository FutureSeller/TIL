# REST API(Representational State Transfer API)

- 자원(Resource): URI
  - 리소스 명은 동사보다는 명사를 사용 `GET /members`
- 행위(Verb): HTTP METHOD
  - GET, POST, PATCH, PUT, DELETE, etc.
  - e.g., `DELETE /members/1`, `GET /members/1`, `POST /members {body}`
- 표현(Representations)
  - `/`로 계층관계를 나타냄. 마지막 문자로 `/`를 포함하지 않음
  - `-`을 사용하되 `_` 사용을 지양
  - 소문자; 확장자는 포함시키지 않음
    ```
    GET /document HTTP/1.1 
    Host: example.com 
    Accept: text/plain or text/csv 등등...
    ```
  - 리소스간 관계
    - e.g., `GET /members/{userId}/devices` (has 관계를 표현할 때)
    - 관계명이 복잡하다면, 서브 리소스에 명시적으로 표현; e.g., `GET /members/{userId}/likes/devices`
  - Collection and Document
    - 복수와 단수로 구분지어주는 것이 좋음
    - e.g., `GET /sports`, `GET /sports/baseball`
  - 즉, HTTP Header를 잘 사용하면 됨
- Response: HTTP Response code로 시맨틱을 고려해 적절히 구성

> RESTful: REST를 따르는 시스템 

### 특징
- Uniform: URI로 지정한 리소스에 대한 조작을 통일되고 한정적인 인터페이스로 수행하는 아키텍처 스타일
- Stateless: 세션 정보나 쿠키정보를 별도로 저장하고 관리하지 않음
- Cachable: e.g,  Last-Modified, E-Tag
- Self-descriptiveness: REST API 메시지만 보고도 이를 쉽게 이해 할 수 있는 자체 표현 구조
- Client - Server: 서버는 API 제공; 클라이언트는 사용자 인증이나 컨텍스트(세션, 로그인 정보)등을 직접 관리
- 계층형구조: 보안, 로드 밸런싱, 암호화 계층을 추가해 구조상의 유연성을 둘 수 있고 PROXY, 게이트웨이 같은 네트워크 기반의 중간매체 사용가능

---
## Reference
- https://meetup.toast.com/posts/92
- https://stackoverflow.com/questions/41189842/what-is-difference-between-rest-and-api
