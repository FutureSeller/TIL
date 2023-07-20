flex 컨테이너 하위에 `position: fixed` 요소가 있다고 가정했을 때. left, top 등 위치를 제어하는 어떠한 속성도 주어지지 않았다면
flex layout rule을 따라간다. 

https://codepen.io/FutureSeller/pen/poQVBJq

[스펙](https://drafts.csswg.org/css-flexbox/#change-201403-css21-staticpos)을 좀 찾아보니 정말 그러하다.

> In other words, the static position of an absolutely positioned child of a flex container is determined after flex layout by setting the child’s static-position rectangle to the flex container’s content box, then aligning the absolutely positioned child within this rectangle according to the justify-content value of the flex container and the align-self value of the child itself.
