## 겪었던 상황

- next-auth apple oauth를 연동하다보면, redirect url(next-auth에선 callback url이라 부른다)이 제대로 동작하지 않는다. 이유는 단순하다.
- next-auth은 인증 토큰과 callback url을 쿠키에 저장한다. (정확한진 모르겠지만 cookie에 `next-auth.callback-url=blahblah` 이런식으로 )
- 이 쿠키의 정책은 기본이 HTTP only, secure, 그리고 `Same-site: Strict`이다. (사파리에선 좀 다르긴하다.)
- 무튼, 서비스의 도메인에 담아둔 쿠키가 apple oauth url를 타고 다니면서 origin이 달라지므로 `Same-site: Strict` 요것에 의해 싹 날아가게 된다.
- next-auth는 저 쿠키 값이 없으면, NEXTAUTH_URL로 리다이렉트 시켜버린다. 그래서 callback-url이 이상하게 동작하는 것 처럼 보인다

## 해결 방법
- 매우 찜찜하고 권장되진 않지만, `Same-site: none`으로 풀어줘야했다. 왜냐면 apple에 post로 던져서 lax가 무용지물이기 때문.
