> React는 강력한 합성 모델을 가지고 있으며, 상속 대신 합성을 사용하여 컴포넌트 간 코드를 재사용하는 것이 좋습니다.

### 컴포넌트에서 다른 컴포넌트를 담기
- 어떤 children이 들어올지 미리 예상할 수 없는 경우
- `children` prop을 사용하여 자식 엘리먼트를 출력에 그대로 사용

``` javascript
function FancyBorder(props) {
  return (
    <div ....>
      {props.children}
    </div>
  )
}
```

### 특수화
- 더 "구체적인" 컴포넌트가 "일반적인" 컴포넌트를 렌더링하고 props를 통해 내용 구성
``` javascript
function Dialog(props) {
  return (
    <div ...>
      <h1>{props.title}</h1>
      <p> {props.message} </p>
      { props.children }
    </div>
  )
}

function SpecificDialog() {
  return (
    <Dialog title="Welcome" message="Hello World!">
      <........./>
    </Dialog>
  )
}
```

### Inheritance
> Facebook에서는 수천 개의 React 컴포넌트를 사용하지만, 컴포넌트를 상속 계층 구조로 작성을 권장할만한 사례를 아직 찾지 못했습니다.
> rops와 합성을 통해 컴포넌트의 모양과 동작을 명시적이고 안전한 방법으로 사용자 정의하는 데 필요한 유연성을 모두 얻을 수 있습니다. 
> 컴포넌트는 원시 값, React 엘리먼트 또는 함수를 비롯한 임의의 props를 받아들일 수 있다는 점을 기억하십시오.

### Questions
- 왜 Inheritance를 권장할 만한 사례가 없지?
  - Props + 합성: 명시적이면서 안전함. 유연성을 제공한다고 함.
  - 여러 사람들의 경험(?)에서 비롯된 것 말고 다른 이유가 있을 것 같은데?
  - 예를 들면, 모두 같은 method를 사용하는 Button인데 style만 다르거나 text만 다름.
    - 즉, 내부 구조가 변할일이 없는 어떤 컴포넌트가 있음.
    - 근데 나름 Component를 나눠서 관리하고 싶음. (SuccessButton, DiscardButton 이라던지)
  - https://www.reddit.com/r/reactjs/comments/9eqh52/what_are_the_motivations_behind_not_using/
    - Easy to debug: 결국 root cause를 찾기 어렵기 때문에. composition은 명시적이라 따라가기 쉬움
      - UI identification: composition의 경우 wrapped component와 같이 보여주는데, 상속의 경우, prototype chain의 마지막만 보여줌
      - `complex inheritance hell` (어떤 컴포넌트의 method가 문제가 생겼을 때, 찾기 어려움)
    - Suitability: "Lifecycle methods"
      - lifecycle method들에 상속이 발생한 subclass에서 overwrite을 했다고 가정
      - 각 lifecycle method들에 상응하는 `super.xxxx`를 개발자가 명시적으로 call해야함.
      - `no way to have parent's prev/next props or state in a child`
---
## Reference
- https://ko.reactjs.org/docs/composition-vs-inheritance.html
