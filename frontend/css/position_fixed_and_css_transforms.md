# Position fixed and CSS transforms

> An HTML element with `position: fixed` will lose its fixed positioning if a CSS transform is applied to its ancestors

- 일반적으로 `position:fixed;`는 viewport를 기준으로 잡힘
- 부모 요소에 CSS transform이 먹혀있다면?
  - 새로운 context(지역 좌표 시스템)를 생성하게 되어 viewport가 아닌 부모를 기준으로 포지셔닝
  - 해당 요소 영역에 새로운 viewport가 설정됨
  - 자식요소가 position:fixed 속성을 가질때 영향을 받음
  - 마치 `position: absolute` 인 양 작동함
- `background-attachment`도 마찬가지라고 함

1\. 요소를 밖으로 빼내거나
2\. JS로 css transform을 제거해버리거나
3\. 둘 다 안되면 적당히 포지셔닝을 해본다.

---
## Reference
- https://achrafkassioui.com/blog/position-fixed-and-CSS-transforms/
- https://marshall-ku.tistory.com/285
- Example: https://codepen.io/FutureSeller/pen/NWWrrdK
