# display: flex

## flexbox
> 뷰포트나 요소의 크기가 불명확/동적으로 변할 때에도 효율적으로 요소를 배치,
정렬, 분산할 수 있는 방법
>> 장점: 복잡한 계산 없이 요소의 크기와 순서를 유연하게 배치

``` css
.flex_container {
  display: flex;
}
```

- flex container
  - 전체적인 정렬이나 흐름
  - flex-direction, flex-wrap, justify-content, align-itmes, align-content
- flex item
  - 자식 요소의 크기나 순서
  - flex, flex-grow, flex-shrink, flex-basis, order
- keywords
  - initial: { flex: 0, 1, auto }
  - none: { flex: 0, 0, auto }
  - auto: { flex 1, 1, auto }
  - ${input}: { flex ${input} 1 0 }

---
## 예제 clone하여 습득
### Example 1: 스크롤 없는 100% 레이아웃
- 100% 레이아웃: 전체 페이지를 구성할 때 자주 사용
- flex의 주축의 방향: 왼쪽 → 오른쪽으로 향하는 수평 방향
- `flex:1`: 자식 요소의 크기 확장
  - `flex { flex: ${flex-grow} ${flex-shrink} ${flex-basis}; }`
  - `{ flex: 2; } == { flex: 2 1 0 } = { flex: flex-grow: 2; ...}`
  - flex-grow: flex item의 확장에 관련된 속성
    - 0: flex item의 크기가 커지지 않고 원래 크기로 유지
    - 1: continer가 커질 때, item도 커지게
    - >=1: item의 원래 크기에 상관 없이 flex container를 채우도록 item이 커짐
  - flex-shirnk: flex item의 축소에 관련된 속성
    - 0: 원래 크기 유지
    - >=1:container의 크기에 맞추어 줄어듬
  - flex-basis: 기본 크기. 기본 값은 auto
    - width 속성에서 사용하는 모든 단위 사용 가능 (30px, 30% ..)
    - 0: 절대적 flex item; flex container를 기준으로 크기 결정
    - 단위도 함께 설정 해야 함: `flex-basis: 0px, flex-basis: 0%`
- <details><summary> CSS Example </summary><p>

  ``` css
  html, body {
    height: 100%;
  }

  .flex_container {
    display: flex;
    flex-direction: column; /* 주축의 방향을 바꿈. flex item을 수직으로 정렬 */
    height: 100%
  }

  .flex_item {
    flex: 1;  /* flex 1 1 0 */
    overflow: auto;
  }

  ```
  </p><details>

### Example 2: 내비게이션
- `flex:none`: 크기가 고정되어야 하는 flex item
  - 기본 값: `flex: 0 1 auto`: container의 flex item의 크기보다 작아질 때, item의 크기가 작아짐
  - `flex :none`: flex item의 크기 고정 == `flex: 0, 0, auto`
- `margin-left: auto`: flex item의 바깥 여백이 자동으로 확장
  - flex item이 flex container 가운데에 위치하게 됨
  - `margin-right: auto`: 바깥 여백이 오른쪽 모든 공간을 차지하기 위해 item을 왼쪽으로 민다
  - `margin: 0 auto`: 양쪽에서 밀기 때문에 flex item이 수평 중앙에 위치
  - `margin-left: auto`: 바깥 여백이 왼쪽 모든 공간을 차지하기 위해 item을 오른쪽으로 민다
  - 같은 원리로 `margin-bottom: auto`, `margin: auto 0`, `margin-top: auto`

### Example 3: Footer
- 화면의 맨 아래 딱 붙는 모습을 기대함. 
- 콘텐츠의 길이가 화면보다 짧으면 짧아진 만큼 위로 올라감
- <details><summary> CSS Example </summary><p>

  ``` css
  .flex-comtainer {
    display: flex;
    flex-direction: column;
  }
  .flex_item {
    margin-top: auto;
  }

  ```
  </p><details>

