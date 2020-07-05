# Centering in CSS: A Complete Guide

## Horizontally (수평)

#### inline 혹은 inline-* 요소인가? (like text or links)

> block 레벨의 부모 요소에 들어있는 인라인 요소인 경우: `center`

<details><summary> css </summary><pre>
```css
.center-children {
  text-align: center;
}
```
</pre></details>

inline, inline-block, inline-table, inline-flex 등 inline-* 들에 대해 적용이 가능하다.

#### block 요소인가?

> `margin-left`와 `margin-right`를 auto로 만듬

<details><summary> css </summary><pre>
```css
.center-me {
  margin: 0 auto;
}
```
</pre></details>

요소의 width와 관계 없이 블록 레벨 요소를 가운데 정렬 할 수 있습니다.

#### 하나 이상의 block이 존재하는가?
보통 이런 경우, 하나의 행에 여러개 블록 요소가 있고, 이를 가운데 정렬하기 위함이다.

두 개 이상의 블록 레벨 요소가 매 행마다 horizontally 가운데에 있길 원한다면, `display` 값에 따라 다르다.

https://codepen.io/chriscoyier/pen/ebing

1\. inline-block 인 경우; text-align을 적당히 이용한다.

<details><summary> code </summary><pre>
```html
<style>
.inline-block-center {
  text-align: center;
}

.inline-block-center div {
  display: inline-block;
  text-align: left;
}

</style>
<main class="inline-block-center">
  <div> .... </div>
  <div> .... </div>
  <div> .... </div>
</main>
```
</pre></details>

2\. flexbox

<details><summary> code </summary><pre>
```html
<style>
.flex-center{
  display: flex;
  justify-content: center;
}

</style>
<main class="flex-center">
  <div> .... </div>
  <div> .... </div>
  <div> .... </div>
</main>
```
</details>

하나의 열에 정렬하는 게 아니라, 모든 요소들을 그냥 가운데 정렬하고 싶다면 `margin: 0 auto`를 쓰면된다.

## Vertically (수직)

#### inline 혹은 inline-* 요소인가?

1\. single line?

가끔 inline/text 요소들은 vertically 중앙정렬 되어 있는 것 처럼 보이는데, 그것은 위/아래 padding이 같은 값으로 먹어있기 때문이다.
https://codepen.io/chriscoyier/pen/ldcwq

<details><summary> code </summary><pre>
```html
<style>
main {
  background: white;
  margin: 20px 0;
  padding: 50px;
}

main a {
  background: black;
  color: white;
  padding: 40px 30px;
  text-decoration: none;
}
</style>
<main>
  <a href="#0">We're</a>
  <a href="#0">Centered</a>
  <a href="#0">Bits of</a>
  <a href="#0">Text</a>
</main>
```
</pre></details>

하지만 위의 경우, 줄바꿈(e.g., <br>)이 먹힐 경우 깨지게된다. 그럴 때 `line-height`를 `height`와 같은 값으로 만들어 주면 된다.

<details><summary> css </summary><pre>
```html
<style>
main div {
  height: 100px;
  line-height: 100px;
  white-space: nowrap;
}
</style>
<main>
  <div>
    I'm a centered line.
  </div>
</main>
```
</pre></details>

2\. multiple line?
padding top/bottom을 주는 것으로 같은 효과를 볼 수 있긴 한데, 요소가 table cell인 경우 동작하지 않을 수 있다.
table cell의 경우 `vertical-align` 프로퍼티가 이러한 것들을 제어해준다.

https://codepen.io/chriscoyier/pen/ekoFx

<details><summary> code </summary><pre>
```html
<style>
body {
  background: #f06d06;
  font-size: 80%;
}

table {
  background: white;
  width: 240px;
  border-collapse: separate;
  margin: 20px;
  height: 250px;
}

table td {
  background: black;
  color: white;
  padding: 20px;
  border: 10px solid white;
  /* default is vertical-align: middle; */
}

.center-table {
  display: table;
  height: 250px;
  background: white;
  width: 240px;
  margin: 20px;
}
.center-table p {
  display: table-cell;
  margin: 0;
  background: black;
  color: white;
  padding: 20px;
  border: 10px solid white;
  vertical-align: middle;
}
</style>
<table>
  <tr>
    <td>
      I'm vertically centered multiple lines of text in a real table cell.
    </td>
  </tr>
</table>

<div class="center-table">
  <p>I'm vertically centered multiple lines of text in a CSS-created table layout.</p>
</div>
```
</pre></details>

