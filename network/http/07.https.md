# HTTPS (HyperText Transfer Protocol over Secure Socket Layer)
- Protocol: TLS(Transport Layer Security, 구 SSL)
- Port: 443
- Scheme: `https://`
- 보호의 수준: 웹 브라우저에서의 구현의 정확도, 서버에서 지원하는 암호화 알고리즘에 달려있음

## TLS(Transport Layer Security)
- 암호화 (Encryption)
- 데이터 무결성 (Data integrity): 데이터 손상 방지
- 인증 (Authentication): MITM 차단

### [Digital Certificates](http://www.ktword.co.kr/word/abbr_view.php?m_temp1=1004)
- 공개키 및 그 키를 소유한 사용자에 대해 신뢰할만한 제3자(인증기관)가 서명 발행한 것
- 공개키를 공인하는 전자적 증명서 (공개키 인증서)
- Certificate Authority (CA)
  - 다른 곳에서 사용하기 위한 디지털 인증서를 발급하는 하나의 단위
  - 인증 기관은 공개키 인증서를 발급하며, 이 인증서는 해당 공개 키가 특정 개인이나 단체, 서버에 속해 있음을 증명
  - 인증 기관의 의무는 인증서에 대한 정보를 사용자에게 확인시켜 주는 것

### Handshake
#### Basic TLS handshake (Full & Initial)
1\. Negotiation
  - [C]: `ClientHello` 메세지를 전송
    - 지원하는 가장 높은 버전의 TLS 프로토콜 버전
    - 키 생성을 위해 생성된 난수
    - cipher_suites
  - [S]: `ServerHello` 메세지로 응답
    - 선택된 프로토콜 버전(가장 높은 버전)
    - 키 생성을 위해 생성된 난수
    - 선택된 cipher_suites (기본적으로 가장 강력한 것)
    - `session ID`: 이 값을 보고 서버가 다시 재개할지 확인 및 허가. 없으면 생성해서 보내줌
  - [S]: `Certificate` 메세지 전송
    - 서버의 인증서와, 그 인증서를 확인한 CA들의 모든 인증서인 certificate chain 전송
  - [S]: `ServerKeyExchange` 메세지 전송
    - 서버와 클라이언트의 합의한 키 교환 방식이 DHE/DH_anon 일 때 서버의 key를 보냄
  - [S]: `ServerHelloDone` 메세지 전송: negotiation이 끝났음을 알림
  - [C]: `ClientKeyExchange` 메세지로 응답
    - `ServerHelloDone`을 받은 뒤, 서버의 인증서의 서명을 확인
    - 선택된 cipher에 따라 PreMasterSecret(서버의 certificate에 포함된 public key를 사용해 encrypt) 생성
    - 이 때, 서버는 서버의 private key를 사용하여 descryption
  - [C&S]: 서버와 클라이언트는 생성된 난수와 PreMasterSecret을 사용하여 `master secret` + `session key` 생성
2\. [C] `ChangeCipherSpec` 메세지 전송
  - `Finished`(authenticated and encrypted) 메세지를 전송 (MAC + hash): `session key`로 encrypt
  - 만약, 서버에서 decryption & verification이 실패하면 handshake는 실패한 것: `session key`로 decrypt
3\. [S] `ChangeCipherSpec` 메세지 전송
  - `Finished` 메세지를 전송
  - 클라이언트에서도 2와 동일하게 decryption & verification 성공하는지 봄

#### Client-authenticated TLS handshake: 양쪽의 certificate
- Negotiation 시
  - 서버가 `CertificateRequest` 메세지를 전송 후, `ServerHelloDone` 전송
  - 클라이언트가 `Certificate` 메세지 전송: client의 certificate이 포함되어 있음
  - 클라이언트가 `ClientKeyExchange` 전송. (`PreMasterSecret`은 서버의 public key로 encrypt)

#### Resumed TLS handshake
- Session ID나 Session tickets를 사용해 handshake를 간소화함
  - 서버 인증서 확인
  - cipher_suite 결정
  - 암호화 키 교환
- Session ID
  - 클라이언트와 서버가 같은 `master secret`을 가지고 있어야 함. 다르면 handshake는 실패
  - `ClientHello` 전송 시 포함되어 전송
  - `ServerHello` 에서 검증: 같으면 그대로 같은 값을 반환. 다르면 새로운 값 생성하여 반환
  - 이 후, `master secret`과 random한 값을 통해 key 생성하여 통신에 씀
- Session tickets
  - 서버와 클라이언트 모두 지원해야 사용 가능함
  - 서버가 Session ID의 map을 가지고 있자니 메모리를 너무 잡아먹음
    - 클라이언트가 저장 후 전달
    - 서버는 session-specific state를 알고 있으면 됨
  - 서버가 encrypt하고 verify 함

### History
- SSL 1.0, 2.0, and 3.0
- TLS 1.0, 1.1, 1.2, 1.3

---
## Reference
- https://support.google.com/webmasters/answer/6073543?hl=ko
- https://en.wikipedia.org/wiki/Transport_Layer_Security
- https://engineering.linecorp.com/ko/blog/best-practices-to-secure-your-ssl-tls
- http://www.ktword.co.kr/word/abbr_view.php?m_temp1=1004
- https://ko.wikipedia.org/wiki/%EC%9D%B8%EC%A6%9D_%EA%B8%B0%EA%B4%80