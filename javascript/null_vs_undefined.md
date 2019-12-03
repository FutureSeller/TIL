# `null` vs. `undefined`

자세히 알아보기 전, 내가 가지고 있던 intuition은 다음와 같다.

두 가지의 공통점은 값이 없다는 것을 나타내지만 확연하게 다른 의미를 가진다고 생각한다.

`undefined`는 keyword가 암시하는 그대로 유저로부터 정의되지 않은 어떤 값 또는 상태를 나타내고,
초기화 하지 않으면 `undefined`로 할당된다.

`null`은 엄밀히 말하면 유저가 명시적으로 준 값이며 어떤 객체(변수)에 어떤 값이 있었는데,
의도적으로 비어있는 값으로 만들고 싶을 때 쓰는 것이라고 생각한다.

``` javascript
typeof null // 'object'
typeof undefined // 'undefined'
```

## `null` : 존재하지 않는 객체에 대한 참조
> JavaScript의 원시값 중 하나로, 어떤 값이 의도적으로 비어있음을 표현합니다.

> 리터럴로서 식별되지 않은 상태를 나타내며 해당 변수가 어떤 객체도 가리키고 있지 않음을 표시합니다.

> *보통 함수의 반환값이 기대되지만 일치하는 값이 없을 때 대신 사용됩니다.*

## `undefined` : 값이 할당되지 않은 상태
> **전역** undefined 속성은 undefined 원시 값을 나타내며, 원시 자료형 중 하나입니다.

> undefined는 전역 객체의 속성입니다. (전역 스코프에서 변수)

> 값을 할당하지 않은 변수는 undefined 자료형입니다.

> *함수가 값을 명시적으로 반환하지 않으면 undefined를 반환합니다.*


## Wrap up
- null은 의미 없는 특별한 값이 등록되어 있는 것
- undefined는 등록되어 있지 않기때문에 초기화도 정의되지도 않은 것
- undefined는 미리 선언된 **전역변수**, null은 선언, 등록을 할 때 사용되는 **키워드**
  - 이게 말이 되려면, JavaScript를 파싱할 때 룰에 의해 `null`은 identifier가 될 수 없음, `undefined`는 가능해야함.
  - TMI
    -  V8에서 `null`은 keyword token으로 등록되어있으나 `undefined`는 없음
    - https://github.com/v8/v8/blob/master/src/parsing/token.h#L164, https://github.com/v8/v8/blob/master/src/parsing/keywords.txt
    - `undefined`는 V8엔진을 initialize할 때(정확히 말하면 Isolate를 init할 때), global에 constant로 할당함.

``` javascript
const null // Uncaught Syntax Error: Unexpected token 'null'

const undefined // undefined
const undefined = 1 // Uncaught Syntax Error: Indentifier 'undefined' has already been declared
```

---
## Reference
- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/null
- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/undefined
- https://webclub.tistory.com/1
- https://medium.com/javascript-scene/handling-null-and-undefined-in-javascript-1500c65d51ae
- https://ko.javascript.info/types