하지만 우리에겐 강려크한 flex가 있다. (https://codepen.io/chriscoyier/pen/uHygv)

위의 두가지 경우엔 항상 parent 요소의 height 값이 항상 정해져 있는 경우에 working한다.

"ghost element"라는 트릭이 있고, full-height pseudo-element를 컨테이너에 넣어두고 `vertical-align`시키는 방법이다.
(https://codepen.io/chriscoyier/pen/ofwgD)

<details><summary> code </summary><pre>
```html
<style>
body {
  background: #f06d06;
  font-size: 80%;
}

div {
  background: white;
  width: 240px;
  height: 200px;
  margin: 20px;
  color: white;
  resize: vertical;
  overflow: auto;
  padding: 20px;
}

.ghost-center {
  position: relative;
}
.ghost-center::before {
  content: " ";
  display: inline-block;
  height: 100%;
  width: 1%;
  vertical-align: middle;
}
.ghost-center p {
  display: inline-block;
  vertical-align: middle;
  width: 190px;
  margin: 0;
  padding: 20px;
  background: black;
}
</style>
<html>
<div class="ghost-center">
  <p>I'm vertically centered multiple lines of text in a container. Centered with a ghost pseudo element</p>
</div>
</html>
```
</pre></details>


#### block 요소인가?

> 보통 우리는 웹페이지 레이아웃에서 height를 모르는게 일반적입니다.
>> width가 변경되면 리플로우가 발생하면서 height가 변경됨;
>
>> 텍스트 스타일의 차이로 인한 높이 변경;
>
>> 텍스트 양의 차이로 인한 높이 변경;
>
>> 이미지와 같이 aspect ratio를 가지고 있는 경우 height가 바뀌게 됨;


1\. 요소의 height를 알 수 있는가?

운이 좋은 경우인데 (조금 귀찮긴 함) 직접 계산해서 위치를 조정하면 됨

<details><summary>css</summary><pre>

```css
.parent {
  position: relative;
}
.child {
  position: absolute;
  top: 50%;
  height: 100px;
  margin-top: -50px;
}
```

</pre></details>

2\. 요소의 height를 알 수 없는가?

모르는 경우, 전통의 방법을 사용하면 된다.

<details><summary>css</summary><pre>

```css
.parent {
  position: relative;
}
.child {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
```
</pre></details>

3\. 컨테이너의 height에 요소들을 늘리고 싶지 않니?

table과 css display를 적당히 섞어주면 된다. (https://codepen.io/chriscoyier/pen/RmeWvQ)

<details><summary>code</summary><pre>
```html
<style>
body {
  background: #f06d06;
  font-size: 80%;
}

main {
  background: white;
  height: 300px;
  margin: 20px;
  width: 300px;
  position: relative;
  padding: 20px;
  display: table;
}
main div {
  background: black;
  color: white;
  padding: 20px;
  display: table-cell;
  vertical-align: middle;
}
</style>
<main>
  <div>
     I'm a block-level element with an unknown height, centered vertically within my parent.
  </div>
</main>
```
</pre></details>


4\. flexbox를 쓰면 안되니? 역시 flex는 참 강력하다.

## Horizontally + Vertically
1\. 요소의 height/width가 정해져있는 경우라면?

`top: 50%; left: 50%;`를 두고 직접 마진을 계산해서 조정한다.

https://codepen.io/chriscoyier/pen/JGofm

2\. 요소의 크기를 모른다면?

`transform: translate(-50%, -50%)`와 `top: 50%; left: 50%;`

https://codepen.io/chriscoyier/pen/lgFiq

3\. flex

역시 flex는 강력하다. (https://codepen.io/chriscoyier/pen/msItD)

<details><summary>css</summary><pre>
```css
.parent {
  display: flex;
  justify-content: center;
  align-items: center;
}
```
</pre></details>

4\. grid

최근엔 좀 더 강력한 녀석인 grid가 등장했다. (https://codepen.io/chriscoyier/pen/NvwpyK)
음.... 근데 가운데 정렬하려고 이 녀석을 쓰기엔 좀 뭔가 이질감이 든다.

<details><summary>code</summary><pre>

```html
<style>
body, html {
  height: 100%;
  display: grid;
}
.center-me {
  margin: auto;
}
</style>
<div class="center-me">
  I'm centered!
</div>
```

</pre></details>


---
## Referece
- https://css-tricks.com/centering-css-complete-guide/
