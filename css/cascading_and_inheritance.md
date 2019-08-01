## CSS(Cascading Style Sheets)
- 스타일, 레이아웃 등을 통해 문서가 유저에게 어떻게 표시되는지 지정하는 "언어"
- 문서(document): 마크업 언어를 사용한 텍스트 파일
- 표시(present): 텍스트를 방문자가 이용할 수 있는 형식으로 전환

### Cascading? Inheritance?
#### Inheritance: 상속
- 상위 요소에 적용된 프로퍼티를 하위 요소가 물려 받는 것
- 모든 프로퍼티가 상속 되는 것은 아님
  - make sense: font-family, color
  - not make sense: margin, padding, border and background-image
- Controlling: 
  - inherit: parent의 property를 상속 받음
  - initial: browser default
  - unset: parent에 매칭되는게 있으면 inherit, 없으면 initial
    - usecases: `input { all: unset }`, reset 처럼 쓸 수 있음
  ``` html
  <style>
  .wrapper { color: orange; }
  .wrapper p { color: purple; }
  p.one { color: inherit; }
  p.two { color: initial; }
  p.three { color: unset; }
  </style>
  <div class="wrapper">
    <p class="one">Snake<p>  <!-- orange: parent is .wrapper -->
    <p class="two">Lizard<p> <!-- browser default -->
    <p class="three">Alligator</p> <!-- orange: parent is .wrapper -->
    <p>Komodo Dragon</p> <!-- purble: .wrapper p -->
  </div>
  ```

#### Cascading
- 요소는 하나 이상의 CSS 선언에 영향을 받을 수 있음
- Cascading Order: 충돌을 피하기 위한 CSS 적용 우선 순위
- Rule1: Importance: CSS가 어디에 선언 되었는 지에 따른 우선 순위
- Rule2: Specificity: 대상을 명확하게 특정한 정도
  - "basically a measure of how specific a selector is"
  - !impotant > 인라인 > #id > .class > tag > * > 상속된 속성
  - four different values (thousands, hundreds, tens and ones)
    - thousands: inline style, don't have selectors
    - hundreds: ID selector
    - Tens: Class selector, attribute selector, or pseudo-class
    - Ones: element selector
  - Universal(*), combinators(+, >, ~, '') and negation(:not) : no effect on specificity 
    ``` html
    <style>
      p { color: red !important; } /* selected */
      #thing { color: blue; }
      
      div.food { color: chocolate; } /* selected */
      .food { color: green; }
      div { color: orange; }
    </style>
    ...
    <p id="thing"> Will be Red </p>
    <div class="food"> Will be Chocolate. </div>
    ```
- Rule3: Source order: 선언된 순서에 따라, 나중에 선언된 스타일이 우선 적용됨
  ``` html
  p { color: blue; }
  p { color: red; } /* selected because of Source order*/
  ```
  
  ``` html
  .footnote { color: blue; } /* selected because of specificity: 0010 */
  p { color: red; } /* specificity: 0001 */
  ```

---
## Reference
- https://poiemaweb.com/css3-inheritance-cascading
- https://developer.mozilla.org/ko/docs/Learn/CSS/Introduction_to_CSS/Cascade_and_inheritance
- https://alligator.io/css/inherit-initial-unset/
