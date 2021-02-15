# Access-Control-Allow-Headers

CORS는 참 좋은데 개발할 수록 참 귀찮은 녀석이긴하다. 
가끔 개발을 하다보면 Custom Header를 붙여서 보내는 일이 생기는데, 이때 특정 헤더들을 실어보낼때 preflight request에 실어서 해당 요청을 Accept 할 지 여부를 나타내는 헤더의 목록이다.

```
Access-Control-Allow-Headers: X-Custom-Header, Upgrade-Insecure-Requests
```

일부 헤더들은 default로 그냥 받아준다. 예를 들면 Accept, Accept-Language, Content-Language, Content-Type 같은 것들이 있다.

만약 상호간의 협의로 커스텀 헤더를 사용한다면 서버 쪽에서 Custom Header를 Accept 해야줘야하고, preflight가 CORS에러를 내며 튕긴다면 서버의 설정을 한번쯤 확인해보는 것이 좋다.