### Example 4: 정렬이 다른 메뉴
- `justify-content`: 주축을 기준으로 flex item을 수평으로 정렬함
  - flex-start: 주축의 시작부분을 기준으로 flex item 정렬
  - center: 주축의 중앙을 기준으로
  - flex-end: 끝부분을 기준으로
  - space-around: 주축을 기준으로 일정한 간격으로 정렬
  - space-between: 첫 번째와 마지막은 시작과 끝부분, 나머지는 일정한 간격으로 정렬

![image](https://d2.naver.com/content/images/2018/12/helloworld-201811-flex_19.png)

### Example 5: 폼 레이블 수직 중앙 정렬
- `align-items`: 자식 요소를 교차 주축을 기준으로 flex item을 수직 정렬
  - stretch: container 전체 높이를 채움
  - flex-start: 시작 부분을 기준으로 정렬
  - center: 중앙을 기준으로 정렬
  - baseline: 글꼴 기준선인 baseline을 기준으로 정렬
  - flex-end: 끝부분을 기준으로 정렬
![image](https://d2.naver.com/content/images/2018/12/helloworld-201811-flex_21.png)

### Example 6: 중앙 정렬
``` css
.flex_container {
  display: flex;
  align-items: center;
  justify-content: center;
}

/* alternatives */
.flex_container {
  display: flex
}
.flex_item {
  margin: auto
}
```

### Example 7: 유동 너비 박스
- https://codepen.io/witblog/pen/oPyvEa
``` css
.flex_container {
  display: flex;
}
.flex_item {
  /* flex: initial */
  max-width: 300px; /* 요소의 width가 해당 값보다 커지는 것을 방지 */
}
```

### Example 8: 말줄임과 아이콘
- flex container인 부모 요소의 크기가 작아 flex item의 텍스트 요소를 모두 표시할 수 없을 때
- `display: inline-flex`: inline 블록 요소로 만듬. `display:flex`는 블록 요소.
``` css
.flex_container {
  display: inline-flex;
  max-width: 100%;
}
.text {
  overflow: hidden;
  text-overflow: ellipsis; /* 줄임표를 이것으로 구현한다고 함*/
  white-space: nowrap;
}
```

### Example 9: 위아래로 흐르는 목록
- `flex-direction`: default는 row, column으로 바꾸면 수직
![image](https://d2.naver.com/content/images/2018/12/helloworld-201811-flex_30.png)
- `flex-wrap`: flex item이 flex container를 벗어날 때 줄을 바꾸는 속성
  - white-space와 동일하게 작동
  - default인 nowrap은 flex item의 전체 크기가 container보다 커져도 한 줄로 item을 배치
  - wrap: 줄을 바꿔 여러 줄로 flex item을 배치
- `align-content`: flex item이 여러 줄로 나열될 때, 주축을 기준으로 수직정렬
  - stretch, flex-start, center, flex-end
  - space-around: 교차축을 기준으로 일정한 간격으로 정렬
  - space-between: 첫 번째와 마지막은 축을 기준으로 양끝, 나머지는 일정한 간격

``` css
.flex_container {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;  /* flex-flow: column wrap; */
  justify-content: space-around;
  align-content: space-around;
}
```

### Example 10: 가로세로 비율을 유지하는 반응형 박스
- `flex-basis`: 목록을 이루는 항목 요소가 일정한 비율로

--- 
## Reference
- https://d2.naver.com/helloworld/8540176
- https://css-tricks.com/snippets/css/a-guide-to-flexbox/

## Appendix
#### overflow: 요소의 박스에 내용이 더 길 때, 어떻게 보일지 선택하는 속성
- visible (default): 내용이 더 길어도 그대로 보임
- hidden : 자른 부분 보이지 않음
- scroll : 내용이 넘치지 않아도 항상 스크롤바가 보임
- auto : 내용이 잘릴 때만 스크롤바가 보임
