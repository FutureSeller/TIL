> 적절히 article 들을 요약해보고 느낀점

> 웹폰트: 사용자가 폰트를 설치하지 않아도 디자이너가 원하는 타이포그래피를 웹 페이지에 구현할 수 있게 하는 기술

```css
@font-face {
  font-family: NanumSquare; // 폰트 이름
  src: url(path-to-font.woff2) format('woff2'); // 경로와 포맷
}

html {
  font-family: NanumSquare, san-serif; // fallback 폰트
}
```

#### 생길 수 있는 문제: 웹 폰트의 로딩이 늦어져 로딩이 끝나기 전에 폰트가 렌더링 되지 않음
- 왜? 브라우저의 렌더링 과정을 보면
  - CSSOM 생성 과정에서 웹 폰트 링크로 정의된 부분을 보고 폰트 파일을 다운로드
  - paint 단계에서 외부 링크로 연결된 파일의 다운로드가 완료되지 않았다면 브라우저는 해당 자원을 사용하는 컨텐츠의 렌더링을 차단함
- 원인
  - 네트워크 속도: 이것은 제어할 수 없음
  - 웹 폰트의 용량
  - 웹 폰트가 적용된 텍스트가 보이지 않는 문제

#### 최적화 방법 1: 폰트 파일의 용량 줄이기
- woff 2.0 포맷 사용
  - 압축된 포맷
  - 다만 레거시 브라우저가 지원하지 않으면 fallback을 등록해줘야함
  - woff2 > woff > ttf
- 서브셋 폰트
  - 불필요한 글자를 제거하고 사용할 글자만 남겨둔 폰트 (휴리스틱, 경험적으로 쓰이지 않는 글자들을 제거하여 파일 크기 줄임)
- unicode-range: 유니코드로 지정한 글자에만 웹폰트 적용 (`unicode-range: U+BC14, U+CC28`)
  - 등록된 글자가 없으면 웹 폰트 다운로드를 요청하지 않아 불필요한 다운로드 막음
  - Google은 머신 러닝 기반 최적화 기술을 통해 주제에 따라 사용되는 글자의 패턴에 따라 그룹을 나누고 unicode-range를 사용함.

#### 최적화 방법 2: 텍스트가 항상 보이게 하기

- 웹 폰트 적용 될 때 텍스트의 번쩍임 (flash of text)이 발생함.
- 브라우저의 렌더링 차단 방식에 따라 조금 다르게 나타남
  - FOUT(Flash Of Unstyled Text): IE 계열; 폴백 폰트 상태에서 폰트가 바뀌면서 번쩍임
  - FOIT(Flash OF Invisible Text): 나머지; 텍스트가 보이지 않는 상태에서 폰트가 바뀌며 번쩍임

FOUT일 경우, 텍스트가 보이지만 레이아웃이 틀어지는 문제가 있고 FOIT은 아예 컨텐츠가 안보이는 문제가 있음.
이 최적화의 초점은 FOIT을 FOUT 방식으로 작동하게 하면 항상 보이게 할 수 있다는 것.

- Font Face Observer 라이브러리: 폰트 로딩 상태를 추적할 수 있는 로더.
- css의 font-display: swap을 사용함
  - block: FOIT
  - swap: FOUT
  - fallback: 100ms 동안 텍스트가 보이지 않고 폴백 폰트로 렌더링; 약 2초간 swap 시간이 있음. 이때 동안 웹 폰트가 다운로드 완료되면 변경
  - optional: fallback과 비슷한데 브라우저가 네트워크 상태를 파악해서 웹 폰트 전환 여부를 결정; 네트워크 상태가 안 좋으면 다운로드 되어도 캐시에만 저장하고 전환은 안함

#### 최적화 방법 3: Font Style Matcher
- https://sangziii.github.io/fontStyleMatcher/ 를 보고 최대한 비슷하게 맞추는 것.

#### 최적화 방법 4: preload 옵션으로 먼저 로딩
- `<link>`의 rel 속성에 preload 사용; 주로 폰트, 이미지, 스크립트, 비디오 등 페이지에서 중요도가 높은 자원을 의도적으로 먼저 로딩
- `<link rel="preload" href="...." as="font" type="font/woff2" crossOrigin="" />` 
- 겸사겸사 `<link rel="preconnect" href="...' />`를 통해 미리 DNS preconnect를 하면 브라우저가 필요한 소켓을 미리 설정해 둬서 DNS, TCP, TLS 왕복 시간을 줄임.
- 단점: preload를 많이하면 리소스가 많아질수록 처음 렌더링 시간이 늦어짐.


---

## 어떻게 Measure 하는가?

- Chrome Lighthouse 를 열고 퍼포먼스 리포트를 본다.
  - critical request chain 을 보고 웹폰트가 얼마나 비중을 차지하는지 확인
  - FP(First Paint), FCP(First Contentful Paint), FWF(First Web Font), Visually Complete(VC), Lighthouse Score 등을 참고
- https://www.webpagetest.org/ 이런데서 링크를 넘겨본다. 

## 추가: 꽤나 괜찮은 방법론
- Async CSS: 구글 폰트 파일을 async하게 로딩: https://csswizardry.com/2020/05/the-fastest-google-fonts/ 여길 읽어볼 것

---
## Reference
- https://d2.naver.com/helloworld/4969726
- https://web.dev/codelab-preload-web-fonts/
- https://csswizardry.com/2020/05/the-fastest-google-fonts/
