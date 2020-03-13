# Partial
> 타입스크립트에서 기본적으로 제공해주는 유틸 타입 중 하나로, 제너릭 타입 T에 대해 프로퍼티들을 Optional하게 변경한다.

정의는 아래와 같다. 

```typescript
type Partial<T> = {
  [P in keyof T]?: T[P]
}
```

대표적인 예시인 TodoItem을 가지고 생각해보자. 보통 id, 컨텐츠, 완료 여부를 가지고 있기때문에 타입은 아래와 같다.

```typescript
interface TodoItem {
  id: number
  content: string
  label: string
  isCompleted: boolean
  ...
}

function create(todoItem: TodoItem) {
  setState(todoItemList.concat(
  {
    id: ...,
    content: ...
    label: ....
    isCompleted: ...
  }))
}
```

개발을 하다보면 값의 일부만 바라보고 변경하며 상태를 관리하는 경우가 생긴다.

예를 들면 label 같은 값을 빈 값으로 뒀다가 나중에 채우고 싶을 수 있다.

하지만 위의 타입 명세에서는 모든 값이 required기 때문에 label도 생성할 때마다 번거로움이 생기는데 이를 줄여줄 수 있다.


```typescript
type PartialTodoItem = Partial<TodoItem>

// 위의 type은 아래와 같다.
interface PartialTodoItem {
  id?: number
  content?: string
  label?: string
  isCompleted?: boolean
}

function create(todoItem: PartialTodoItem) {
  setState(todoItemList.concat(
  {
    id: ...,
    content: ...
  }))
}
```


(여기서부터는 개인적인 생각)

여기서 이런 생각이 빠르게 스쳐지나갈 수 있다.

> 처음부터 타입 잘 나누거나 혹은 Optional한 프로퍼티를 명세하면 되지 않겠는가?

예시가 너무 간단해서 쉬워 보일 수 있지만 현실은 항상 녹록치 않다. 

요구사항이 프로젝트 도중에 변경되거나, 해당 타입이 상당히 많은 컴포넌트에 영향을 준다면 이에 따른 위험부담 + QA등 리소스가 소모될 수 있음을 감안해야한다.

따라서 상황에 맞게 쓰면 될 것 같다는 결론이다.

---

## Reference
- https://www.typescriptlang.org/docs/handbook/utility-types.html#partial
- https://dev.to/nickraphael/typescript-partial-t-where-have-you-been-my-whole-life-4ig4
