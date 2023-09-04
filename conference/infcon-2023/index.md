# INFCON 2023

<details><summary>타입스크립트는 왜 그럴까? -> 집합으로 보자</summary>

- 타입 호환성: 특정 타입의 값을 다른 타입으로 취급해도 괜찮은지 판단하는 기준. super-sub 관계로 판단
  - up casting (작은 집합을 큰 집합으로 판단)은 가능. down casting은 불가능(대부분)
- 특수한 녀석들
  - unknown: 전체 집합
    - 모든 타입의 값을 저장할 수 있음 (`let a: unknown = 1`)
    - e.g., 현재 정확한 타입을 알기 어려울 때 + type guard & narrowing으로 값 보장 가능
  - never: 공집합 (`let neverVar:never; let a: number: neverVar;`)
    - e.g., 정상적으로 도달하지 않는 함수 (`function error(v: never) { throw new Error() }`)
    - e.g., switch의 완전성 보장 (default case 핸들링)
  - any: 타입 검사를 받지 않음
    - never 타입의 변수에는 저장 불가
    - e.g., 불가능한 타입 단언 가능하게함 (`let str2: string = 10 as any | unknown as string`)
- structural typing(duck typing)간 호환성: property의 여부 + 타입의 super-sub 관계로 판단
- 대수 타입 (algebraic data types): 둘 이상의 타입을 합쳐 만든 타입
  - union: 합집합 (`|`)
  - intersection: 교집합 (`&`)
</details>
<details><summary>당신의 웹페이지는 몇점인가요? 라이트 하우스를 통한 화면 성능 개선</summary>

- 웹 성능 개선이란?
  - 사이트내의 리소스 로드 시간 단축
  - interactive 가능한 타이밍을 앞으로 당겨야함
  - 체감 성능: 실제로는 느리게 반응하지만 사용자가 느끼는 체감으로 줄어든듯한 느낌줌(skeleton)
- 로딩 성능: 리소스 로딩까지 걸리는 시간 (network)
  - e.g., redirect, app cache, dns, tcp -> 캐싱
  - e.g., request, response -> 리소스 압축
- 렌더링 성능: 받아온 리소스와 DOM이 그려지는 성능 (performance)
  - CRP(Critical Rendering Path)
  - devtools가 찍어주는 몇몇 방점들
    - FP(First Paint): 최초의 픽셀이 그려진 시점
    - FCP(First Contentful Paint): 최초의 컨텐츠가 그려진 시점
    - LCP(Largest Contentful Paint): 보여지는 화면에서 가장 큰 컨테츠가 그려진 시점
    - DCL(Document Content Loaded): DOM이 완성되는 시점
    - L(Load)
  - 예시: 렌더링 성능 개선 - 파싱 과정 최적화 (js에 영향을 많이 받음)
    - 아래 코드의 문제점: 브라우저가 HTML 파싱을 두번하게됨.
      ```javascript
      document.addEventListener('DOMContentLoaded', () => {
        const change_dom = document.querySelector('.chanage_dom');
        change_dom.innerHTML = `<img src="..." alt=".." />`
      })
      ```
    - 파싱을 한번으로 만듬 ('DOMContentLoaded`를 없앰)
      ```html
      <!-- improved -->
      <body>
        <script src="./test.js" />
      </body>

      <script>
        const change_dom = document.querySelector('.chanage_dom');
        const img = document.createElement('img')
        img.src = '...';
        change_dom.appendChild(img)
      </script>
      ```
  - 예시: 렌더트리 성능 구성 이후 개선 Layout -> Paint -> Composite
    - Layout, Paint, Composite 단계가 하나씩 빠지게 된다면?
    - css 속성마다 이 과정이 빠지는 속성들이 있다. 찾아보렴
- long task: 50ms가 초과되는 작업. 메인스레드를 독점하는 작업(대개 js)
- 사용자 경험 개선 (Core Web Vitals) -> lighthouse
  - LCP(Largest Contentful Paint): 사용자는 시각적으로 가장 큰 영역이 빠르게 그려질수록 빠르게 렌더링된다고 느낌
  - SI(Speed Index): 페이지가 그려지는 중 시각적으로 표시되는 속도를 나타내는 지표 (컨텐츠가 채워지는 속도)
  - TTI(Time to Interactive): 사용자의 상호작용이 안정적으로 응답할 수 있는 시점의 시간 -> 메인스레드 안잡아먹고 있으면 상호작용 바로 할 수 있는거 아니냐
  - TBT(Total Bloking Time): longtask의 50ms 제외한 나머지 시간. 높으면 높을 수록 blocking time이 높지 않냐
    - FCP와 TTI 사이의 longtask들의 기준 시간을 뺀 모든 값을 더한 시간 (모든 task가 걸린시간 - longtask기준시간 * task num)
  - CLS(Cummulative Layout Shift): 화면기준 특정 영역이 이동한 거리로 계산한다. (사용자 이벤트 기준으로 500ms가 지나면 예상치 못한 레이아웃 이동)
  - FID(First Input Delay)
</details>
