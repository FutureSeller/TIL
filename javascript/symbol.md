# Symbol

Symbol을 썼을 때 장점은 이해가 되는데 현업에서 많이 쓸 까라는 생각을 하게 됨

## 목적
- 생성되면 변경되지 않음. 속성을 부여할 수 없음
- 반환되는 모든 심볼 값은 **고유함**. 
- 객체 프로퍼티에 대한 식별자로 사용 가능
- 서브파티에서 가지고 온 객체에 side effect를 주지 않고 객체를 식별하기 위해 쓰기도 함 (충돌하지 않기 때문)
  - `id` vs. `Symbol('id')`: 이미 id라는 property가 있어도 상관 없음
  - 디버깅하기 편할 것 같음

### 기본적인 사용
``` javascript
const id1 = Symbol('id')
const id2 = Symbol('id')

console.log(id1) // Symbol(id)
console.log(id1 == id2) // false
console.log(id1 === id2) // false
console.log(id1.description === id2.description) // true

typeof id1 // "symbol"

alert(id1) // TypeError: Cannot convert a Symbol value to a string

const test = new Symbol() // TypeError: Symbol is not a constructor
```

### 객체 리터럴 & 심볼
``` javascript
let id = Symbol('id')
let user = {
  name: 'FutureSeller',
  [id]: 1,
}
```

### 전역 심볼 레지스트리
``` javascript
const symbol1 = Symbol.for('foo')
const symbol2 = Symbol.for('foo')

console.log(symbol1 === symbol2) // true
console.log(Symbol.keyFor(symbol1)) // foo
```

### Usage: Private property access
``` javascript
const PASSWORD = Symbol('password')

class User {
  constructor(name, password) {
    this.name= name
    this[PASSWORD] = password
  }

  getPassword() { return this[PASSWORD] }
}

const user = new User('FutureSeller', 'JavaScript')
console.log(user['password']) // undefind
console.log(user[Symbol('password')]) // undefined
console.log(user[Symbol.for('password')]) // undefined
console.log(Object.getOwnPropertyNames(user)) // ["name"]
console.log(user.getPassword()) // JavaScript
console.log(user[PASSWORD]) // JavaScript

console.log(PASSWORD in user) // true
console.log(Object.getOwnPropertySymbols(user)) // [Symbol(password)]
```


### 시스템 심볼
- 자바스크립트 내부에서 사용되는 심볼

#### Symbol.match
- Symbol을 키로 갖는 value를 입력값과 비교하기 위해 `String.match`에 hook을 걸어준 것이라고 함

```javascript
const PASSWORD = Symbol('password')

class User {
  constructor(name, password) {
    this.name= name
    this[PASSWORD] = password
  }

  [Symbol.match](pwd) {    
    return this[PASSWORD] === pwd
  }
}

let user = new User('FutureSeller', 'JavaScript')
'JavaScript'.match(user) // true
```

#### Symbol.toPrimitive
- type conversion 시, 어떻게 동작할 지 명시해주는 것
- coersion 같은 것들을 통해 equality(==) 같은 걸 처리해주기도 함

```javascript
const LEN = Symbol('len')
class Password {
  constructor(pwd) {
    this[LEN] = pwd.length
  }
  [Symbol.toPrimitive](hint) {
    return '*'.repeat(this[LEN])
  }
}

let securePassword = new Password('password')
('' + securePassword) // '********'
```


- Symbol.hasInstance: `instanceof`를 처리할 수 있도록 함
- Symbol.iterator: user-defined iterable을 처리할 수 있도록함

---
## Reference
- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Symbol
- https://poiemaweb.com/es6-symbol
- https://ko.javascript.info/symbol
- http://hacks.mozilla.or.kr/2015/09/es6-in-depth-symbols