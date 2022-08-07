# Conditional Types

## Conditional Type Constraints

interface에서 `extends`는 상속을 의미한다. conditional type에선 extends는 LHS가 RHS를 확장하고 있는지 여부에 따라 삼항연산자를 수행한다.

```typescript
type MessageOf<T> = T extends { message: unknown } ? T["message"] : never;

interface Email {
  message: string;
}
type EmailMessageContents = MessageOf<Email>; // string

interface Dog {
  bark(): void;
}
type DogMessageContents = MessageOf<Dog>; // never;
```

## Inferring Within Conditional Types

`infer`는 타입 스크립트가 엔진이 런타임 상황에서 타입을 추론할 수 있도록한다.
`infer` 키워드는 조건문에 쓰이는 타입 중 하나를 이름붙여 빼와서, 삼항 연산자의 true, false 절에 사용하기 위해 사용한다.


`type Flatten<Type> = Type extends Array<infer Item> ? Item : Type;`

---
## Reference
- https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#handbook-content

