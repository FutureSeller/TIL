## `object-fit`
> 대체되는 요소의 내용(img, video, object, sgv 등)이 지정된 너비와 높이에 맞게 장착되는 방식을 지정함

#### fill
- 대체되는 요소의 내용이 **지정된 너비와 높이에 따라** 크기가 확대, 축소, 늘어나거나 줄어듬
- 요소를 가득 채울 수 있는 크리고 변화 하면서 종횡비는 유지되지 않음

#### contain: 내용이 종횡비를 유지하면서 요소에 정의된 너비와 높이 안에서 가능한 많이 확대

#### cover: 종횡비를 유지하면서 정의된 너비와 높이를 가득채울 때 까지 확대

#### none: 요소의 크기와는 상관없이 기본 알고리즘에 의해 조정됨. 가운데 정렬된 형태

#### scale-down: 아무것도 지정되지 않거나 contain이 지정되어 있는 것 처럼. 원본보다 작아짐


## `object-position`
- 기본적으로 요소의 가운데로 화상을 이동 시킴
- 기본 값은 50%, 50%

---
## Reference
- https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit
- https://webdir.tistory.com/486
- Example: https://codepen.io/uzugoer/pen/QjoVVw
