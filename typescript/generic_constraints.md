# Generic Constraints

제너릭한 것들 중에 몇몇 특정 타입(프로퍼티나 메소드)이 포함되어야하는 제약을 걸 때 사용

아래 예시에서는 length를 포함하게 하고 싶어함

```typescript
function loggingIdentity<T>(arg: T): T {
  console.log(arg.length); // Error: T doesn't have .length
  return arg;
}

interface Lengthwise {
  length: number;
}

function loggingIdentity<T extends Lengthwise>(arg: T) {
  ...
}
```

## Using Type Parameters in Generic Constraints

다른 파라미터로 제한되는 파라미터를 선언할 경우

```typescript
function getProperty<T, K extends keyof T>(obj: T, key: K) {
  return obj[key];
}
```
