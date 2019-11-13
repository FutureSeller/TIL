# PKI (Public Key Infrastructure): 공개 키 기반 구조

> 공개 키 암호 방식을 바탕으로 한 디지털 인증서를 활용하는 소프트웨어, 하드웨어, 사용자, 정책 및 제도 등을 총칭하여 일컬음

#### 하는 일
- 인증서 발급
- 인증서 관리
- 인증서 배포
- 인증서 사용
- 인증서 저장
- 인증서 취소

#### 구성요소
- CA(Certification Authority); 인증기관: 디지털 인증서를 발급하고 검증하는 기관
- RA(Registration Authority); 등록기관: CA의 위임을 받아 등록/분배등 사용자와 접촉 필요한 부분을 담당하는 기관
- Directory; 디렉토리: PKI 관련 정보들을 저장 및 검색하는 장소
- End Entity; 사용자: 인증서와 비공개키를 소지. 요청하는 주체

---
## Reference
- https://ko.wikipedia.org/wiki/%EA%B3%B5%EA%B0%9C_%ED%82%A4_%EA%B8%B0%EB%B0%98_%EA%B5%AC%EC%A1%B0
- http://wiki.wikisecurity.net/wiki:pki