# HTTP(Hypertext Transfer Protocol)
- Hypertext, 나아가 Hypermedia를 주고받기 위한 프로토콜 based on TCP/IP(애플리케이션 레벨) 
- 신뢰할만한 전송 혹은 세션 레이어의 연결을 통해 메세지를 주고받는 상태가 없는 요청/응답 프로토콜
- WWW 상에서 정보를 주고 받을 수 있는 프로토콜
- 클라이언트: 서버와 연결을 맺고 하나 이상의 HTTP 메시지를 보내는 프로그램
- 서버: 클라이언트의 연결을 수락하고 HTTP 요청을 처리하여 응답을 보내주는 프로그램

## HTTP의 기본적인 특징
- "Connectionless": 클라이언트가 서버에 요청을 한 뒤, 서버가 클라이언트에게 응답을 보내면 접속을 끊음
- "Stateless": 서버와 클라이언트의 통신이 끝난 뒤, 클라이언트의 상태 정보를 유지하지 않음
- "Media Independent": 데이터와 그에 맞는 Content-Type만 넘겨주면, 핸들 할 수 있음

## HTTP 메시지
- ASCII로 인코딩된 텍스트 정보이며 여러줄로 되어있음
- 요청(Request): 클라이언트가 서버로 전달해서 서버의 액션이 일어나게끔 하는 메시지
- 응답(Response): 요청에 대한 서버의 답변
- 구조
  - 시작 줄(start-line): 실행되어야 할 요청, 요청 수행에 대한 성공 또는 실패
    - HTTP Methods: 서버가 수행해야할 동작
    - 요청 타겟: URL, 프로토콜, 포트, 도메인의 절대 경로
    - HTTP 버전
  - HTTP Header: 요청에 대한 설명, 메시지 본문에 대한 설명
  - 빈 줄(blank line): 요청에 대한 모든 메타 정보가 전송되었음을 알림
  - 본문: 응답과 관련된 문서, 일부 요청은 본문이 필요가 없음

```
POST / HTTP/1.1
Host: localhost:8000
User-Agent: Mozilla/5.0 ...
Accept: text/html,application/xhtml+xml,...
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, defalte
Connection: keep-alive
Content-Type: multipart/form-data; boundary=...
Content-Length: 345

-12659794

----

HTTP/1.1 403 Forbidden
Server: Apache
Content-Type: text/html; charset=iso-8859-1
Date: Web, 10 Aug 2016 09:23:25 GMT
Keep-Alive: timeout=5, max=10000
Connection: Keep-Alive
Age: 3464
Content-Length: 220
```
---

## Questions
#### 1. HTTP는 왜 생겼을 까? 그냥 원래 있던 Protocol들 쓰면 안되나?
- 결론적부터 말하자면, 기존에 있던 프로토콜이 WWW 상에서 Hypertext를 주고 받는 것에 맞지 않았기 때문
- 프로토콜은 본래 각각의 목적을 달성하기 위해 만들어짐
- HTTP의 목적을 다시 생각해 봐야함 
  - Hypertext를 주고 받기에 적합해야함
  - Hyperlink를 통해 다른 서버로 연결할 수 있어야 함
  - WWW 상에서 수많은 클라이언트들이 사용할 수 있어야 함
  - 그러려면, 사용하기도 쉽고 알아보기 쉬워야함

#### Q2. Stateless 하다는데? UDP 써도 될 것 같은데?  왜 TCP를 썼지?
- HTTP는 "Reliable Transport"를 전제로 함. 즉, TCP의 Reliable한 점을 높게 샀음
- 즉, 요청한 자원을 Reliable하게 반환해줘야 함
- 선택의 문제. 잘 만들어진 TCP를 두고 위험부담을 하고싶지 않았을 수도(추측)
- 정말 불가능한가?
  - UDP위에 덧붙여서 구현하면 되는거 아닌가? 물론, 서버도 좀 복잡해 지겠지만
  - "QUIC(Quick UDP Internet Connections)"을 나중에 다뤄볼 것

#### Q3. HTTP 메시지의 body는 왜 ASCII를 사용할까?
- Plain text라 보안적으로 취약한 치명적인 단점이 있음: 중간에서 헤더를 변조한다거나 body를 변조한다거나
- HTTPS가 나오긴 했지만, 근본적인 문제가 있는데 왜 ASCII를 사용했을까? Binary 형태로 보내도 됐을텐데?
```
# 1
A reason that's both technical and historical is that text protocols are almost always preferred in the Unix world.
Well, this is not really a reason but a pattern. 
The rationale behind this is that text protocols allows you to see what's going on. 
You don't need a specialized analyzer as you need for TCP/IP. 
This makes it easier to debug and easier to maintain.

# 2
With HTTP, the content of a request is almost always orders of magnitude larger than the protocol overhead. 
Converting the protocol into a binary one would save very little bandwidth, 
and the easy debugability that a text protocol offers easily trumps the minor bandwidth savings of a binary protocol.
```
- 특별하거나 큰 이유는 없는 것 같음(추측)
  - 예전 부터 그렇게 해왔으니까(Unix world에서 선호했다고 함)
  - 읽기 쉽고 분석/유지보수하기 편하니까

--- 
## Appendix
### Terminology
- Hyperlink: 하이퍼텍스트 문서 안에서 직접 모든 형식의 자료를 연결하고 가리킬 수 있는 참조 고리
- Hypertext: 하이퍼링크를 통해 독자가 한 문서에서 다른 문서로 즉시 접근 할 수 있는 텍스트
- Hypermedia: 하이퍼텍스트 + 그래픽, 오디오, 영상등을 포함하여 정보를 구성한 것
- WWW(World Wide Web): 인터넷에 연결된 컴퓨터를 통해 사람들이 정보를 공유할 수 있는 전 세계적인 정보 공간
- TCP(Transmission Control Protocol)
- UDP(User Datagram Protocol)
- IP(Internet Protocol)
- SMTP(Simple Mail Transfer Protocol): 인터넷에서 이메일을 보내기 위해 이용되는 프로토콜
- FTP(File Transfer Protocol): TCP/IP를 가지고 서버와 클라이언트 사이 파일 전송을 위한 프로토콜

## Reference
- https://developer.mozilla.org/en-US/docs/Web/HTTP
- https://www.w3.org/Protocols/WhyHTTP.html
- https://www.w3.org/Protocols/DesignIssues.html
- https://www.tutorialspoint.com/http/http_overview.htm
- https://stackoverflow.com/questions/393407/why-http-protocol-is-designed-in-plain-text-way
