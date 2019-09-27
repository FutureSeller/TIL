## Nullish Coalescing (Stage 3)
해당 feature가 proposal되기까지 truthy, falsy에 대한 이해가 필요하다.

v8.dev를 천천히 읽다가 재밌는 걸 발견했다. 아래의 코드를 보면,

``` javascript
function Component(props) {
  const data = props.data || [];  // [1]
  const enable = props.enabled || true; // [2]
  const value = props.value || 100; // [3]
}
```

보통 falsy인 값을 특정 값으로 초기화하고자 할 때 쓰는데,
[1]의 경우는 크게 문제가 될 게 없는데 
[2,3]의 경우 의도치 않은 버그가 생길 수 있다.

`props.enabled` 값에 따라 뒤의 행동이 결정된다고 가정해보자.

> 개발자의 의도: `undefined`일 때, true로 default 값을 설정

default 값을 정하는 건 좋은데, `||` operator의 원래의도는 or 이다.
따라서, `props.enabled`가 false 일 때 값을 true로 강제로 바꿔버리는 의도치 않은 결과로 이어질 수 있어 아래와 같이 수정할 수 있다.

```javascript
const enable = props.enabled !== false
```

[3]의 경우, 숫자 0이 [2]에 해당할 수 있다.
문제는 [2]와 같이 lhs가 boolean이 아닌 경우
`if-then-else`나 `ternary`를 사용해야하는 번거로움이 있다.

``` javascript
// ternary
const value = props.value === undefined ? 0 : 100;

// if-then-else
let value = props.value;
if (value === undefined) {
  value = 100;
} 
```

위의 번거로움을 막기 위해 nullish coalescing (`??`)이 제안되었다.
nullish는 undefined와 null만을 지칭하며, falsy와 구분되어 사용되어야 한다.

``` javascript
// props.value : 0 -> 0
// props.value : [undefined | null] -> 100
const value = props.value ?? 100;

// props.enable : false -> false
// props.enable : [undefined | null] -> true
const enable = props.enable ?? true;
```

---
## Reference
- https://v8.dev/features/nullish-coalescing
- https://github.com/tc39/proposal-nullish-coalescing
