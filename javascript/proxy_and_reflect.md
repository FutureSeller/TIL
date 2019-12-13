# Proxy

- 객체를 감싸 기본적인 동작의 새로운 행동을 정의할 때 사용함 (속성 접근, 할당, 순회, 열거, 함수 호출 등)
- 작업을 중간에 가로채어 처리하기도하고, 원래 객체가 처리하도록 전달하기도 함
- 일반 객체와는 다른 행동 양상을 보이는 `exotic object` (특수 객체)임. 프로퍼티가 없음

### Syntax

```javascript
new Proxy(target, handler);
```

- `target`: 감싸게될 객체. 모든 객체 가능
- `handler`: 동작을 가로채는 `trap`이 담긴 객체
  - 새로운 행동을 정의함
  - 정의되어있지 않다면 행동을 객체로 전달하는 wrapper가 됨

#### Example: Without Trap

```javascript
let target = {};
let proxy = new Proxy(target, {});

proxy.test = 5;
console.log(target.test); // 5
console.log(proxy.test); // 5
```

### Trap

- 내부 메서드의 호출을 가로챔(https://tc39.es/ecma262/#sec-proxy-object-internal-methods-and-internal-slots)
- 트랩을 사용할 때, 명세된 몇 가지 규칙(invariant)을 반드시 따라야 한다고 함
  - 가능한 내부 메서드의 명세를 따르는 게 좋은 듯함 (반환 값 같은 것들)
  - 일관된 동작을 하도록 하기 위함
- 주의할 점: 일관성 유지를 위해 타깃 객체를 프락시로 감싼 이후에는 타깃 객체를 참조하는 코드가 없어야함
- [A complete traps list example; document.cookie](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Proxy#A_complete_traps_list_example_%EC%99%84%EB%B2%BD%ED%95%9C_traps_%EB%A6%AC%EC%8A%A4%ED%8A%B8_%EC%98%88%EC%A0%9C)

#### Example: With trap

```javascript
let user = {
  name: "John",
  _password: "***",
  checkPassword: function(value) {
    return this._password === value;
  }
};

user = new Proxy(user, {
  get(target, prop) {
    if (prop.startsWith("_")) {
      throw new Error("접근이 제한되어있습니다.");
    }
    let value = target[prop];
    return value; // (*)
    // (**) return (typeof value === "function" ) ? value.bind(target) : value
  }
});

user.checkPassword.toString(); // "function(value) { return this._password === value; }"
user.checkPassword("***"); // Uncaught Error: 접근이 제한되어있습니다.
```

- 왜 Uncaught Error?
  - `checkPassword` 메서드에서 값을 비교하기 위해 private 프로퍼티인 `this._password`에 접근하려면 `get` 트랩을 타기 때문임
  - `user.checkPassword()`를 호출하면 `this`가 프락시로 감싸진 wrapper이기 때문임
- 해결책: (\*\*)와 같이 `get` 트랩에서 메서드가 내부 private 프로퍼티에 접근할 경우, `bind`를 해주면 됨
- 바람직한 해결책은 아님: 한 마디로 요약하자면 동일한 동작 및 컨벤션을 유지하기가 힘들 수 or 어려울 수 있음
  - 메서드가 어딘가에서 프락시로 감싸지 않은 객체를 넘기게 되면 기존 객체와 프락시로 감싼 객체가 어디에 있는지 파악할 수 없음
  - 여러 번 프락시로 감쌀 경우, 객체에 가하는 수정이 다를 수 있어 의도치 않은 결과가 나타날 수 있음

### `Proxy.revocable(target, handler)`

> Revocable: 폐지[취소, 해제]할 수 있는, 무효화할 수 있는

- Summary. `trap`을 해제할 수 있는 프록시를 만듬
- `revoke()` 메서드가 호출되면..
  - 프록시는 더 이상 사용할 수 없고, 모든 internal 메서드들에 대한 참조를 지워버림
  - 즉, 어떤 동작을 하더라도 `TypeError`를 던짐
  - revoked로 남게 되고 `target` 객체는 조만간 GC의 타겟이 됨

#### Example

```javascript
const target = {};
const revocable = Proxy.revocable(target, {
  get: function(target, name) {
    return "[[" + name + "]]";
  }
});
const proxy = revocable.proxy;
console.log(proxy.foo); // "[[foo]]"

revocable.revoke();

console.log(proxy.foo); // TypeError is thrown
proxy.foo = 1; // TypeError again
delete proxy.foo; // still TypeError
typeof proxy; //
```

---

# Reflect

- 중간에서 가로챌 수 있는 자바스크립트 작업에 대한 메서드를 제공하는 내장 객체; 메서드의 종류는 프록시의 trap들과 동일함
- 프록시를 좀 간단하게 사용하는 것 처럼 보이기도 함

```javascript
// [[Set]]: obj[prop] = value;
// Reflect: Reflect.set(obj, prop, value)

let user = {};
Reflect.set(user, "name", "john");
console.log(user.name); // john
```

## Reference

- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Proxy
- https://ko.javascript.info/proxy
- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Reflect
- https://ko.javascript.info/proxy#ref-746
