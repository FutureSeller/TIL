## Caching
- 목적: 이미 fetch된 리소스들을 어딘가에 저장해 latancy/traffic을 줄임
- 종류: "어딘가"에 따른
  - Shared Cache: 많은 사용자들에 의해 공유되어 사용됨 (CDN....)
  - Private(Local) Cache: `single user`를 위한 cache (Browser....)
- Target: `GET`이 주로 caching의 대상. 적절한 헤더 사용 시 다른 method도 사용 가능(POST)
- Cache-Control
  - `Cache-Control: no-store`
    - No caching: 말 그대로 매번 서버로부터 download.
    - revalidate: cache가 release되기 전, 유효한 cache인지 재검증
  - `Cache-Control: public`
  - `Cache-Control: private`
  - `Cache-Control: max-age=<seconds>`
- ETags
- If-None-Match

---
## Reference
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching