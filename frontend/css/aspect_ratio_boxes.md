# Aspect Ratio Boxes

## The Core Concept: padding in percentages is based on width

부모 요소의 `width`를 고정해두고 `padding-top`이나 `padding-bottom`을 조정한다.

예를 들면, 요소의 width가 500px일 때, padding-top 100%은 500px임을 이용하는 것이다.

- 요소의 height를 0으로 강제하고, border를 없앰
- box-model에서 이를 이용하면 padding으로 square를 만들 수 있음

이런 특성을 이용해서 56.25%(9/ 16 = 0.5625) top padding을 주면 16:9 와 같은 비율의 box를 만들 수 있다.

---
## Reference
- https://css-tricks.com/aspect-ratio-boxes/
