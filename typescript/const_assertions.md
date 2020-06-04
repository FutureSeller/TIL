업무를 진행하던 중, 사용돌 배열에 들어있는 문자열 리터럴들을 타입으로 만드는 방법이 궁금해졌다.

```typescript
const FRUITS = ['apple', 'banana', 'orange'] as const
type FruitTypes = typeof FRUITS[number]
```

위와 같이 사용하면 되는데, 이때 `as const`가 어떤 의미를 갖는 지 궁금해져서 찾아보았다.

## Const Assertions
> 리터럴 타입에 대해 조금 더 명시적으로 type을 정의하고자 사용함

- type widening: 기존에 정의된 타입보다 좀 더 제너럴한 타입으로 확장 되는 현상
- 타입 추론의 범위를 좁혀주기 위해 const assertion을 사용한다.


#### No literal types in that expression should be widened
- let 변수에 대해서 const 변수를 사용할 때와 같은 타입 추론 규칙을 적용 가능함
- 흠. 그냥 const를 쓰면 되는 거 아닌가.

```typescript
const x = 'x' // x has the type 'x'
let y = 'y' // y has the type string

let z = 'z' as const // z has type 'z'; let z: 'z'
z = 'y' // error
```

#### Object literals get `readonly` properties

```typescript
const action = { type: 'INCREMENT } // has type { type: string }
action.type = 'DECREMENT'
```

`action`을 const로 둔다고해서 프로퍼티를 변경할 수 없는 것은 아니다.
위의 `action`의 `type` 프로퍼티에 type widening이 발생하여 string 타입이 되었기 때문이다.

아주 기본적인 Redux의 예시를 보자.

```typescript
const setCount = (n: number) => {
  return {
    type: 'SET_COUNT',
    payload: n
  }
}

const action = setCount(3) // { type: string, payload: number } >> type widening!
```

우리는 이것을 회피하고자 보통 아래와 같이 action의 interface나 type을 정의하곤 한다.
```typescript
interface SetCount {
  type: 'SET_COUNT'
  payload: number
}

const setCount = (n: number): SetCount => {}
```

하지만, Redux의 모든 액션을 저렇게 정의하는 건 매우 귀찮고 피곤한 일이다. 이때 `const assertion`이 유용하다.
```typescript
const setCount = (n:number) => {
  return <const>{
    type: 'SET_COUNT',
    payload: n
  }
}

const action = setCount(3) // { readonly type: "SET_COUNT", readonly payload: number }
```

`const assertion`을 통해 readlonly 가 되며, 각 프로퍼티는 해당 값이 타입으로 추론된다.
나아가 아래와 같이 확장할 수 있다.

```typescript
const setCount = (n: number) => {
  return <const>{
    type: 'SET_COUNT',
    payload: n
  }
}

const resetCount = () => {
  return <const>{
    type: 'RESET_COUNT'
  }
}

type CountActions = ReturnType<typeof setCount> | ReturnType<typeof resetCount>;
```

TS의 discriminated union이라는 기능이 있는데, const assertion을 주면 따로 type guard를 만들어주지 않아도 된다.
아래의 예제는 JS에서는 문제가 없지만 TS에서는 type widening으로 인해 문제가 된다.

```typescript
const circle = {
  type: 'circle',
  radius: 10
}

const square = {
  type: 'square',
  width: 10,
  height: 20
}

type Shape = typeof circle | typeof square; // { type: string, radius: number } | { type: string, width... }

function draw(shape: Shape) {
  switch(shape.type) {
    case 'circle': 
      console.log(shape.radius)
      break
    case 'square': ...
  }
}
```

이 경우, circle과 square의 각 type에 const assertion을 주거나 객체 자체에 const assertion을 주면 된다.

#### Array Literals become `readonly` tuples
```typescript
const action = {
  type: 'SET_HOURS',
  payload: [8, 12, 5, 8],
} // { type: string, payload: number[] }

action.payload.push(12) // no error

const action = {
  type: 'SET_HOURS',
  payload: [8, 12, 5, 8],
} as const

action.payload.push(12) // Property 'push' does not exist on type 'readonly [8, 12, 5, 8]'.
```

결과적으로 property들이 type widening 되어 다른 타입이 들어갈 수 있는 경우를 의미하는데 interface를 잘 정의하면 이런 일이 없을 수도 있을 것 같다.
하지만 Redux의 예시 처럼, 모든 케이스에 대해 interface를 다 만들어야하는 번거로움이 있을 때 꽤나 유용하게 사용할 수 있을 것 같다.

---

## Reference
- https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-4.html#const-assertions
- https://blog.logrocket.com/const-assertions-are-the-killer-new-typescript-feature-b73451f35802/
- https://medium.com/@seungha_kim_IT/typescript-3-4-const-assertion-b50a749dd53b
