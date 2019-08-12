## Background
- historycally, tab을 닫기전까지는 무한히 살아있음
- memory, CPU, battery, entwork 등 리소스를 갉아먹게됨. 이에 따라 나아가 Bad UX의 원인이 되기도 함
- Lifecycle States
  - DOMContentLoaded
    - 최초 HTML이 완전히 로드되고, 파싱 후, DOM을 생성했을 때 `document`에서 발생하는 이벤트
    - (external) resource loading이 끝나길 기다리지 않음: (CSS, Image, Subframe 등)
    - `document.addEventListener("DOMContentLoaded", () => { new App('#root') })`
  - load
    - DOMCntentLoaded 이 후, 모든 리소스가 완전히 로드되었을 때 사용. `window`
    - 외부의 자원을 사용하는 경우에도 사용됨 (iframe, image, script)
    - onload는 문서에 하나만 존재: 마지막 선언으로 overwrite
    ``` html
    <script>
    window.onload = function() {
      alert('Page loaded');
      // image is loaded at this time
      alert(`Image size: ${img.offsetWidth}x${img.offsetHeight}`);
    };
    </script>
    <img id="img" src="https://en.js.cx/clipart/train.gif?speed=1&cache=0">
    ```
  - beforeunload
    - 윈도우를 닫을 때, resource를 unload하기 전 발생하는 이벤트
    - document는 남아있고, 취소가능한 상태
    - e.g., 창이 닫히기 직전 사용자의 확인을 구하는 경우
    ``` javascript
    // However, this is deprecated and no longer supported in most browsers.
    window.addEventListener('beforeunload', (event) => {
      // Cancel the event as stated by the standard.
      event.preventDefault();
      // Chrome requires returnValue to be set.
      event.returnValue = '';
    });
    ```
  - unload
    - 페이지에서 벗어날 때, `window`. history/navigate/exit/새로고침
    - `cancelable`하지 않음. beforeunload에서 commit 여부를 확인한다고 생각하는 듯
  - `document.readyState`
    - loading: document 로딩 중
    - interactive: external resource 들이 로딩되고 있는 상태
    - complete: load 이벤트가 발생되기 직전 상태
    ``` javascript
    document.addEventListener('readystatechange', event => {
      if (event.target.readyState === 'interactive') {
        initLoader();
      }
      else if (event.target.readyState === 'complete') {
        initApp();
      }
    });
    ```
  - visibilitychange
    - 컨텐츠가 visible 혹은 hidden 상태로 변화할 때 발생함, `document`
    - States 
      - visible
      - hidden
    ``` javascript
    var videoElement = document.getElementById("videoElement");

    // Autoplay the video if application is visible
    if (document.visibilityState == "visible") {
      videoElement.play();
    }

    // Handle page visibility change events
    function handleVisibilityChange() {
      if (document.visibilityState == "hidden") {
        videoElement.pause();
      } else {
        videoElement.play();
      }
    }
    document.addEventListener('visibilitychange', handleVisibilityChange, false);
    ```
---

## Reference
- https://javascript.info/onload-ondomcontentloaded
- https://www.w3.org/TR/page-visibility/#sec-visibilitychange-event
- https://developers.google.com/web/updates/2018/07/page-lifecycle-api
- https://stackoverflow.com/questions/44044956/how-does-browser-page-lifecycle-sequence-work
