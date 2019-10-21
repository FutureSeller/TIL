## Basic: Object.isExtensible
- 객체가 확장 가능한지(객체에 새 속성을 추가할 수 있는지 여부)를 결정
``` javascript
const object1 = {};

// default object: extensible
Object.isExtensible(object1) // true

// Object.preventExtensions: inextensible
Object.preventExtensions(object1)
Object.isExtensible(object1) // false

// Object.seal: inextensible
var sealed = Object.seal({})
Object.isExtensible(sealed) // false

// Object.freeze: inextensible
var frozen = Object.freeze({})
Object.isExtensible(frozen) // false

// in ES5
Object.isExtensible(1) // Type Error

// in ES6
Object.isExtensible(1) // === false
```

## Object.seal
- seal: 밀봉
- 현재 존재하는 모든 속성을 설정 불가능 상태로 만들어줌
  - data property <-- x --> accessor property
- 쓰기 가능한 속성의 값은 밀봉 후에도 변경 가능
- 밀봉한 후 속성의 추가/삭제나 속성 사이의 전환은 모두 (Implicit)Error
``` javascript
const object1 = {
  property1: 42
};

Object.seal(object1);

// change (O)
object1.property1 = 33;
console.log(object1.property1); // expected output: 33

// delete (X)
delete object1.property1; // cannot delete when sealed
console.log(object1.property1); // expected output: 33

// add (X)
object1.property2 = '1'
console.log(object1.property2); // expected output: undefined

// data prop -> accessor (X)
Object.defineProperty(object1, 'foo', { get: function() { return 'g'; } }); // TypeError
```

## Object.preventExtension
- 새로운 속성이 추가되는 것을 방지, `__proto__`의 확장 또한 막는다.
- `default`에서 `preventExtension`으로 만들순 있으나, 역은 불가능하다.

``` javascript
let obj = { 'a' : 1 };
Object.preventExtensions(obj);

// change (O)
obj['a']= 2;
console.log(obj); //{ a: 2 }

// remove (O)
delete obj['a']
console.log(obj); //{}

// add (X)
obj['b'] = 1;
console.log(obj); //{}
```

## Object.freeze
- freeze: 동결
- 속성 추가/제거 방지, 값이 변경되는 것도 방지
- accessor property 또한 동일함, 동결된 사본을 생성하지 않음
``` javascript
const obj = {
  prop: 42
};

var o = Object.freeze(obj);

o === obj // === true

// change (X)
obj.prop = 33; // Throws an error in strict mode
console.log(obj.prop); // expected output: 42

// add (X)
obj.prop2 = 42;
console.log(obj); // { prop: 42 }

// remove (X)
delete obj['prop'];
console.log(obj); // { prop: 42 }

```
- 얕은 동결
  - 직속 속성(바로 아래의 property)에만 적용됨
  - property에 object가 할당되어있다면 재귀적으로 동결해야함
``` javascript
var employee = {
  name: "Mayank",
  designation: "Developer",
  address: {
    street: "Rohini",
    city: "Delhi"
  }
};

Object.freeze(employee);

employee.name = "Dummy"; // 비엄격 모드에서 조용하게 실패
employee.address.city = "Noida"; // 자식 객체의 속성은 수정 가능

console.log(employee.address.city) // 출력: "Noida"
```

## freeze vs. seal vs. preventExtension

| Operation | default | preventExtension | seal | freeze |
| -      | - | - | - | - |
| add    | ✓ | - | - | - |
| remove | ✓ | ✓ | - | - |
| change | ✓ | ✓ | ✓ | - |

---
## Reference
- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/isExtensible
- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/seal
- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze
- https://til.cybertec-postgresql.com/post/2019-10-11-Object-preventExtension-vs-seal-vs-freeze
