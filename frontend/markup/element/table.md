# A Complete Guide to the Table Element

## Basic Example
```html
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>ID</th>
      <th>Favorite Color</th>
    </tr>
  </thead>
  <tfoot>
    <tr>
      <th>Footer: N</th>
      <th>Footer: I</th>
      <th>Footer: F</th>
    </tr>
  </tfoot>
  <tbody>
    <tr>
      <td>Jim</td>
      <td>00001</td>
      <td>Blue</td>
    </tr>
    <tr>
      <td>Sue</td>
      <td>00002</td>
      <td>Red</td>
    </tr>
    <tr>
      <td>Barb</td>
      <td>00003</td>
      <td>Green</td>
    </tr>
  </tbody>
</table>
```
</details>

#### Rows: Head, Body and Foot
- tr(tabular rows): 하나의 행을 표현하는데 쓰임
- Head
  - 열 제목으로 구성된 행의 집합
  - table에서 한번만 쓸 수 있음
  - tbody나 tfoot보다 먼저 선언되어야 함
- Body: 모든 데이터가 표현되는 곳
- Foot
  - 도표 하단에 나오는 열의 요약: 테이블의 맨 마지막에 위치
  - table에서 한번만 쓸 수 있음

#### Cells: td and th
- th(tabular headers)
- td(tabular data)

#### Caption
- 표의 제목을 나타냄. table 요소의 첫 번째 child가 되어야 함
- 접근성에 있어 필수적임
- `caption-side`: top, bottom 같은 값으로 캡션의 위치를 조정(https://developer.mozilla.org/en-US/docs/Web/CSS/caption-side)

## Styling
- `border-spacing`: 인접한 표 셀의 테두리간 간격
- `border-collapse`
  - seperate: 표의 테두리와 셀의 테두리 사이에 간격을 둠
  - collapse: 표의 테두리와 셀의 테두리 사이의 간격을 없앰

#### Connecting Cells
- colspan: 열들을 병합. `<td colspan="2"> ... </td>`
- rowspan: 행들을 병합. `<td rowspan="3"> ... </td>`
- example: https://codepen.io/chriscoyier/pen/fixJg

## Use cases

#### Layout 처럼 쓰이는 경우
- tr이 블록 레벨 요소 처럼 동작하기 때문에 컨테이너처럼 쓰이기도 했음 (요즘은 흐음. flex/grid 가 있음)
- https://codepen.io/chriscoyier/pen/JnLIt
- text를 wrap이 없도록 하면 `white-space: nowrap;`을 쓰면 되긴 하는데, text의 길이만큼 요소가 늘어나서 스크롤이 생길 수 있음

#### Two Axis Tables
<details><summary> Example </summary>

https://codepen.io/chriscoyier/pen/qJBpF

```html
<style>
td, th {
  width: 4rem;
  height: 2rem;
  border: 1px solid #ccc;
  text-align: center;
}
th {
  background: lightblue;
  border-color: white;
}
body {
  padding: 1rem;
}
</style>
<table>
  <tr>
    <th>1</th>
    <th>2</th>
    <th>3</th>
    <th>4</th>
    <th>5</th>
  </tr>
  <tr>
    <th>2</th>
    <td>4</td>
    <td>6</td>
    <td>8</td>
    <td>10</td>
  </tr>
  <tr>
    <th>3</th>
    <td>6</td>
    <td>9</td>
    <td>12</td>
    <td>15</td>
  </tr>
  <tr>
    <th>4</th>
    <td>8</td>
    <td>12</td>
    <td>16</td>
    <td>20</td>
  </tr>
</table>
```

</details>

#### Zebar Striping Tables
```css
tbody tr:nth-child(odd) {
  background: #eee;
}
```

#### Highlighting

<details><summary> Example </summary>
```html
<style>
col:nth-child(3) {
  background: yellow; 
}
</style>
<table class="zebra"> 
<col>
<col>
<col>
<col>
<col>
<thead> 
<tr> 
    <th>Last Name</th> 
    <th>First Name</th> 
    <th>Email</th> 
    <th>Due</th> 
    <th>Web Site</th> 
</tr> 
</thead> 
<tbody> 
<tr> 
    <td>Smith</td> 
    <td>John</td> 
    <td>jsmith@gmail.com</td> 
    <td>$50.00</td> 
    <td>http://www.jsmith.com</td> 
</tr> 
<tr> 
    <td>Bach</td> 
    <td>Frank</td> 
    <td>fbach@yahoo.com</td> 
    <td>$50.00</td> 
    <td>http://www.frank.com</td> 
</tr> 
<tr> 
    <td>Doe</td> 
    <td>Jason</td> 
    <td>jdoe@hotmail.com</td> 
    <td>$100.00</td> 
    <td>http://www.jdoe.com</td> 
</tr> 
<tr> 
    <td>Conway</td> 
    <td>Tim</td> 
    <td>tconway@earthlink.net</td> 
    <td>$50.00</td> 
    <td>http://www.timconway.com</td> 
</tr> 
</tbody> 
</table> 

```

</details>

## 언제 Table을 쓰면 좋고, 언제 쓰면 안되는 가?
> tables are for tabular data 

- spread sheet 같은 것을 고려한다거나, grid 같은 경우 사용을 고려해볼 수 있음
- layout or container를 나타내고자 할 때 적절하지 않음
  - Semantics: HTML tag; 의미상 맞지 않음
  - Accessibility; Screen Reader에 의해 읽힐 때 의미 없는 순서로 읽을 수 있음
  
## Semantic Elements 들을 Table 처럼 쓰는 방법
```html
<section style="display: table;">
  <header style="display: table-row;">
    <div style="display: table-cell;"></div>
    <div style="display: table-cell;"></div>
    <div style="display: table-cell;"></div>
  </header>
  <div style="display: table-row;">
    <div style="display: table-cell;"></div>
    <div style="display: table-cell;"></div>
    <div style="display: table-cell;"></div>
  </div>
</section>
```

```css
display: table;                /* <table>     */
display: table-cell;           /* <td>        */
display: table-row;            /* <tr>        */
display: table-column;         /* <col>       */
display: table-column-group;   /* <colgroup>  */
display: table-footer-group;   /* <tfoot>     */
display: table-header-group;   /* <thead>     */
```

## Scope: Accessilbility를 위한 속성
- th에 사용하는 속성으로 제목과 내용을 연결해주는 기능
- 스크린 리더가 어느 방향으로 순서대로 읽을 지 명시해줌

---
## Reference
- https://css-tricks.com/complete-guide-table-element/
- https://www.codingfactory.net/10616
- http://webberstudy.com/html-css/html-2/table-symactic/
