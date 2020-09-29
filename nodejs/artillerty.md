# Artillery란?

> Node.js 기반의 부하 테스트 및 기능 테스트를 위한 도구

- 목적: 애플리케이션의 실제 부하를 시나리오 기반으로 시뮬레이션하는 것
- 동작 방식: 가상 유저가 사전에 정의한 시나리오를 기반으로 애플리케이션의 액션을 발생시킴
- 지원하는 프로토콜: HTTP(S), WebSocket
- 시나리오: YAML로 작성되고 필요한 경우, JS로 확장하여 세부 동작을 커스텀 할 수 있음
  - beforeScenario / afterScenario: 가상 유저가 시나리오 실행 전/후로 실행하는 JS
  - beforeRequest: 요청 시 파라미터들(header, URL, cookie, body 등)을 커스텀하는 데 주로 쓰임
  - afterRequest: 응답을 검증하거나 커스텀 하는데 사용
  - function: 시나리오의 특정 포인트에 실행될 JS 함수들을 삽입하는 용도 (e.g., 로깅)
- 외부 모니터링: Datadog이나 InfluxDB 등에 실시간으로 결과를 등록할 수 있음
- 리포트 페이지를 제공함

## 테스트 스크립트를 읽는 법

부하테스트는 스크립트는 크게 config와 scenario로 나눠서 볼 수 있다.

### config: 테스트 타겟, 테스트 조건, 프로토콜 관련 옵션을 설정 하는 곳

