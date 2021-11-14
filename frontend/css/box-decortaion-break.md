# box-decoration-break

> The box-decoration-break property lets you control how box decorations are drawn across the fragments of a “broken” element. 
> An element can break into fragments at the end of a line, over columns, or at page breaks.

- element가 fragment 들로 쪼개진 상황에서 스타일을 어떻게 어떻게 할 것인가에 대한 프로퍼티
- values
  - slice: "initial". 끊어진 fragment들이, 끊어지지 않은 box 처럼 스타일이 적용됨.
  - clone: 복제된 스타일이 모든 fragment들에 똑같이 적용됨. 각 fragment들이 독립적으로 스타일링됨.
- 영향 받는 값들
  - background
  - border
  - border-image
  - box-shadow
  - clip-path
  - margin
  - padding


--- 
## Reference

- https://developer.mozilla.org/en-US/docs/Web/CSS/box-decoration-break
- https://css-tricks.com/almanac/properties/b/box-decoration-break/
