## Distance Units
- "length": /-?[0-9]+(px|rem|em....)/. 숫자와 단위 중 하나를 붙여 구성
- 숫자와 단위 사이에 공백이 있어선 안됨. 
- 0 뒤에는 단위를 붙이지 않아도 됨.
- 종종 음수의 값을 가지기도 함.

### Absolute Lengths
- 언제 사용하나? 
  - 출력 수단의 크기를 알 수 있을 때.
  - 고정된 크기의 element를 rendering 할 때 등등
- 해상도에 따라 기준 단위가 달라짐
  - 저해상도 : px
  - 고해상도 : in, cm, mm
- 1in == 96px == 72pt == 2.54cm == ...
 
| Units | Description |
| - | - |
| Q | 1/4mm. 1Q = 1/40cm (experimental)
| mm | 1mm = 1/10 cm
| cm | 1cm = 96px/2.54
| in | 1in = 2.54cm = 96px
| pt | One point. 1pt = 1/72nd of 1in
| pc | 1피카. 1pc = 12pt = 1/6in
| px | 하나의 장치 픽셀. 

### Relative Lengths
- 어떤 기준점을 가지고 다른 거리와의 상대적 비율을 표현함
- 단위에 따라 특정 문자, line-height, 뷰포트
- Questions
  - 뷰포트: 현재 화면에 보여지고 있는 다각형(보통 직사각형)의 영역
  - x 높이(x-height)
    - 기준선과 서체에서 소문자의 평균 줄 사이의 거리
    - `vxw`의 bottom을 기준선으로 두고, 소문자의 top 사이까지의 거리
    - `u`같은 경우 곡선때문에 약간 높이를 넘어설수도있고, 낮을 수도 있다고 한다;
    - 보편적으로 사용되지 않는다고 하는데 언제, 어디서, 왜 쓰는거지?
    - 언제: font styling할 때
    - 어디서: web이나 뭐 latex 같은 곳
    - 왜: 흠... design 적인 decision일듯함

| Units | 기준점 | Description |
| - | - | - |
| em | parenet element | parent element의 font-size에 비례. parent의 font-size 의 배수 |
| ex | font's baseline | font의 x높이. 많은 글꼴에서 1ex == 0.5em |
| rem | root element font-size | root + em |
| vw | width of viewport | 뷰포트 width의 1%
| vh | height of viewport | 뷰포트 height의 1%
| vmin | smaller dim of viewport | 뷰포트의 가장 작은 diemnsion (x or y)의 1%
| vmax | larget dim of viewport | 뷰포트의 가장 큰 diemnsion (x or y)의 1%
| % | parent element | 부모 element 기준으로 percent

## Angle Units
| Unit | Description |
| - | - |
| deg | 양수의 경우, 시계방향으로 degree만큼 회전. 음수는 반시계방향
| grad | gradian. 90 deg == 100grad
| rad | radian. 180deg == 3.1416rad
| turn | 90deg = 0.25turn

## Time Units
| Unit | Description |
| - | - |
| s | Seconds |
| ms | Milliseconds |

---
## Reference
- https://developer.mozilla.org/ko/docs/Learn/CSS/Introduction_to_CSS/Values_and_units
- https://developer.mozilla.org/ko/docs/Web/CSS/length
- https://www.w3schools.com/cssref/css_units.asp
- https://ko.wikipedia.org/wiki/%EB%B7%B0%ED%8F%AC%ED%8A%B8_(%EC%BB%B4%ED%93%A8%ED%84%B0_%EA%B3%BC%ED%95%99)
