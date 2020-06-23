# Largest Contentful Paint (LCP)

> 페이지가 로딩되는 동안 가장 큰 요소가 뷰포트에 보이기까지의 시간; 페이지 로딩 중에 가장 큰 컨텐츠는 계속 바뀔 수 있음

LCP 기준에서 빠른 페이지는 페이지 로딩 시작부터 2.5초 이내에 가장 큰 컨텐츠가 렌더링 되는 것

## 해당하는 엘리먼트
- img
- svg 내부의 image
- video
- background-image가 있는 엘리먼트
- 텍스트를 포함하는 블록 레벨 엘리먼트

## 왜 이런 메트릭이 생겼지?
- 기존에 FP(First Paint), FCP(First Contentful Paint), FMP(First Meaningful Paint)가 있었음
  - FP: 페이지 로딩 시, 사용자가 첫 번째 pixel을 보기까지의 시간
  - FCP: 브라우저가 텍스트, 이미지, 흰색이 아닌 캔버스 또는 SVG를 포함한 DOM의 컨텐츠를 페이지에 처음 렌더링하기 까지의 시간
  - FMP: 사용자에게 필요한 정보를 빠르게; 주요 컨텐츠(유의미한 컨텐츠)가 화면에 그려지는 시점

좀 더 유저 경험과 관련된 메트릭을 만들어서 유의미한 개선을 이끌어 내기 위함.
FMP는 너무 복잡하고 설명하기 힘들며 가끔 잘못된 경우도 있어 좀 더 단순화된 메트릭이 필요했음.

## 어떻게 엘리먼트의 크기가 결정되는가?
- 현재 뷰포트에서 사용자에게 표시되는 크기이며, 뷰포트 밖에 있거나 hidden 오버플로우가 있는 경우는 크기에 포함되지 않음
- 고유 크기에서 크기가 조정된 이미지는 더 작은 크기의 이미지를 기준으로 결정
- 텍스트의 경우 블록이 더 큰 것을 의미
- CSS를 통해 조정된 margin, padding, border는 고려되지 않음

## 개선해야할 포인트와 최적화하는 가?

#### 1. 응답이 느린 경우

Time to First Byte(TTFB)를 측정 후 병목을 찾아 개선

- 서버의 병목을 찾아 개선
- CDN으로 라우팅
- Cache assets
- Serve HTML pages cache-first
  - 서비스 워커를 사용하여 백그라운드에서 실행되는 서버의 요청을 가로 채어 캐시 제어
  - 페이지의 일부 또는 전부를 캐시하고 컨텐츠가 변경되었을 때만 캐시를 업데이트
- Establish third-party connections early
  - 이 녀석들이 LCP에 영향을 줄 수 있음. 가장 큰 영역을 잡아먹을 수 있음
  - `rel=preconnect`를 통해 커넥션을 최대한 빨리 맺음
  - fallback으로 `rel=dns-prefetch`를 사용하는 것이 좋음

#### 2. 렌더링을 블락하는 JS와 CSS
브라우저가 렌더링 하기전 HTML을 파싱하고 DOM 트리를 만듬. HTML 파서는 외부 스타일시트를 만나거나 synchronous 스크립트 태그를 만나면 일시정지하게 됨.

이로 인해 FCP가 늦춰지며 결국 LCP에 영향을 끼치게 되므로, 중요하지 않는 JS와 CSS는 defer 시킴

- Reduce CSS blocking time
  - minify css
  - defer non-critial css: `<link rel="preload" href="stylesheet.css" as="style" onload="this.rel='stylesheet'">`
  - inline critial css: 중요한 녀석들은 head 태그 하위에 직접 위치시킴
- Reduce JS blocking time
  - minify js
  - defer unused JS: bundle dynamic imports > code splitting
  - minimize unused polyfills

#### 3. 리소스 로딩이 느린 경우
- 이미지 압축
  - 페이지 로딩 시, 불필요한 이미지가 있으면 없앰
  - 말 그대로 이미지 압축
  - 새로운 포맷으로 변경 (JPEG 2000, JPEG XR, or WebP)
  - Responsive 이미지 사용
  - CDN을 적극 활용
- Preload resources: `<link rel="preload">`
- 텍스트 압축: gzip and brotli를 사용
- Deliver different assets based on network connection (adaptive serving)
  - 3g vs. 4g vs. 5g; connection 타입과 기타 디바이스의 정보들을 활용
  - navigator.connection.effectiveType
  - navigator.connection.saveData; data-saver
  - navigator.hardwareConcurrency; CPU core count
  - navigator.deviceMemory; Device Memory
- Cache assets using a service worker

---
## Reference
- https://web.dev/lcp/
- https://web.dev/optimize-lcp/
- https://ui.toast.com/weekly-pick/ko_20200528/
