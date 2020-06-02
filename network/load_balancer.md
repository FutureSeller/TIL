# Load Balancer (로드 밸런서)

> 트래픽 분산을 통해 부하를 줄이는 것을 목표로하는 네트워크 장비 혹은 플랫폼

#### 기능 / 특징
- Service Discovery: 로드 밸런서가 사용가능한 백엔드들을 결정
  - Static config file
  - DNS
  - Zookeeper, Etcd, Consul 등
  - Envoy's universal data plane API
- Health Checking: 로드 밸런서가 트래픽을 처리하는데 특정 백엔드를 사용할 수 있는지 결정
  - Active: 주기적인 간격을 두고 상태를 측정 (e.g., /healthcheck)
  - Passive: 데이터 흐름을 보고 상태를 감지 (e.g., 연결 오류 threshold를 두고 넘는지 확인)
- Load Balancing: 모든 정상적인 백엔드에 부하 균형을 맞추기 위해 사용하는 알고리즘
  - Round robin
  - random selection
  - power of 2 least request load balancing
- Sticky Sessions: 특정 앱들에 한해, 같은 세션에 의한 요청은 같은 백엔드에 도달하는 것이 중요하기 때문
  - e.g., HTTP cookies, properties, attributes
  - 디자인을 잘해야 안정적임
- TLS termination: e.g., 인증서 확인 / pinning / SNI
- Observability: 통계, 추적 및 로깅
- Security and DoS Mitigation
  - rate limiting
  - authentication
  - IP address tagging and identification
- Configuration and control plane

#### 이점
- 네이밍 추상화: 클라이언트가 Name resolution 작업을 로드밸런서에 위임함
- 장애 허용: 상태 확인 및 알고리즘을 통해 효율적으로 백엔드로 라우팅
- 비용 및 성능 이점

## L4(connection/session) 로드 밸런싱

![L4 Load Balancing](https://miro.medium.com/max/1400/1*1PjTpM3hLnm3iEAd4-_AaQ.png)

- 클라이언트: 로드 밸런서에 TCP를 통해 연결함
- 로드 밸런서: 연결을 종료하고(SYN을 직접 응답), 백엔드를 선택한 다음 새 UDP/TCP 연결을 만듬 (새로운 SYN을 전송)
- L4 단에서 다뤄지기때문에, bit/byte 단위의 연산이 빈번하게 발생됨.
- 상위 단(L5~L7)의 프로토콜로 어떤 byte가 어떤 필드를 의미하는지 알 수 없음

### 종류

#### TCP/UDP termination 

![term](https://cdn-images-1.medium.com/max/1600/1*1PjTpM3hLnm3iEAd4-_AaQ.png)

- `클라이언트 - 로드 밸런서`, `로드밸런서 - 백엔드` 서로 다른 두 개의 TCP 연결이 사용됨
- 구현이 쉬움

#### TCP/UDP passthrough

![pass](https://cdn-images-1.medium.com/max/1600/1*mf0S8BrWjxSBU-mP4ZpC9A.png)

- TCP 연결이 로드 밸런서에 의해 종료되지 않으며 트래킹 및 NAT이 수행된 후, 각 연결에 대한 패킷이 백엔드로 전달됨
  - Connection Tracking: 모든 active한 TCP 커넥션의 상태를 추적하는 프로세스
  - NAT: Connection Tracking 데이터를 사용하여, 로드 밸런서 통과시 패킷의 IP/Port 정보를 변경하는 프로세스
- Flow
  - 클라이언트는 로스밸런서를 가리킴, 백엔드는 특정 Origin을 가짐
  - 클라이언트의 패킷이 로드밸런서에 도착
  - 로드밸런서는 패킷의 목적지 IP 및 포트를 백엔드의 Origin으로 교환 + 패킷의 소스 IP를 로드밸런서 주소로 교환
  - 백엔드에서 응답 시, 로드 밸런서로 보내고 NAT은 역방향으로 수행됨

#### DSR (Direct Server Return)

![dsr](https://cdn-images-1.medium.com/max/1600/1*4IW2Y8SvovEMrWpuZA-mtg.png)

- 요청 패킷만 로드 밸런서를 통해 전달되는 최적화 (e.g., 요청의 크기는 10MB인데 응답의 크기가 100MB? => 병목이 생김)
- 트래픽 흐름을 제어해 큰 사이즈의 응답 패킷이 나갈 때 로드 밸런서를 거치지 않고 서버가 클라이언트로 보냄
- NAT 대신 Generic Routing Encapsulation(GRE)를 사용
  - 로드 밸런서에서 백엔드로 전송되는 패킷을 캡슐화
  - 백엔드가 캡슐화된 패킷을 받아 해석하면 클라이언트의 주소를 알 수 있어 응답 가능
- 백엔드가 로드 밸런싱에 참여: GRE 터널이 올바르게 구성되어 있어야 함

#### Fault tolerance via high availability pairs

![pair](https://miro.medium.com/max/1400/1*dgVKtmARcboQe0up5dQiBQ.png)

로드 밸런서가 단일 인스턴스인데 죽으면 로드 밸런서를 통과하는 모든 연결이 상실됨. 이를 방지하기 위해 여분을 둠.
이 이상의 설명은 생략...하자..


## L7 로드 밸런싱

- multiplexing: 단일 L4 연결을 통해 concurrent application이 요청을 보내는 것
- kept-alive: active request가 없음에도 커넥션을 끊지 않는 것

최근 프로토콜들은 두 가지를 성능상 이점을 얻기 위해 가져가고 있다. 커넥션을 맺는 것, 특히 TLS 커넥션을 맺는데 많은 비용이 들기 때문이다.

![L7 Load Balancing](https://cdn-images-1.medium.com/max/1600/1*zsaxjSziEm1Tipr6kxs5Zg.png)

- 클라이언트: 로드 밸런서에 단일 HTTP/2 TCP 커넥션을 맺음
- 로드 밸런서: 두 개의 백엔드 커넥션을 생성
- 이 후 클라이언트로부터 전송된 각각의 HTTP/2 stream은 논리적 구분에 따라 백엔드로 각각 분산됨

## 로드 밸런서 토폴로지의 종류

#### Middle Proxy
- *simplicity*: 클라이언트는 DNS를 통해 로드 밸런서와 커넥션을 맺은 뒤 아무것도 안해도 됨
- 로드밸런서가 단일 장애 지점이며, bottleneck이 될 수 있음 + 블랙박스라 어디서 문제인지 알기 어려울 수 있음

#### Edge Proxy
- 인터넷을 통해 로드 밸런서에 접근할 수 있는 중간 프록시 토폴로지의 변형
- API 게이트웨이 기능 제공: 이 때 로드 밸런서가 TLS termination, 인증 및 트래픽 라우팅 등

#### Embedded client library
- 라이브러리를 통해 로드 밸런서를 서비스에 직접 내장
- 로드 밸런서의 모든 기능을 각 클라이언트에 분산하여, 단일 장애 지점 이슈 및 확장성 이슈 제거
- 라이브러리를 모든 언어로 구현 + 모든 서비스에 라이브러리 관리를 해줘야 함

#### Sidecar proxy
- 앱의 변경 없이 독립적으로 동작하는 프록시를 뗐다 붙였다 하는 형식
- 프로세스간 통신에 약간의 latency 손해를 보지만 Embedded와 비교했을 때 관리가 편함
- Envoy, NGINX, HAProxy 등등이 있음


---
## Reference
- https://blog.envoyproxy.io/introduction-to-modern-network-load-balancing-and-proxying-a57f6ff80236?gi=5fe7f08e3eee
- https://smashingpumpkins.tistory.com/entry/DSRDirect-Server-Return%EC%9D%B4%EB%9E%80
