# Electronic Signature (전자서명)

> 서명자를 확인하고 서명자가 당해 전자문서에 서명했다는 사실을 나타내는 데 이용하려고, 특정 전자문서에 첨부되거나 논리적으로 결합된 전자적 형태의 정보

### 기술 기반
- Hash function: 무결성 확인을 위함 (변조 여부 확인, MD5, SHA1, SHA256 등)
- Public-key Cryptography (해시 값을 공개키 암호화)

#### Flow (Vulnerable)
- 배포: 서명, 공개키를 포함
  - [바이너리] --- hash function ---> **[해시 값(H)]**
  - [해시 값(H)] --- encrypt using private key ---> **[서명(S)]**
  - **[공개키]**
  - 크게 보면: [바이너리] --- signing ---> [signed 바이너리(공개키 + 서명 + 바이너리)]

```
Hash(B1) => H1;
Encrypt(KeyPrivate, H1) => S;
C1 = { B1, KeyPublic, S }
```

- 검증: 서명과 공개키를 분리 하고 구한 해시 값과 비교
  - [signed 바이너리] --- 분리 ---> [바이너리], [서명], [공개키]
  - [서명(S)] --- decrypt using public key ---> **[해시 값(H')]**
  - [바이너리] --- hash function ---> **[해시 값(H'')]**
  - H'와 H''가 일치하면 원본 바이너리와 일치함을 알 수 있음

```
{ B1, KeyPublic, S } = C1;
Decrypt(KeyPublic, S) = H1';
Hash(B1) = H1'';
H1' === H1'' => Success
```

#### 공인인증서
- 위의 코드사인 과정을 해커가 wrapping해서 한 번 더 수행하면 우회할 수 있음
  - 한 번 코드사인 된 그 자체를 Original Binary로 보고, 해커의 Public Key를 심음
  - 해커의 코드사인을 기준으로 검증하기 때문

> 복호화 키인 공개키를 파일 형태로 만들어 놓은 것 + 서명을 한 주체를 확인

![인증서 기본 구조](https://d2.naver.com/content/images/2015/06/helloworld-744920-4.png)

- 일반적으로 알려진 신뢰할 수 있는 공인 인증 기관에 공개키와 기타 정보를 등록
- 주체, 주체의 공개키, 발급자, 그리고 발급자의 서명 등
- 발급자의 서명은 발급자의 복호화키로 환원. 결국 믿을 수 있을만한 기관에 한단계 인증을 더 추가한 셈

#### Flow (Extended, Only diff): 공개키가 인증서로 대체된 것
- 배포: [서명] + [인증서] + [바이너리] --- composition ---> [Signed 바이너리]
- 검증: 발급자의 공개키를 사용. 인증서부터 검증: 인증서 주체부터 확인 후 공개키 얻음
  
---
## Reference
- https://d2.naver.com/helloworld/744920
- https://ko.wikipedia.org/wiki/%EC%A0%84%EC%9E%90%EC%84%9C%EB%AA%85