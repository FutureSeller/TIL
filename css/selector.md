## Selector
- 목적: style을 HTML 요소에 적용될지 정의
- 왜? 말 그대로 style을 특정 HTML 요소에 적용하기 쉽도록 하기 위함

### Patterns
#### Universal Selector
- `*`: HTML 내의 모든 요소를 선택 (head도 포함됨)

#### Type Selector
- `p`: 지정된 태그명을 가지는 요소

#### ID Selector
- `#id`: id 값은 중복될 수 없는 유일한 값임

#### Class Selector
- `.class`: class는 중복될 수 있음

#### Attribute Selector
- `a[href]`: 지정된 attribute를 갖는 모든 요소 선택
- `a[target="_blank"]`: 지정된 attribute가 갖는 값을 기준으로 요소 선택
- `h1[title~="first"]`: 지정된 attribute 값이 (공백으로 분리된) 단어를 포함하는 요소 선택
- `p[lang|="en"]`: 지정된 attribute 값과 일치 혹은 연이은 하이픈(en-*)으로 시작하는 요소 선택
- `a[href^="https://"]`: 지정된 attribute 값으로 시작하는 요소 선택
- `a[href$=".html"]`: 지정된 attribute 값으로 끝나는 요소 선택
- `div[class*="test"]`: 지정된 attribute 값을 포함하는 요소 선택 (first_test, test, first test)

#### 후손 셀렉터(Descendant Combinator)
- `div p { color: red; }` : div 요소의 후손 요소 중 p 요소
``` html
<body>
  <div>
    <p> P1 </p> <!-- red -->
    <p> P2 </p> <!-- red -->
    <span><p> P3 </p></span> <!-- red: descendant -->
  </div>
  <p> P4 </p> <!-- initial -->
</body>
```

#### 자식 셀렉터(Child Combinator)
- `div > p { color: red; }` : div 요소의 child 요소 중 p 요소
```
<div>
  <p> P1 </p> <!-- red -->
  <p> P2 </p> <!-- red -->
  <span><p> P3 </p></span> <!-- initial -->
</div>
<p> P4 </p> <!-- initial -->
```

#### Sibiling Combinator
- Adjacent Sibling Combinator: `p + ul`: p 요소의 형제 요소 중 p 요소 바로 뒤에 위치하는 ul 요소들
- General Sibling Combinator: `p ~ ul`: p의 형제 요소 중, p뒤에 위치하는 모든 ul 요소들

#### Pseudo-Class Selector
- 요소의 특정 상태에 따라 스타일을 정의할 때 사용
- 원래 클래스가 존재하지 않지만 가상 클래스를 임의로 지정하여 선택
- `:`을 사용. CSS 표준에 의해 미리 정의된 이름이 있기 때문에 임의의 이름을 사용할 수 없음
- link, visited, hover, active, focus
  - `a:hover { color: red; }`, `input:focus { background-color: yellow; }`
- checked, enabled, disabled
- `:first-child`, `:last-child`
- `ol > li:nth-child(2n)`: ol의 자식 요소 중, li의 짝수번째 요소만을 선택
- `ol > li:nth-child(2n+1)`: ol의 자식 요소 중, li의 홀수번째 요소만을 선택
- `ol > li:nth-child(4)`: ol의 자식 요소 중, li의 4번째 요소
- `ul > :nth-last-child(2n)`: ul 요소의 모든 자식 요소 중에서 뒤에서부터 짝수 번째 요소 선택
- `input:not([type=password])`: 셀렉터에 해당하지 않는 모든 요소를 선택
- `:valid`, `:invalid`: 정합성 검증이 성공한 input 요소 또는 form 요소

#### Pseudo-Element Selector
- `::first-letter`: 콘텐츠의 첫 글자를 선택
- `::first-line`: 콘텐츠의 첫 줄 선택
- `::selection`: 드래그한 콘텐츠를 선택
- `::before`: 콘텐츠의 앞에 위치하는 공간 선택, content 사용 가능
- `::after`: 콘텐츠의 뒤에 위치하는 공간 선택, content 사용 가능
  ```
  h1::before { 
    content: "HTML!!!";
    color: blue;
  }
  ```

--- 

## Reference
- https://developer.mozilla.org/ko/docs/Web/CSS/CSS_%EC%84%A0%ED%83%9D%EC%9E%90
- https://poiemaweb.com/css3-selector
