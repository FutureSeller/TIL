# Prototype

- 프로토타입 객체 === 프로토타입
- 다른 객체의 원형이 되는 객체
- 객체 원형인 프로토타입을 이용하여 새로운 객체를 만들어 냄
- 객체는 생성된 각각의 객체에 공유 프로퍼티를 제공하기 위해 사용됨

### [[Prototype]]

- 각각 객체가 가지는 private 속성 (internal slot)
- `null` 혹은 자신의 프로토타입이 되는 다른 객체를 가리킴
- 객체를 생성할 때, 결정되며 다른 임의의 객체로 변경할 수 있음
- 될 수 있으면 Prototype 변경을 하지 말라고 함. 왜?
  - [[Prototype]]은 일반적으로 생성시점에만 만들고, 이후엔 수정하지 않음
  - 자바스크립트 엔진은 이를 토대로 최적화 되어있음

```javascript
function Person(name) {
  this.name = name;
}

const foo = new Person("Lee");

console.dir(Person); // prototype 있음
console.dir(foo); // prototype 없음
```

#### `__proto__`

- 객체의 Accessor Property; 즉, [[Prototype]]용 getter/setter
- 모든 객체가 가지고 있음
- `Object.create`, `Object.getProrotypeOf`, `Object.setProrotypeOf`를 사용하는 게 좋다고 함

```javascript
console.log(Person.__proto__ === Funciton.prototype);
```

#### `prototype`

함수 객체만 가지고 있는 property; 함수 객체가 생성자로 사용될 때, 프로토타입을 가리킴

```javascript
// 생성 시점에, foo.[[Prototype]] = Person.prototype
console.log(Person.prototype === foo.prototype);
```

#### `constructor`

객체 자신을 생성한 객체를 가리킴

```javascript
console.log(Person.prototype.constructor === Person);
console.log(foo.constructor === Person);
console.log(Person.constructor === Function);
```

### 프로토타입 체인

객체의 프로퍼티나 메소드에 접근하려고 할 때, 접근하고자하는 것이 없다면 [[Prototype]]이 가리키는 링크를 따라 자신의 프로토타입 객체를 차례대로 검색함

```javascript
const student = {
  name: "Lee",
  score: 90
};
console.log(student.hasOwnProperty("name")); // true
console.log(student.__proto__ === Object.prototype); // true
```

#### TMI: for..in, `Object.keys`, `Object.values`

- 프로토타입 체인을 타고 `enumerable`한 것만 traverse
- key-value를 순회하는 메서드들은 대부분 상속 프로퍼티를 제외하고 동작함

```javascript
const animal = {
  eats: true
}

const rabbit = {
  jumps: true
  __proto__: animal
}

console.log(Object.keys(rabbit)) // jumps
for(const prop in rabbit) {
  const isOwn = rabbit.hasOwnProperty(prop)
  if (isOwn) {
    console.log(prop) // jumps
  } else {
    console.log(prop) // eats
  }
}
```

### Convention: 네이티브 프로토타입

- 개발자에 의해 변경 될 수 있음. 전체에 영향을 미쳐 충돌을 일으킬 수 있음
- `Polyfill`을 위해 네이티브 프로토타입 변경을 허용

```javascript
if(!String.prototype.repeat) { ... }
console.log('JS'.repeat(4)) // JSJSJSJS
```

---

## Reference

- https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain
- http://www.nextree.co.kr/p7323
- https://ko.javascript.info/prototype-inheritance
- https://poiemaweb.com/js-prototype
