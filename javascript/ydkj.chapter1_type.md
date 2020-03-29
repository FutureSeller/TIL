# Chatper 1. 타입

> 자바스크립트 엔진/개발자 모두에게 어떤 값을 다른 값과 분별할 수 있는, 고유한 내부 특성의 집합

## 내장 타입

- null
- undefined
- boolean
- number
- string
- symbol
- object

## `typeof` 연산자를 통한 타입 확인 및 검사

```javascript
typeof undefined === "undefined";
typeof true === "boolean";
typeof 42 === "number";
typeof "42" === "string";
typeof { foo: 42 } === "object";
typeof Symbol() === "symbol";
typeof null === "object";

// null은 object이기 때문에 명확히 비교하려면 아래와 같아야 한다.
const nullObject = null;
!nullObject && typeof nullObject === "object";
```

위의 경우를 제외하고 `typeof`가 반환하는 문자열이 하나 더 있다.

```javascript
typeof function a() {} === "function";
```

명세를 읽어보면 실제로 `object`의 하위 타입이며, 구체적으로 명시하면 *Callable Object*이다.
이는 내부 프로퍼티 `[[Call]]`로 호출할 수 있는 객체를 의미한다.

많이 쓰이는 배열의 경우도 `object` 타입이다.
즉, 배열 또한 숫자 인덱스와 `length` 프로퍼티가 자동으로 관리되는 등의 추가 특성을 지는 `object`의 하위 타입이다.

```javascript
typeof [1, 2, 3] === "object";

// Array인지 검사하려면 아래와 같은 방법을 쓰면 된다.
Array.isArray([1, 2, 3]) === true;
```

> 변수에 typeof 연산자를 대어보는 것은 엄밀히 말하면 변수의 타입이라기보다는 변수에 들어있는 값의 타입이 무엇인지를 묻는 것이다.

## 값이 없는 혹은 선언되지 않은

> `undefined`는 접근 가능한 스코프에 변수가 선언되었으나 아무런 값도 할당되지 않은 상태

> `undeclared`는 접근 가능한 스코프에 변수 자체가 선언조차 되지 않은 상태

## 선언되지 않은 변수

존재하지 않는 기능 추가를 위해 폴리필을 정의한다고 한다고 가정하고, 이미 선언되었는 지 존재 여부를 체크한다고 하자.

#### `typeof` 가드를 통한 체크

```javascript
if (typeof atob === "undefined") {
  atob = function() {};
}
```

이 때, `atob` 앞에 `var` 키워드의 유무에 따라 미묘하게 다른 동작을 할 가능성도 있다.
`if`문 블록에 `var`키워드가 있다면 코드 실행을 하지 않더라도 호이스팅 되기 때문에 원하는 동작과 상이하게 동작 할 수 있다.

#### 전역객체의 프로퍼티로써 변수를 검사하는 방법

```javascript
if (window.atob) {
  //...
}
```

요즘에는 다중 자바스크립트 환경 (node.js)와 같이 `window`가 전역객체가 아닐 수도 있다.
