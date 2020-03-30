# Chapter3. 네이티브

> 특정 환경에 종속되지 않은, ECMAScript 명세의 내장 객체를 말함

- String()
- Number()
- Boolean()
- Array()
- Object()
- Function()
- RegExp()
- Date()
- Error()
- Symbol()

```javascript
const s = new String("Hello World");
s.toString(); // 'Hello World'

typeof s; // 'object'
s instance of String; // true
Object.prototype.toString.call(a); // [object String]
```

생성자의 결과는 원시값을 감싼 객체 래퍼이며, object의 하위 타입에 가깝다.

```javascript
/*
Browser: Chrome M80

String { 'Hello World' }
0: 'H'
...
length: 11
[[PrimitiveValue]]: 'Hello World'
*/
console.log(s);
```

해당 결과는 브라우저마다 어떻게 객체를 직렬화하여 보여주는 지 상이하다.

## 내부 `[[Class]]`

`typeof`가 `object`인 값에는 `[[Class]]`라는 내부 프로퍼티가 추가로 붙는다.
대부분 해당 값과 관련된 네이티브 생성자를 가리키고, 원시 값의 경우 박싱과정을 거친다.

```javascript
Object.prototype.toString.call([1, 2, 3]); // [object Array]
Object.prototype.toString.call(/regex/i); // [object RegExp]

Object.prototype.toString.call(null); // [object Null]
Object.prototype.toString.call(undefined); // [object Undefined]

Object.prototype.toString.call(42); // [object Number]
Object.prototype.toString.call("42"); // [object String]
```

## 래퍼 [언]박싱하기

> 객체 레퍼는 아주 중요한 용도로 쓰인다.

```javascript
const s = "abc";

s.length; // 3
s.toUpperCase(); // 'ABC'
```

원시 값엔 프로퍼티나 메서드가 없기 때문에 `length`와 같은 프로퍼티에 접근하려면 래퍼를 사용한 박싱이 필요하다.
하지만, 자바스크립트 엔진이 **알아서 암시적으로** 박싱해주기 때문에 개발자들이 직접 박싱할 필요가 없다.

```javascript
const flag = new Boolean(false);
if (!flag) {
  console.log("UNREACHABLE");
}
```

`false`를 래퍼로 감쌌지만 객체 자체가 truthy하기 때문에 if의 조건을 통과하지 못하는 실수를 할 수 있다.
따라서, 직접 박싱하는 것은 되도록 지양하며 그렇게 해야할 경우에만 사용한다. (언젠지는 사실 잘 떠오르진 않는다. ~무의식에 쓰고 있을 수도~)

객체 래퍼의 원시 값은 `valueOf()` 메서드로 (명시적으로) 추출할 수 있다.

```javascript
const a = new String("asdf");
const b = new Number(42);

a.valueOf(); // 'asdf'
b.valueOf(); // 42
```

## 네이티브: 생성자

#### Array

(주의) 확실히 반드시 필요해서 쓰는 게 아니라면 생성자는 가급적 쓰지 않는 것이 좋다.

```javascript
// 일반적인 배열 생성 방법
const a = new Array(1, 2, 3); // [1,2,3]
const b = [1, 2, 3]; // [1,2,3]

// 주의 해야 할 것: 배열의 크기가 인자로 들어감
const c = new Array(3); // [empty x 3]

const d = [];
d.length = 3; // [empty x 3]

const e = [undefined, undefined, undefined]; // [undefined, undefined, undefined]
```

직접 undefined를 할당하지 않는 이상, 브라우저는 직렬화 결과를 보여줄 때 empty로 보여준다.
실제 값은 undefined가 들어있긴 하다.

#### Object, Function, and RegExp

> new Object()는 사실상 사용할 일이 없고, 리터럴 형태로 사용하는 것이 좋다.

> Function 생성자는 인자나 내용을 동적으로 정의해하하는 매우 드문 경우에 사용. 하지만 거의 쓸 일이 없다.

> 정규표현식은 리터럴 형식으로 정의할 것을 권장한다. (자바스크립트 엔진이 실행 전, 미리 컴파일후 캐시하기 때문에 성능상 이점이 있다.)

#### Date, Error and Symbol

Date, Error는 리터럴 형식이 없어 다른 네이티브에 비해 유용하기 때문에 적절히 레퍼런스를 보면서 사용하면 된다.

Symbol은 새로운 원시 값 타입이고 충돌 염려 없이 객체 프로퍼티로 사용 가능한 유일 값이다.
이것 또한 빈번하게 사용되진 않는 듯하고 레퍼런스를 참고하면 좋을 것 같다.
