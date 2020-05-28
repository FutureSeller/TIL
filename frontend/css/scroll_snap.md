# Scroll snap
> 사용자가 터치, 휠 스크롤 조작을 마쳤을 때 오프셋을 설정할 수 있도록 하는 모듈

## 배경
- 스크롤링의 정밀도가 부족하여 컨텐츠의 중간에서 멈추거나 일부만 보일 때
- 미리 설정한 위치로 이동하면 자연스러운 스크롤 움직임과 함께 사용자 경험을 향상 시킬 수 있음

## Browser Support
- https://caniuse.com/#feat=css-snappoints

## 요소

### Scroll Container
- Scroll snap 동작이 발생하는 영역
- 스크롤 컨테이너에 있는 요소를 적당히 스크롤 시켜 바른 위치에 보이게 하기 위함
- 사용자가 스크롤링하면 해당 컨테이너에서 Scroll snap이 동작함

#### `scroll-snap-type`
- snap position을 지정할 수 있는 축과 엄격도를 지정
- `scroll-snap-type: axis strictness`
  - axis: x(가로), y(세로), block(area의 block 축), inline, both
  - strictness: none, proximity(snap-position or 유저 에이전트에 따름), mandatory(강제)

#### `scroll-snap-stop`
- 스크롤 중 스냅 위치가 여러개 나올 때 정책
- normal, always

#### `scroll-padding`
- 컨테이너의 패딩 값이 변경되는 것이 아닌, 해당 뷰포트에 패딩이 적용됨

### Snap area
- 컨테이너 내부의 각 요소
- 스크롤링 시 타겟이 되는 오브젝트

#### `scroll-snap-align`
- snap area안에서 원하는 정렬 방식을 설정
- snap-type에서 지정한 축을 기준으로 정렬을 정함
- none, start, end, center

#### `scroll-margin`
- scroll-padding과 동일하게 실제 요소에 영향을 미치지 않음

---

## Reference
- https://wit.nts-corp.com/2018/08/28/5317
- https://css-tricks.com/practical-css-scroll-snapping/
- https://www.w3.org/TR/css-scroll-snap-1/
