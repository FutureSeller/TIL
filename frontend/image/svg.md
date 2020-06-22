# SVG (Scalable Vector Graphics)

SVG가 무엇이고 어떤 특징이 있는지 짚어보는 정도

> 그래픽을 마크업하기 위한 XML의 특수언어

- XML 텍스트 파일로 정의 되어 있어 검색화, 목록화, 스크립트화가 가능하며 필요하면 압축도 가능함
- 픽셀 단위가 아닌 벡터(점, 직선, 곡선과 같이 좌표 기반)로 작성됨
- 1990년 후반에 도입되어 현재 모든 모던 브라우저를 지원함 (IE 9 이후의 브라우저)
- 움직이지 않는 이미지 + 애니메이션과 사용자 인터페이스를 우해 사용될 수 있음
- 이미지가 요구되는곳에 URL을 지정할 수 있음

벡터 기반으로 이미지의 품질 손실 없이 어떤 크기에서도 렌더링할 수 있고 SVG 자체 코드를 수정해서 쉽게 변경할 수 있음

- 확장 가능성과 해상도의 자유로움: 픽셀 기반이 아닌 좌표 기반으로 작성되기 때문
- 작은 파일 사이즈
- 성능향상과 속도
  - 크기가 작기 때문. 텍스트를 렌더링하는 것에 가까움
  - 인라인 SVG의 경우 이미지를 렌더링하기 위해 별도의 http 요청이 불필요함
  - 복잡한 이미지의 SVG는 오히려 로딩 성능이 현저히 떨어질 수 있음; 따라서 로고 혹은 아이콘등 단순한 이미지에 많이 활용
- DOM과 유사한 스타일 변경
  - CSS나 JS로 수정이 가능; 스타일을 내용물과 분리시킬 수 있음

## SVG 사용방법
- img src: 이미지의 width와 height에 의해 크기가 바뀔 수 있음
- background image: `background-image: url(image.svg)`
- inline svg
  - 부가적인 http 요청은 없음. data uri를 사용하는 이점과 동일
  - HTML 마크업이 좀 더러워질 수 있고, 캐싱이 안되기 때문에 로드될 때마다 읽어야 하는 단점이 있음
- `<object>` 요소로 참조
  - `<object data="image.svg type="image/svg+xml" />`
  - 캐싱은 되지만 CSS로 svg 내부를 조작할 순 없음: svg 내부에 style tag를 두고 조작해야함
  - 하지만 꼼수는 있기 마련; HTML에서 CSS를 가져오고 svg 안에서 css를 로드하도록 하면 됨

## Accessibility
요약하자면 title, desc, role 그리고 aria-label을 직접 사용해 접근성을 개선할 수 있음

- SVG as img src: `<img src="image.svg" alt="..." role="img">`
- inline svg
  - SVG의 첫 번째 자식 요소에 title 태그, 두 번째에 desc 태그를 추가 후, unique한 id 값을 줌
  - SVG 태그에 `aria-labelledby="${titleId} ${descID}"`를 줌
  - SVG 태그에 `role="img"`를 줌
- object or iframe: https://css-tricks.com/accessible-svgs/#3-embed-svg-via-object-or-iframe


---
## Reference
- https://developer.mozilla.org/ko/docs/Web/SVG/Tutorial
- https://developer.mozilla.org/ko/docs/Web/CSS/Getting_Started/SVG_graphics
- https://css-tricks.com/using-svg/
- https://css-tricks.com/accessible-svgs/
