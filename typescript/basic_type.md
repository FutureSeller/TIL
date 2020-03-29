## Basic Type
- boolean
- number : ECMAScript에서 지원하는 각종 진수들 모두 지원함 (2, 8, 10, 16)
- string : template string 또한 가능함
- array: `Array<T>` 혹은 `T[]`
- tuple
  ```typescript
  let x: [string, number];
  x = ["hello", 10]; // OK
  x = [10, "hello"]; // Error
  ```
- enum: 기본적으로 0부터 시작하며 값을 바꿀 수 있음
- any: 어떤 타입이든 가능. 어떤 타입이 올지 모를 때 쓰임 + 다양한 타입이 올 수 있는 합성 값 + 혹은 기타 등등의 사유
- void: 보통 함수의 return 값이 없을 때 쓰임. 자바스크립트에서도 `void a === undefined` 이기 때문
  ```typescript
  function warnUser(): void {
    console.log("This is my warning message");
  }
  ```
- null and undefined
- never: 절대로 발생하지 않는 값의 타입. `throw`와 같이 엮여 사용하곤 함
  ```typescript
  function error(message: string): never {
    throw new Error(message)
  }
  ```
- object: non-primitive type들을 통틀어서 나타냄

## Type Assertion
> Type assertions are a way to tell the compiler “trust me, I know what I’m doing.” 
> A type assertion is like a type cast in other languages, but performs no special checking or restructuring of data.

런타임에 영향을 미치지 않으며 컴파일타임에만 사용되고, 개발자가 필요한 검사들을 미리 수행했다고 생각한다.

```typescript
let someValue: any = "this is a string";

let strLength: number = (<string>someValue).length;
let strLength: number = (someValue as string).length;
```

음.. 컴파일러가 알아서 해주는게 참 좋다고 생각했지만, 당연히 개발자들이 너무 빡빡한 검사를 피하거나 런타임에 달라질 경우 mitigation이 있을 거라 생각한다.
왜냐면 결국 자바스크립트의 수퍼셋이니까.
하지만 이 기능을 많이 사용할 수록 타입스크립트로 부터 얻을 장점들이 퇴색되는 느낌이긴하다.

[여기](https://hyunseob.github.io/2017/12/12/typescript-type-inteference-and-type-assertion/)에 실제 환경에서 쓰일 법한 좋은 예시가 있다.


---
## Reference
- https://www.typescriptlang.org/v2/docs/handbook/basic-types.html
- https://hyunseob.github.io/2017/12/12/typescript-type-inteference-and-type-assertion/
