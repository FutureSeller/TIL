https://codepen.io/FutureSeller/pen/OJagOBX

flex가 아주 많이 nested된 컴포넌트에 말줄임표(`text-overflow: ellipsis`)를 넣어보려고했다.

---

우선, `text-overflow: ellipsis`를 넣으려면 두 가지의 속성이 함께 쓰여야한다.

```css
text-overflow: ellipsis;
overflow: hidden;
white-space: no-wrap;
```

한줄로 만들고, 요소의 범위를 넘어가면 숨기는데, ellipsis를 적용해주겠다는 의미이다.
물론, inline 요소에는 fit-content하게 너비가 잡히기 때문에 ellipsis가 적용되지 않는다. (최소 길이가 content니까)

---

flex에 저 속성을 먹이려면, flex item의 동작 방식을 생각해봐야한다. flex item의 min-width, min-height가 auto이기 때문에, 줄어들 수 없기때문이다. [css-flexbox-1/#min-size-auto](https://www.w3.org/TR/css-flexbox-1/#min-size-auto)
flex item이 아닌 녀석들의 최소 크기는 일반적으로 0이다. (스크롤 컨테이너라 부르는 듯 + min-width: 0). 

<details><summary>그렇다면 https://www.w3.org/TR/css-overflow-3/#scroll-container, https://www.w3.org/TR/css-overflow-3/#scrolling 란 무엇인가?</summary>

- 스크롤 컨테이너: 클리핑 된 영역을 유저가 스크롤 해서 볼 수 있는 컨테이너
- 스크롤 포트: 스크롤 컨테이너의 시각적 뷰포트. 패딩 박스와 일치함. 스크롤 포트를 통해 오버플로우 영역을 볼 수 있다.

쉽게말하면, overflow 속성 값으로 hidden, auto, scroll이 적용되는 요소를 의미한다.
</details>



그렇다면 flex item의 min-width를 0으로 만들어주면 스크롤 컨테이너가 되어 ellipsis를 먹일 조건이 충족된다. 
이게 flex 컨테이너의 depth가 1일땐 참 간단하다. (https://codepen.io/FutureSeller/pen/XWygVmo)

이럴일이야 잘 없겠지만, 아래 처럼 depth가 하나만 더 깊어져도 동작하지 않는다.

<details><summary>예시</summary>

```html
<style>
.container {
  display: flex;
  width: 500px;
  background-color: tomato;
}

.number {
  width: 100px;
  background-color: aqua;
}

.depth-1 {
  display: flex;
}

.depth-2 {
  min-width: 0;
}

.text {
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}
</style>
<div class="container">
  <div class="number">1</div>
  <div class="depth-1">
    <div class="depth-2">
    <p class="text">
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quod
                dolorum atque a. Corporis eius odio similique sunt quibusdam
                doloremque dolorem totam neque? Modi quo optio aut consectetur
      amet. Minus, qui?</p>
    </div>
      </div>
</div>
```

</details>

위의 예시의 경우 depth-1에도 `min-width: 0`를 넣어서 스크롤 컨테이너로 만들어줘야한다. 
아주아주 만약에 depth가 매우 깊은 경우, 말줄임을 하고 싶은 요소가 깊다면, 감싸고 있는 모든 flex 컨테이너에 min-width: 0를 넣어줘야한다는 말이다.
(최상단 flex 컨테이너인 `.container`의 flex-item까지... 중간에 하나만 빼먹어도 min-width는 auto로 강제된다.)

---
## Reference
- https://dfmcphee.com/flex-items-and-min-width-0/
