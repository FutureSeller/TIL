# OAuth: Open Auth(Authentication + Authorization)

> OAuth를 사용자 인증을 위한 방법으로 쓸 수 있지만, 더 큰 목적은 'Authorization with scope'
>
> > Access token을 기반이므로 세션이나 쿠키를 이용해 상태를 유지할 필요가 없음 (HTTP 헤더에 포함)

## Basic Knowledge

#### Roles

- Resource Owner: 유저
- Resource Server(Service Provider)
  - 유저에게 종속된 정보(보호된 자원)를 접근 할 수 있도록 해주는 서버
  - access token을 사용해서 권한 검증
  - e.g., 이름, 나이 등 아이디 관련 정보를 제공하는 서버
- Client(Consumer)
  - Resource Server에 접근 하여 사용자의 보호된 자원에 접근하는 앱
  - e.g., 구글, 페이스북 아이디로 로그인이 가능한 제 3의 서비스
- Authorization Server
  - 유저의 요청을 허용/거부하는 서버; Access token을 발급해주는 서버
  - 로그인을 통해 인증 후 권한을 부여하는 서버

#### Token

- Access Token
  - 보호된 자원에 접근할 때 권한 확인 용으로 사용됨
  - 문자열 형태; 여러 인증 방식에 각각 대응하지 않아도 확인 가능
- Refresh Token
  - Access token이 만료되었을 때, 새로운 token을 발급 받기 위한 토큰
  - Authorization 서버가 access token을 발급해 줄 때 함게 발급해줘서 별도의 발급절차 없이 미리 가직고 있을 수 있음
  - Resource Server에는 전송되지 않음

## Creating an App: OAuth를 사용하기 위해 Client가 해야할 것들

#### App 등록: Redirect URIs

- App 이름과 웹 사이트, 로고 등등을 등록하게 되어있음
- **Redirect URI**를 반드시 등록해야함
- MITM을 막기 위해, HTTPS 위에서 등록된 URI로 리다이렉트를 시켜줌

#### Client ID and Secret

> OAuth 서비스에서 애플리케이션을 식별하기 위한 정보

- Client ID
  - public한 정보; 로그인 URL을 만드는데 보통 쓰임
  - 단순하게 생각하면 애플리케이션의 OAuth ID
- Secret(Optional): 공유되어선 안되고 앱을 확인하는데 같이 쓰임

## 인증 방법들 (grant types)

### Authorization Code: web and mobile apps

#### Overall

1. 애플리케이션이 브라우저를 열고 OAuth 서버로 요청을 보냄
2. 유저는 앱의 요청에 대해 허가를 할지 말지 결정함
3. Authorization code가 포함된 URL로 애플리케이션으로 다시 돌아옴
4. 애플리케이션이 Authoization code를 가지고 access token을 얻음

#### 1 ~ 3. 요청 및 허가

- 요청 with Params
  - `response_type`: auth code를 얻기위한 flow 임을 명시
  - `redirect_uri`: 허가 받은 뒤 리다이렉트 될 목적지
  - `scope`: 얻어진 토큰으로 허가할 권한에 대해 명시
  - `state`: random string, 서버에서 validation. CSRF를 막기 위해 쓰임

```
GET /auth
 ?response_type=code
 &client_id=29352915982374239857
 &redirect_uri=https://example-app.com/redirect
 &scope=create+delete
 &state=xcoiv98y2kd22vusuye3kch

Host: authorization-server.com
```

- 응답: response
  - `code`: auth code가 담겨져서 옴. access token을 얻기 위함
    - 일회용이며, 짧은 만료 시간을 가짐 (보통 10분으로 제한)
  - `state`: 위의 값이 존재할 때, 동일한 값이 보임

```
## Success
HTTP/1.1 302 Found
Location: https://example-app.com/redirect
 ?code=g0ZGZmNjVmOWIjNTk2NTk4ZTYyZGI3
 &state=xcoiv98y2kd22vusuye3kch

## Failure
HTTP/1.1 302 Found
Location: https://example-app.com/redirect
 ?error={error_code}
 &error_description=...
 &error_uri=...
 &state=...
```

#### 4. Access Token 요청

- Spec: POST로 요청해야하며 `application/x-www-form-urlencoded` 포맷으로 전달해야함
- 요청 및 응답 예시

```
## 요청
POST /token
Host: example-app.com

grant_type=authorization_code
code={code}
redirect_uri={redirect_uri}
client_id={client_id}
client_secret={client_secret}


## 응답: Success
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: no-store
Pragma: no-cache

{
  "access_token":"MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
  "token_type":"bearer",
  "expires_in":3600,
  "refresh_token":"IwOGYzYTlmM2YxOTQ5MGE3YmNmMDFkNTVk",
  "scope":"create delete"
}

## 실패: Failure
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
    "error":"invalid_client"
}
```

### Password

간단한 OAuth granted type 중 하나이며, 오직 한 step으로만 이루어짐. 유저이름과 패스워드를 가지고 요청하면 access token을 구할 수 있음.

#### Flow

1\. 유저가 클라리언트에 유저이름과 패스워드를 가지고 요청 2\. 클라이언트는 Authorization 서버에 전달 3\. Authorizatioin 서버가 Access token을 내려줌 4\. 해당 Access token을 가지고 요창

#### 요청 및 응답 예시

```
## 요청
POST /oauth/token HTTP/1.1
Host: authorization-server.com
Content-type: application/x-www-form-urlencoded

grant_type=password
&username=exampleuser
&password=1234luggage
&client_id=xxxxxxxxxx

## 응답
{
  "access_token": "MTQ0NjOkZmQ5OTM5NDE9ZTZjNGZmZjI3",
  "token_type": "bearer",
  "expires_in": 3600,
  "scope": "create"
}
```

### Client credentials

별다른 인증 절차 없이 Access Token 을 줌. 데이터에 접근하기 위한 권한이 엄청 빡빡하지 않을 때 사용됨. 1-step 이며, 요청하면 바로 access_token을 줌.

### Implicit

Auth code 교환 과정을 빼고 바로 Access token을 발급 받음. Access otken이 URL에 직접 반환됨. (위의 Authorization은 POST body에)

#### 왜 쓰는거지?

- 일반적으로 JS 용으로 작성된 것
- CORS bypass: OAuth 서버에서 CORS-allow를 안해줄때 쓸 수 있음

#### Flow

1\. 애플리케이션이 브라우저를 열어 사용자가 인증을 하도록함 2\. 사용자의 승인 과정 3\. 사용자는 Access token을 받고 애플리케이션으로 돌아옴

## 취약점: CSRF and URL Redirection

---

## Reference

- https://oauth.net/getting-started
- https://developer.okta.com/blog/2018/04/10/oauth-authorization-code-grant-type
- https://developer.okta.com/blog/2018/06/29/what-is-the-oauth2-password-grant
- https://developer.okta.com/blog/2018/06/06/node-api-oauth-client-credentials
- https://yonghyunlee.gitlab.io/temp_post/oauth-Implicit/
- http://www.bubblecode.net/en/2016/01/22/understanding-oauth2
- https://d2.naver.com/helloworld/24942
- https://meetup.toast.com/posts/105
