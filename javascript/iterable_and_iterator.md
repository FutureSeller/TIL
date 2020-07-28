# Iterable(이터러블) 그리고 Iterator(이터레이터)

## Generally, Java | Python

- Iterable: 객체의 멤버를 반복할 수 있는 객체
- Iterator: 반복가능한 객체를 순회, 탐색하기위해 사용될 메소드 혹은 포인터를 제공하고 도움을 주는 상태를 관리하는 객체 혹은 추상화된 무언가
  - Java: `hasNext()`, `next()`, `forEachRemaining()`
  - Python: `next()`, `iter()`
- Iteratee: 반복마다 데이터 청크에 대한 결과를 연속, 순차적으로 계산할 수 있도록 하는 객체, 함수 혹은 추상화된 무언가

## 그렇다면 JavaScript 에서는?

> Iterable = Iterable Protocol 을 준수한 객체

#### Iterable Protocol
- `Symbol.iterator` 메소드를 구현하거나 프로토타입 체인에 의해 상속한 객체
- `Symbol.iterator` 는 Iterator를 반환해야함

```typescript
object[Symbol.iterator]: Function -> Iterator
```

- 객체가 반복되어야 한다면 `Symbol.iterator` 메소드가 인수없이 호출되고, 반환된 이터레이터는 반복을 통해 획득할 값을 얻을 때 사용됨
- `for..of`, spread, destructuring 등이 가능해짐
- 내장 이터러블: built-in object가 이미 `Symbol.iterator`를 정의한 객체
  - .e.g, String, Array, TypedArray, Map, Set, DOM Datastructure, Arguments

```javascript
const array = [1,2,3]
console.log(Symbol.iterator in array) // true

const iterator = array[Symbol.iterator]()
console.log(iterator.next())
console.log(iterator.next())
console.log(iterator.next())
console.log(iterator.next())
```

> Iterator = Iterator Protocol 을 준수하는 객체

#### Iterator Protocol
- `next()` 메서드를 가지고, 반복 시 수행될 시퀀스를 정의하고 종료 시 반환값을 정의
  - 시퀀스 정의: `next()` 메서드를 사용하여 반복
  - 반환 값: `{ done: boolean, value: any }` IteratorResult라고도 한다.
    - 반복 작업을 마쳤을 경우: `{ done : true }`
    - 반복 작업이 남아있을 경우: `{ done: false, value: any }`

#### 임의의 객체를 Iterable 하게 만드는 방법 === 임의의 객체를 Iterable Protocol을 따르도록 함
- `Symbol.iterator` 메소드를 구현 혹은 상속 받도록 함
- `Symbol.iterator`를 구현할 때, 이는 Iterator Protocol을 따라야함

```javascript
const object = {}
const counter =  (maxValue) => {
  let _accumulate = 0
  return () => ({
    next: () => {
      return _accumulate < maxValue
        ? { value: _accumulate++, done: false }
        : { value: undefined, done: true }
    }
  })
}

object[Symbol.iterator] = counter(10)

const iterator = object[Symbol.iterator]()
console.log(iterator.next())

// 혹은, for...of를 사용할 수 있다.
for(const value of object) {
  console.log(value)
}
```

#### 한 문장으로 정리하자면
- Iterable: `Symbol.iterator`가 Iterator를 반환하면 Iterable이다
- Iterator: `next` 메소드를 가지고 있고 이 메소드가 `{ value, done }` IteratorResult를 반환하면 Iterator이다

#### Iterable이면서 Iterator인 객체를 생성하는 함수
- 객체는 `next` 메서드를 가지고 있고, `Symbol.iterator`가 자기 자신을 반환하면 됨

```javascript
function Honjong(maxValue) {
  let _accumulate = 0
  return {
    [Symbol.iterator]() {
      return this
    },
    next() {
      return _accumulate < maxValue
        ? { value: _accumulate++, done: false }
        : { value: undefined, done: true }
    }
  }
}

const honjong = Honjong(10)
```

- 요런 걸 어디에 쓰나요? 실제 `array.entries()`에 쓰이고 있음
  - `Array.prototype.entries()`: 배열의 각 인덱스에 대한 키/값 쌍을 가지는 새로운 Array Iterator 객체를 반환
  - ~왜? 인지는 아직 잘 모르겠다...~

```javascript
const someArray = [1, 5, 7];
const someArrayEntries = someArray.entries();

someArrayEntries.toString(); // [object Array Iterator]
someArrayEntries[Symbol.iterator].toString(); // function [Symbol.iterator]() { [native code] }
someArrayEntries === someArrayEntries[Symbol.iterator](); // true
```

```javascript
// https://exploringjs.com/es6/ch_iteration.html#objectEntries
function objectEntries(obj) {
  let index = 0;

  // In ES6, you can use strings or symbols as property keys,
  // Reflect.ownKeys() retrieves both
  const propKeys = Reflect.ownKeys(obj);

  return {
    [Symbol.iterator]() {
      return this;
    },
    next() {
      if (index < propKeys.length) {
        const key = propKeys[index];
        index++;
        return { value: [key, obj[key]] };
      } else {
          return { done: true };
      }
    }
  };
}

```


## Appendix

#### Iteratee

> 반복마다 데이터 청크에 대한 결과를 연속, 순차적으로 계산할 수 있도록 하는 객체, 함수 혹은 추상화된 무언가

반복시키는 것을 순차적으로 다루는 방법으로 생각하면 쉬움. 사실 우리는 이미 쓰고 있었다.

```javascript
const array = [1,2,3]
const iteratee = v => Math.sqrt(v)
array.map(iteratee)
```

#### `Array.from`

이터러블이나 유사배열을 받아 `Array`로 만들어주는 메서드

```javascript
let arrayLike = {
  0: "hello",
  1: "world",
  length: 2
};

console.log(arrayLike.pop()); // TypeError: arrayLike.pop is not a function

let array = Array.from(arrayLike);
console.log(array.pop()); // world
```

---

## Reference

- https://ko.javascript.info/iterable
- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Iteration_protocols
- https://meetup.toast.com/posts/140
- https://www.educative.io/edpresso/iterable-vs-iterator
- https://www.cs.cornell.edu/courses/JavaAndDS/iteratorIterable/iterator.html
- https://poiemaweb.com/es6-iteration-for-of
- https://poiemaweb.com/js-array-higher-order-function
- https://exploringjs.com/es6/ch_iteration.html#objectEntries