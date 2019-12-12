# Iterable(이터러블) 그리고 Iterator(이터레이터)

#### 이터러블 === 반복가능한 객체

- Symbol.iterator를 key로 가지고 있는 객체. 해당 key의 함수를 실행할 경우 **이터레이터**를 반환함
  - `obj[Symbol.iterator]: Function => Iterator`
- 배열을 일반화한 객체; 어떤 객체에든 `for..of` 반복문을 적용할 수 있음
- @@iterator 메소드를 구현해야함 === Symbol.iterator 프로퍼티를 가져야함
  - built-in object 중 이미 정의되어있거나 (내장 이터러블이라고 하며, Array, Map, String, TypedArray, Set)
  - 없다면 JavaScript 객체를 순회하는 방법을 customize 할 수 있도록 해줌
- 객체가 반복되어야 한다면 @@iterator 메소드가 인수없이 호출되고, 반환된 이터레이터는 반복을 통해 획득할 값들을 얻을 때 사용됨

#### 이터레이터

- Summary. `next()` 메소드를 가지고 있고, 그 메소드가 `{ done: boolean, value: any }`을 반환하도록 구현된 객체
- 반복시 수행될 시퀀스를 정의하고 종료 시 반환값을 정의
  - 시퀀스 정의: `next` 메서드의 control flow
  - 반환 값: `{ done: boolean, value: any }` IteratorResult라고도 한다.
    - 반복 작업을 마쳤을 경우: `{done : true}`
    - 반복 작업이 남아있을 경우: `{done: false, value: any}`
- 몇몇 이터레이터들은 이터러블이다. 아래의 예시를 보자

```javascript
const someArray = [1, 5, 7];
const someArrayEntries = someArray.entries();

someArrayEntries.toString(); // [object Array Iterator]
someArrayEntries[Symbol.iterator].toString(); // function [Symbol.iterator]() { [native code] }
someArrayEntries === someArrayEntries[Symbol.iterator](); // true

// 다음과 같이 개발되어있을거라 짐작됨
const range = {
  values: [1, 5, 7],
  from: 0,
  to: 3,

  [Symbol.iterator]: function() {
    this.current = this.from;
    return this;
  },

  next: function() {
    if (this.current < this.to) {
      return { done: false, value: this.values[this.current++] };
    } else {
      return { done: true };
    }
  }
};

range === range[Symbol.iterator](); // true
for (let value of range) {
  console.log(value); // 1,5,7
}
```

## Appendix

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
