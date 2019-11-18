*Reference의 article을 나름대로 정리 + 개인적인 생각을 첨가*

# Building the DOM faster: speculative parsing, async, defer and preload

### The history of the <script> tag & CSS
- HTML → `<script>` → DOM
  - `script`가 중간에 들어가 있을 경우 HTML 파싱이 `script`의 실행이 끝날때까지 block됨
  - `script`가 DOM을 접근/조작할 수 있기 때문. e.g., `document.write()`
- CSS는 document를 수정하지 않는데 왜?: `script`는 CSSOM 또한 접근/조작할 수 있기 때문
- 이로 인해 발생한 문제가 FOUC(Flash of unstyled content)
- PoC: https://codepen.io/micikato/pen/JroPNm

### Speculative Parsing

#### 읽기 전 내 생각
Computer Architecture 수업 이후로 Speculative 라는 단어를 참 오랜만에 본다.

너무 자세한 내용은 여기서 다루지 않겠지만(Pipeline, Out of order execution, Superscala 등 너무 많은 background가 필요하다) 짧게 말하자면 성능 향상을 위해 뒤의 내용을 미리 실행해보고 아니면 되돌리자라는 컨셉이다. (prediction, prefetch, unroll 등이 있다)

물론 이에 관련된 매우 크리티컬한 취약점인 Spectre, Meltdown이 나오긴했다.

article을 읽기 전에 제목만 봐서는 DOM 파싱을 하면서 resource를 미리 가져오는 듯 하다.

#### Article의 내용

``` html
<script src="slider.js"></script>
<script src="animate.js"></script>
<script src="cookie.js"></script>
<img src="slide1.png">
<img src="slide2.png">
```

- Problem: HTML 파서는 `img`를 fetch 하기전까지 모든 `script`를 로드 및 실행해야함
- Idea: `script`실행 중에 (DOM을 만드는 건 좀 위험하지만) 파싱을 진행하면서 추후 어떤 리소스가 필요한진 알 수 있다.
  - ie: lookahead downloader
  - chrome, safari: the preload scanner
  - firefox: speculative parser

![Preloading resources with speculative parsing](https://hacks.mozilla.org/files/2017/09/waterfall-2-bold@2x-768x319.png)

- 꽤나 위험한 Assumption: `script`에서 DOM을 조작하지 않을 가능성이 높다.
  - `speculative`라고 쓴 이유는 역시 `script`의 개입이 위험할 수 있기 때문. e.g., `document.write()`
  - 따라서 어떤 리소스가 필요한지 보고 `preload`하는데 그침 (DOM tree construction은 안함)
  - article만 보면 firefox는 내부적인 unroll 알고리즘이 있는듯 하다.

### (Pre)loading stuff
- 모든 major 브라우저들이 preload를 지원하는 것
  - scripts
  - external CSS
  - images from the `<img>` tag
- 브라우저가 parallel하게 다운 받으려면 다수의 connection이 필요함
- 특정 리소스들을 markup을 통해 `prioritize` 할 수 있음

### defer and async
- `script` 다운로드가 DOM construction을 block하지 않음: background에서 `script`를 fetch하면서 HTML 파싱을 그대로 유지함
- `defer`: HTML 파싱이 끝나면 스크립트 파일 실행
  - HTML 파싱하는 동안 blcok하지 않고 `script`를 다운받음
  - HTML 파싱이 끝난 후, `DOMContentLoaded` event 실행전 script를 실행
  - 호출된 순서대로 실행됨
- `async`: 스크립트 파일이 비동기적으로 실행 될 수 있음
  - HTML 파싱하는 동안 block하지 않고 `script`를 다운 받음
  - `script`가 다운로드완료되면 HTML 파싱을 block하고 `script`를 실행
  - 다운로드완료 시점에 실행되기 때문에, 실행 순서를 제어할 필요가 있음
- `defer`와 `async`는 모두 **external script**에 적용.

### preload
- viewport에 최대한 빨리 렌더링 되어야할 리소스들에 사용할 수 있음
- 해당 리소스는 동일한 우선순위로 로드되지만, 다운로드가 더 일찍 시작되도록 허용
- e.g., `<link rel="preload" href="..." as="...">`
- as
  - `preload`를 사용가능한 content들; script, style, image, font, audio, video 등
  - as에 올바른 값이 설정되지 않으면 preload 된 리소스를 사용하지 않음

### prefetch
- 기회가 있으면 중요하지 않은 것을 먼저 발생시키려고 함
- 사용자가 다음에 할 행동을 선점하여 준비하는데 적합 (e.g., 예상된 행동 혹은 나중에 필요)
- 페이지가 로딩을 마쳤고, 사용 가능한 대역폭이 있을 때 가장 낮은 우선순위로 가져옴
- "helps to fetch the resource and places it in the cache. instead of making another request"

### preconnect
- 브라우저에게 host에 연결하고 컨텐츠를 가져오려 한다는 것을 알림
- 연결 단계에서 시간 절약, but 반드시 컨텐츠를 바로 가져올 필요 없는 경우
- e.g., `<link rel="preconnect" href="https://example.com">`
- DNS lookup & TCP handshaking을 처리
- dns-prefetch: dns lookup만을 처리

---
## Reference
- https://hacks.mozilla.org/2017/09/building-the-dom-faster-speculative-parsing-async-defer-and-preload
- https://developers.google.com/web/fundamentals/performance/resource-prioritization?hl=ko
- https://codeburst.io/how-to-improve-web-performance-by-using-preload-preconnect-prefetch-6c64e0ecd164