- target: 부하 테스트 대상 (e.g., API 서버의 주소; http://lucas.is.good.software.engineer)
- phases
  - 쉽게 생각하면 주어진 시간동안 시나리오를 실행할 하나 혹은 여러개의 단계
  - 시나리오는 정의된 모든 phase 들을 순차적으로 실행하게 되어 있음
    - 시나리오가 하나 정해져있음 (e.g., “/”에 100번 요청을 해라)
    - warmup phase, sustained max load phase가 있다고 가정
    - 위의 시나리오를 warmup phase에서 실행 한 뒤, sustained max load phase 에서 실행함
  - 얼마나 많은 가상 유저를 특정 time period에 생성할 것인지 정의
  - 하나의 phase는 duration과 arrival rate 값을 통해 생성되어야 할 가상 유저를 정의함
    - duration: phase가 실행 종료 되기 까지의 시간 (초 단위)
    - arrivalRate: 초당 가상 유저의 수
    - rampTo: 보통 서버 warmup을 재현하기 위해 쓰임. arrivalRate부터 rampTo 값까지 가상 유저수를 늘려줌
    - maxVusers: 초당 최대 가상 유저 수를 제한하기 위해 쓰임
    - name: 어떤 phase 인지 알아보기 쉽게 하기 위한 식별자; 리포트에 label을 달아줌
    - pause: 특정 시간동안 아무것도 하지 않도록 함 = NO-OP (초 단위)

```yaml
# warm up case
config:
  target: "https://staging.example.com"
  phases:
    # 120초 동안 10명의 가상 유저를 50명의 가상 유저까지 linear 하게 증가 시키며 테스트
    - duration: 120
      arrivalRate: 10
      rampTo: 50
      name: "Warm up the application"
    # 600초 동안 50명의 가상 유저로 부하 테스트
    - duration: 600
      arrivalRate: 50
      name: "Sustained max load"
```

- environments: target과 관련된 환경 설정
  - 같은 테스트 스크립트를 다른 환경에서도 사용하기 위함
  - 실행 환경을 쉽게 알 수 있도록 명명하는 것이 좋음 (e.g., production, local, dev, staging etc.)
  - CLI 에서  -e 플래그를 사용하여 실행환경을 넘겨줄 수 있음 (e.g., artillery run -e staging my-script.yml)

```yaml
config:
  environments:
    # production 환경과 테스트 phase의 정의
    production:
      target: "http://wontresolve.prod:44321"
      phases:
        - duration: 120
          arrivalRate: 10
    # staging 환경과 phase 정의
    staging:
      target: "http://127.0.0.1:3003"
      phases:
        - duration: 1200
          arrivalRate: 20
```

- payload: 임의의 데이터를 실어서 보내기 위해 사용. CSV file에 미리 정의하고 경로를 지정해줘야 함
- variables: payload의 CSV file을 사용하지 않고 직접 데이터를 YAML에 정의함

```yaml
config:
  payload:
  # path is relative to the location of the test script
  path: "users.csv"
    fields:
      - "password"
  variables:
    username:
      - "odc-front-graphql"
scenarios:
  - flow:
    - post:
      url: "/auth"
      json:
        username: "{{ username }}"
        password: "{{ password }}"
```

- defaults: HTTP 요청에 추가할 헤더들을 정의함
- tls: self-signed certificate 을 설정하기 위한 필드
- ensure: 테스트가 성공했는지 검증할 조건들을 명시(e.g, latency, error rates); CI/CD 연동을 위해 유용함

```yaml
# case 1: error rate가 1% 미만인 경우 return 0
config:
  ensure:
    maxErrorRate: 1

# case 2: p95 latency가 200ms 보다 낮을 경우
config:
  ensure:
    # min, max, median, p95, p99 값을 설정할 수 있음
    p95: 200

timeout: 요청의 타임아웃을 명시. Artillery는 default로 응답이 오는데 120초가 넘어가면 ETIMEOUT 에러를 내뱉음

config:
  target: "..."
  http:
    # 10초가 지나면 timeout!
    timeout: 10
```

- fixed connection pool: config.http.pool
  - 기본적으로 Artillery는 모든 새로운 가상유저에게 새로운 커넥션을 하나씩 맺어줌. 그리고 모든 커넥션들은 `keep-alive` 임.
  - 해당 값을 설정하면 정해진 커넥션 숫자만큼 pool을 유지하고 이를 재사용하게 해줌
  - 보통 로드 밸런서가 있는 상황을 에뮬레이션 하기 위해 쓰임
- Max sockets per virtual user: config.http.maxSockets
  - 기본적으로 각 가상유저마다 TCP 커넥션을 하나씩 맺어줌
  - 가상 유저마다 소켓을 여러개 뚫어주고 싶을 때 이 옵션을 활용
  - 주의할 점은 전체 소켓 수가 아니라 유저마다 가질 수 있는 소켓수라는 걸 꼭 염두해두어야함 (VU가 엄청 많다면 ulimit을 풀어줘야함)

### scenario: 가상 유저가 어떤 시나리오로 실행 될 지 정의하는 곳

- flow: 가상 유저가 실행해야할 일련의 동작들을 정의. 위에서 아래로 순차적으로 실행됨
  - GET / POST / PUT / PATCH / DELETE requests: 
    - url, json, body, headers, cookie
    - capture: https://artillery.io/docs/http-reference/#extracting-and-reusing-parts-of-a-response-request-chaining
- Logging
- Setting Headers
- think: 가상 유저에게 주어진 N 초만큼 멈추라고 정의하는 것
- conditional requests: ifTrue attribute가 참일때 실행됨
- loop: loop 으로 시작됨
- count: 주어진 횟수만큼 돌게 함. 주어지지 않는 다면 무한 루프가 생성됨
- over: loop에 주어지는 배열이며, loop body를 한번 실행할 때, 정의된 값을 모두 사용하여 요청함. 예를 들어 over에 [a,b,c]가 있다면, 한번 loop body를 실행할 때 3개의 요청이 실행됨

나머지는 https://artillery.io/docs/http-reference/#flow-actions 를 참고하면 됨

```yaml
config:
  target: "https://example.com"
  phases:
    - duration: 10
      arrivalRate: 1
scenarios:
  - name: "HTTP Related Flow"
    weight: 3
    flow:
      # log action을 통해 디버깅 메세지를 남김, 변수를 포함할 수 있음
      - log: "New virtual user running: {{ $environment }}"
      - get:
          url: "/"
          capture:
            json: "$.id"
            as: "id"
            
      # /resource에 POST 요청
      - post:
          url: "/resource"
          json:
            hello: "world"
            
      # 2초간 잠시 멈춤
      - think : 2
      
      # /test에 헤더를 붙여 GET 요청
      - get:
          url: "/test"
            headers:
              X-My-Header: "123"
              
      # /pages 의 pageNumber가 10 이하일때만 요청이 가도록 함       
      - get:
          url: "/pages/{{ pageNumber }}"
          ifTrue: "pageNumber < 10"
          
  # / 에 100번 요청하는 flow
  - name: "Loop through number"
    weight: 1
    flow:
      - loop:
        - get:
            url: "/health-check"
        count: 100
  
  # loop을 실행하는 동안 over의 갯수에 해당하는 만큼 요청을 생성함
  - name: "Looping through an array"
    weight: 2
    flow:
      - loop:
        - get:
           url: "/products/{{ $loopElement }}"
       over:
         - id123
         - id456
         - id789
```          

- name: 어떤 시나리오 인지 설명하기 위한 필드
- weight: 여러 시나리오(flow)가 있을 때, 가상 유저가 어떤 시나리오를 실행할 지 도움을 주는 값
  - 높은 값일 수록, 해당 시나리오가 실행될 확률이 높음
  - 설정하지 않으면 기본 값은 모두 1으로 모두가 동일함
  - weight가 같으면 모든 시나리오가 동일한 횟수로 실행되지 않고 같은 확률로 선택될 수 있다는 것을 의미함

```bash
# 각각 weight를 1로 주었을 때
Scenario counts:
    GraphQL Query load test: 30 (60%)
    multiple flow?: 20 (40%)

# GQL: 2, Multiple flow: 1
Scenario counts:
    GraphQL Query load test: 35 (70%)
    multiple flow?: 15 (30%)
```

### Advanced: JS로 로직을 커스텀하는 방법

- HTTP engine이 “hooks”를 지원하기 때문에 시나리오의 특정 시점에 JS 함수를 끼워넣을 수 있음
  - beforeScenario / afterScenario: 가상 유저가 시나리오 실행 전 / 후로 실행하는 JS
  - beforeRequest: 요청 시 파라미터들(header, URL, cookie, body 등)을 커스텀하는 데 주로 쓰임
  - afterRequest: 응답을 검증하거나 커스텀 하는데 사용
  - function: 시나리오의 특정 포인트에 실행될 JS 함수들을 삽입하는 용도 (e.g., 로깅)
- 경로 설정: config.processor 에 JS 파일의 경로를 명시해주면 됨

```yaml
config:
  target: ...
  phases: ...
  processor: "./my-functions.js"
scenarios:
  - ...
```

- JS 파일: 시나리오에서 사용할 함수를 export 해줘야 함. 시나리오에서 함수명을 동일하게 가져다 씀
  - Function Signatures: 각각 어떤 파라미터가 사용되어야하고 어떤 의미를 갖는 지는 아래를 참고
  - https://artillery.io/docs/http-reference/#function-signatures

```javascript
# beforeRequest
function setJSONBody(requestParams, context, ee, next) {
  // DO SOMETHING
  return next();
}

function logHeaders(requestParams, response, context, ee, next) {
  console.log(response.headers);
  retrn next();
}

module.exports = {
  setJSONBody,
  logHeaders,
}
```

이를 활용한 예시들은 각각 아래와 같음

- Request / Response Level Hooks: beforeRequest, afterReponse

```yaml
  # ... a request in a scenario definition:
  - post:
      url: "/some/route"
      beforeRequest: "setJSONBody"
      afterResponse: "logHeaders"
```

- Function Steps in a flow

```yaml
scenarios:
  - flow:
    # Call setupSomeData
    - function: "setupSomeData"
    - get:
        url: "/some/url?q={{ query }}"

# 특정 변수를 conext에 저장하는 함수
# function setupSomeData(context, events, done) {
#   context.vars['query'] = 'foo'
#   return done();
# }
```

## 지표를 보고 해석하는 법
- 터미널에 출력되는 값들을 읽고 해석하는 법
- Artillery는 실행하면 10초마다 아래와 같은 값들을 터미널에 보여주고, 합산된 값을 주어진 경로에 쌓은 뒤 리포팅해준다.

```
Report @ 12:08:57(+0900) 2020-06-23
Elapsed time: 10 seconds
  Scenarios launched:  9
  Scenarios completed: 6
  Requests completed:  56
  Mean response/sec: 6.58
  Response time (msec):
    min: 1.8
    max: 712.9
    median: 441.2
    p95: 587.3
    p99: 710.7
  Codes:
    200: 54
    400: 2

# 합산된 값을 리포팅
Summary report @ 12:09:41(+0900) 2020-06-23
  Scenarios launched:  50
  Scenarios completed: 50
  Requests completed:  370
  Mean response/sec: 6.92
  Response time (msec):
    min: 1.7
    max: 712.9
    median: 446.7
    p95: 524.7
    p99: 534.4
  Scenario counts:
    GraphQL Query load test: 40 (80%)
    multiple flow?: 10 (20%)
  Codes:
    200: 360
    400: 10
```

- Scenarios launched: 10초동안 혹은 전체 테스트 동안 생성된 가상 유저의 수 
- Scenarios completed
  - 10초동안 혹은 전체 테스트 동안 시나리오가 완료된 가상 유저의 수
  - 10초 간격으로 시작 / 완료된 세션수가 아니라, 10초 동안 완료된 세션 수를 의미
  - 요청이 쌓일 수 있다는 의미이고 특정 10초 주기안에 완료된 숫자를 카운팅
- Requests completed: HTTP 요청 / 응답의 숫자. 혹은 전송된 WebSocket 메세지의 수
- Mean response / sec  (공식 문서에는 RPS send); 10초 혹은 전체 테스트 동안, 완료된 요청 / 소요된 시간 (second)
- Response time (공식 문서에는 Request latency)
  - 응답을 받기까지의 소요 시간
  - milliseconds 단위임을 명심
  - p95: 95th percentile, p99: 99th percentile; 
  - p95: 524.7; 풀어 얘기하자면, p95의 값은 100개의 요청 중 95개가 완료되는데 524.7ms 이하가 소요되었음을 의미
- Scenario counts: 실행된 시나리오의 수; flow가 여러개인 경우 각각의 실행된 시나리오 빈도와 다른 시나리오 대비 얼마나 실행되었는 지 비율을 알려줌
- Codes: HTTP 응답 코드를 카운팅한 결과를 알려줌

## Graphical Report를 읽고 해석하는 법

- Summary: 테스트를 수행하는 동안 합산된 결과를 보여주는 섹션
- Scenario counts, Codes, Errors 는 위와 동일함

![report1](https://user-images.githubusercontent.com/50730028/94529427-ae613480-0274-11eb-8f6e-fd035eaf8962.png)

#### Charts: Overall Latency Distribution
- 부하테스트 동안 Latency(Response time)의 분포를 한눈에 보여주는 차트
- 보통 p95 값으로 많이 본다고 하며, 임계값을 두고 개선해야하는 지 판단한다고 함; 예를 들면 p95가 200s를 넘으면 병목을 찾고 개선을 해야해!

![report2](https://user-images.githubusercontent.com/50730028/94529434-b02af800-0274-11eb-9d6d-955c3cc97887.png)

#### Charts: Latency At Intervals
- 부하 테스트 시, 특정 시점에 Latency 값을 볼 수 있는 차트
- percentile과 max, min을 볼 수 있으며 각각 가상 유저마다 다른 시연시간을 가질 수 있음
- min, p95, p99, max 등의 편차가 크다면 서버의 성능으로 몇몇 사용자의 경험이 좋지 않을 수 있음을 짐작 할 수 있음.

![report3](https://user-images.githubusercontent.com/50730028/94529436-b15c2500-0274-11eb-8608-c7fe59e9e64d.png)


#### Charts: Concurrent Users

- 특정 시점의 동시 사용자 수 = 특정 시점에 응답을 받기위해 대기하는 동시 사용자의 수
- 부하 테스트 시, 서버가 arrivalRate (가상유저 수)를 얼마나 감당할 수 있는 지를 볼 수 있음
- 시나리오 소요 시간과 가상 유저의 수에 따라 달라지며, 응용 프로그램의 응답 속도에 따라 달라짐
  - 0 ~ 100초: 거의 요청에 대한 응답을 바로바로 주기때문에 응답을 받아야하는 사용자는 거의 0에 수렴
  - 330 ~ 700초: 점차 응답을 주는 속도가 느려져 응답을 기다리는 사용자의 수가 점점 증가함
  
![report4](https://user-images.githubusercontent.com/50730028/94529510-cb960300-0274-11eb-80a6-e1a118dc1de4.png)

#### Charts: Mean RPS & RPS Count

- Mean RPS: 서버의 요청에 대한 초당 응답 수의 평균 (주의: median이 아님!)
- RPS Count: 서버의 요청에 대한 초당 응답 수
- Latency와 별개로 서버의 처리량을 볼 수 있음
  - 100초 까지는 Warm up으로 차근차근 가상유저의 수가 증가하기 때문에 둘 다 증가함
  - 고정된 가상 유저의 수라면 거의 평행선을 유지하는 게 좋지 않을 까 싶고, dramtic하게 줄어들 경우를 주의깊게 봐야하지 않을까 싶음

![report5](https://user-images.githubusercontent.com/50730028/94529515-cd5fc680-0274-11eb-9994-390b25c20f0b.png)

---
## Reference

- https://artillery.io/
- https://artillery.io/docs/script-reference/
- https://artillery.io/docs/http-reference/#Flow%20actions
- https://www.testim.io/blog/artillery-load-testing-introduction-see-how-your-code-scales/
