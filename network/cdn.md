# CDN (Contents Delivery Network)

> 사용자와 가까운 곳에 위치한 Cache Server에 해당 Content를 저장(캐싱)하고 Content 요청시에 Cache Server가 응답을 주는 기술

> CDN은 오리진이라고도 불리는 콘텐츠 서버와 엔드유저(클라이언트) 사이에서 컨텐츠를 전달하는 역할

### 목적: high availability and high performance

### 장점
- Origin의 트래픽 부하를 줄임
- 빠른 응답으로 인해 Client의 웹 경험 개선

### 작동원리

![CDN 작동원리](https://cdn.hosting.kr/wp-content/uploads/2017/03/How-CDN-works-flow.png)

- ISP(Internet Service Provider) 측에 CDN 서버 설치. 최적의 경로로 컨텐츠 전달 (e.g., 사용자의 가장 가까운 지점)
- 전송가능한 컨텐츠: 디지털화 할 수 있는 모든 데이터
- Load Balancing & Synchronization

### Caching
- Static
  - Origin의 운영자가 미리 Cache Server에 복사함
  - 사용자가 Cache Server에 컨텐츠를 요청하면 항상 hit
- Dynamic
  - 최초 요청 시, Cache Server에 Contents 없음
  - Cache miss 시, Origin으로 부터 다운받아 전달
  - 이 후 요청 부터는 Cache hit

---
## Reference
- https://ko.wikipedia.org/wiki/%EC%BD%98%ED%85%90%EC%B8%A0_%EC%A0%84%EC%86%A1_%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC
- https://cdn.hosting.kr/cdn%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80%EC%9A%94
- https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability