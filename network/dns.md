# DNS (Domain Name System)
> 호스트의 도메인 이름을 호스트의 네트워크 주소로 바꾸거나 그 반대의 변환을 수행할 수 있도록 하기 위해 개발

> 네트워크로 연결된 임의의 장치의 주소를 찾기 위해, 사람이 이해하기 쉬운 도메인 이름을 숫자로 된 식별 번호(IP 주소)로 변환해 줌

## Background: /etc/hosts
- 너무 당연하게도 처음부터 DNS가 있었던 것은 아님
- IP Address는 사람이 기억하기 어려움. human-readable한 체계 필요
- Map; key-value pair: `ip:domains`를 직접 파일에 등록했어야 함
- 점점 규모가 커지면서 관리하기 힘들어짐 + 보안 문제 대두
- 지금도 쓰려면 쓸 수 있음(개발할 때 편함). DNS lookup하기 전에 해당 파일을 먼저 읽고 커넥션을 맺음

#### Domain name syntax, internationalization
- Top-level domain (TLD): 도메인 네임의 가장 마지막 부분
  - 일반 최상위 도메인 (gTLD): `.com, .net, .org, .edu, .gov, .mil`
  - 국가 코드 최상위 도메인 (ccTLD): `.kr, .co.kr`
- Second-level domain (SLD): TLD 하위 단계
- Subdomains : 나머지
- LDH Rule (Letters, Digits, and Hyphen), Case-independent

#### Name servers
- Client/Server Model
- DNS 데이터베이스(RR의 집합)를 가지고 있으며, IP 주소를 요청하는 클라이언트에 정보 제공
- Root 네임 서버
  - TLD(Top-level domain)의 각 권한이 어느 네임 서버에 있는지 알 수 있음
  - 전 세계에 13개 존재 (http://www.iana.org/domains/root/servers)
  > Before, there was only one single server for each of the 13 IP addresses, 
    while today we have a server cluster for each of them—creating a network of hundreds of servers all around the world which use anycast routing.
- Authoritative 네임 서버
  - DNS 요청에 응답하는 네임 서버. IP 주소를 저장, 수정, 삭제하는 기능
  - Primary(모든 레코드의 최종 버전정보 저장) / Secondary(백업 및 동기화)
- Caching 네임 서버 (DNS cache)
  - DNS 질의 결과를 TTL(Time-to-live)로 설정되는 시간동안 캐시에 저장
  - Root/Authoritative 네임 서버의 부하를 줄임

#### Domain name space
- DNS Zone (도메인 관리 영역)
  - DNS 트리의 특정(일부) 영역: 특정 지점의 하위에 존재하는 모든 도메인을 포함
  - Authoritative 네임 서버 하나가 책임이나 권한을 가지는 영역
  - 참고: [Root Zone](https://en.wikipedia.org/wiki/DNS_root_zone)
- [Resource Record](https://en.wikipedia.org/wiki/List_of_DNS_record_types); RR
  - 도메인 네임과 관련된 항목을 가지는 레코드 (이름-값)
  - Type
    - A: Address Record; 호스트명 및 IPv4 주소
    - NS: 네임 서버; Zone에 대한 네임 서버의 호스트명
    - CNAME: 호스트명의 alias

#### Operation
- Domain Name Resolution
- DNS Resolvers: 
  - `client side of the DNS`; 호스트에 대한 정보를 질의하고 응답으로부터 정보 추출
  - 디폴트 상태에서 OS 는 네트워크가 일러주는 리졸버를 그대로 사용
  - 컴퓨터를 네트워크에 연결하면 네트워크는 컴퓨터에 IP 주소를 할당하고 사용할 리졸버를 추천해줌
  - Recursive Query
    - Resolver가 Root DNS 부터 Authorative 네임 서버를 찾을때까지 다른 네임 서버들과 질의/응답
    - 클라이언트에게 응답 (answer or not found)
  - Iterative Query
    - Resolver의 질의에 응답하거나, 다른 DNS 서버에 클라이언트를 연결
    - 자신이 알 수 없는 질의에 응답 가능한 네임 서버의 목록 전달
    - 클라이언트가 다수의 DNS 서버들에 같은 질의 반복
- Reverse Lookup: IP주소를 가지고 도메인 이름을 얻는 것

#### Security
- Tracking
  - 사용자가 방문한 웹사이트 내역 추적
  - Resolver 의 데이터 수집 정책에 따라 악의적인 목적으로 사용될 수 있음
- Spoofing
  - DNS 서버 사이에 있는 누군가가 DNS 서버의 응답을 변경
  - 혹은 Resolver 자체가 광고등 악의적인 목적에 의해 조작
- Trusted Recursive Resolver (TRR)
  - 신뢰할 수 있는 Resolver를 벤더에서 제공
  - e.g., 24시간 마다 데이터 폐기, 제 3자에게 제공하지 않음 등
- DNS over HTTPS (DoH): MITM을 방지하고자 encrypt

---
## Reference
- https://en.wikipedia.org/wiki/Domain_Name_System, [ko](https://ko.wikipedia.org/wiki/%EB%8F%84%EB%A9%94%EC%9D%B8_%EB%84%A4%EC%9E%84_%EC%8B%9C%EC%8A%A4%ED%85%9C)
- http://hacks.mozilla.or.kr/2019/10/a-cartoon-intro-to-dns-over-https
- https://securitytrails.com/blog/dns-root-servers
- https://opentutorials.org/module/288/2802
- https://en.wikipedia.org/wiki/DNS_over_HTTPS