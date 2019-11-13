# 암호학 (Cryptography)

### 용어 설명
- plaintext (평문): 보호해야할 메세지
- ciphertext (암호문): 평문을 암호학적 방법으로 변환한 것
- encryption (암호화): 평문을 암호문으로 변환하는 과정
- decryption (복호화): 암호문을 다시 평문으로 변환하는 과정

```
[plaintext] --- encryption ---> [ciphertext] --- decryption ---> [plaintext]
```

### 목표
- Confidentiality (기밀성): 허가받은 자가 아니면 내용을 알 수 없어야 함
- Integrity (무결성): 허가받은 자가 아니면 내용을 변경할 수 없어야 함
- Availability (가용성): 부적절한 서비스 거부 방지
- Non-repudiation (부인봉쇄): 전달하거나 잔달 받은 자가 해당 사실을 부인할 수 없어야함

### 대칭키 암호 시스템 (Symmetric-key Cryptography)
- encryption & decryption 할 때, 사용하는 키가 동일함
- 키의 길이가 길 수록 안전성 높음. but, 관리의 어려움이 커짐
- 키를 비밀리에 관리해야 함. 폐쇠적 특성을 갖는 그룹에 적합
- 문제점
  - 가입한 사용자들 사이에 하나의 서로 다른 키를 공유해야함 
  - n 명이 가입했으면 총 n(n-1) / 2개 만큼의 키가 필요 (시스템)
  - n - 1개의 키를 관리해야함 (사용자)
- DES(Data Encryption Standard), AES(Advanced Encryption Standard) 등. 각각은 나중에 자세히 볼 예정

### 공개키 암호 시스템 (Public-key Cryptography)
- 사용자는 두 개의 키를 부여 받음
  - 다른 사용자들에게 공개될 공개키(public key)
  - 사용자에 의해 비밀리에 관리되어야 할 비밀키(private key)
- 각 사용자는 자신의 비밀키만 관리하면 되므로, 키 관리의 어려움을 줄일 수 있음
- 공개키를 관리하는 공개키 관리 시스템이 필요: 다른 사용자의 공개키를 열람할 수 있어야 함
- 일반적으로, encryption: public key, decryption: private key

#### 알고리즘
- 각각이 갖는 알고리즘과 키 생성 시 다른 특징을 가지고 있음
- 대표적으로 RSA(Revest-Shamir-Adleman)

---
## Reference
- https://ko.wikipedia.org/wiki/%EC%95%94%ED%98%B8%ED%95%99