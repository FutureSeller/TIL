필연적으로 window 객체에 property를 추가해야하는 상황이 발생하게 되는데, 타입스크립트가 태클을 건다.

```typescript
window.myProperty = window.myProperty || "value";

// TS2339: Property 'myNewProperty' does not exist on type 'Window & typeof globalThis'.
```

window 인터페이스에는 해당 프로퍼티에 대한 정의가 없기 때문인데, 다양한 솔루션들이 있다.

## 1. 전역 타입을 확장하는 방법
```typescript
declare global {
  interface Window {
    myProperty: string;
  }
}
```

## 2. Dynamic 하게 사용하는 방법
```typescript
(<any> window).myProperty; 

(window as any).myProperty;

window['myProperty'];
```

## 3. Augmentation
``` typescript
export {};
declare global {
  interface Document {
    /** documentation on foo */
    foo: string;
  }
}
```

```typescript
document.foo; // successs without importing foo
```


## 4. interface merging
``` typescript
interface Window {
  foo: string;
}

window.foo = 'bar';
```

---
## Reference
- https://github.com/microsoft/TypeScript/issues/19816
