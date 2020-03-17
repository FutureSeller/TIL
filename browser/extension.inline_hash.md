크롬 익스텐션에서 inline script를 쓰려면 security 이슈로 인해 사용해야할 inline script의 hash 값을 비교하여 사용하도록 한다.
해당 hash 값은 `string -- (sha256) -- (base64) --> hash` 다음과 같이 구해진다.

```bash
echo -n "alert('Hello, world.');" | openssl dgst -sha256 -binary | openssl enc -base64
```

해당 값을 manifest의 `content_security_policy'에 추가하면 사용할 수 있다.
