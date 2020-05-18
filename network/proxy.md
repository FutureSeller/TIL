> 클라이언트가 자신을 통해 다른 네트워크 서비스에 간접적으로 접속할 수 있게 해주는 시스템이나 프로그램

- 목적
  - 보안: 익명성 + 역추적 방지 등등등등
  - 캐시를 통한 리소스 접근 속도 향상
  - 컨텐츠로의 접근 정책을 적용 혹은 차단 (e.g., 프록시의 모든 응답은 Origin Allow)
  - 사용률 기록 및 검사

## Forward Proxy

#### 주체
- C : Client
- FP : Forward Proxy
- S : Server

#### 왜? 언제 이걸 쓰면 좋을까?
- Client가 Server에 직접 접근 할 수 없는 상황일 때
  - 예시 1: Client 들이 Server에 접근하게 하고 싶지 않을 때. 즉, 관리자가 특정 요청들을 차단하고자 할 때 사용
  - 예시 2: Server가 Client를 blocking 했을 때, 우회하고자

#### Flow
- 클라이언트가 웹 서버에 접근 시, 요청이 중간의 Proxy 서버에 전달됨
- Proxy 서버는 그 요청을 웹 서버에게 전달하여 응답을 받아옴
- 기존의 요청: `C ============> S`
- Foward Proxy를 거쳤을 떄: `C ====== FP ======> S`


## Reverse Proxy

#### 주체
- C : Client
- RP : Reverse Proxy
- S : Server

#### 왜? 언제 이걸 쓰면 좋을까?
- 서버가 요청을 RP로만 받고 싶을 때
  - 대용량 트래픽을 서버가 감당할 수 없을 경우
  - 많은 서버를 증설해놓고 리버스 프록시를 설정하여 사용자가 서버에 방문하려 할 때 가까운 서버로 보냄
  - e.g., Load Balancer, CDN
- 서버의 관리자가 실제 서버를 공개적으로 공개하고 싶지 않을 때

#### Flow
- 클라이언트가 웹 서버의 주소가 아닌 Reverse Proxy로 설정된 주소로 요청
- Proxy 서버가 받아서 그 뒷단의 웹 서버에게 다시 요청
- 클라이언트는 웹 서버의 정보를 알 수가 없음

## X-Forwarded-For (XFF)
> 프록시나 로드 밸런서를 통해 HTTP Server에 요청한 client의 IP를 식별하기 위한 표준

#### 왜? 
- 중간에 프록시나 로드밸런서를 거치면 서버 로그엔 해당 IP만 남기 때문에 클라이언트의 IP를 보기 위해 사용됨
- 즉, 디버깅, 통계, 위치 종속적인 컨텐츠를 위해 사용됨

```
X-Forwarded-For: <client>, [<proxy>].join(,)
```

---
## Reference
- https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9D%EC%8B%9C_%EC%84%9C%EB%B2%84
- https://stackoverflow.com/questions/224664/whats-the-difference-between-a-proxy-server-and-a-reverse-proxy-server
- https://i.stack.imgur.com/0qpxZ.png
- https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/X-Forwarded-For
