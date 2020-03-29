# Chatper 2. 값

## 배열

> 문자열, 숫자, 객체 심지어 다른 배열이나 어떤 타입의 값이라도 담을 수 있는 그릇

주의할 점은 `delete`를 통해 원소를 제거하더라도 `length`는 그대로 라는 것이다.

```javascript
const arrayObject = [1, 2, 3];
delete arrayObject[0];

arrayObject.length === 3;
arrayObject; // Chrome M80의 경우, [empty, 2, 3]
arrayObject[0]; // undefined
```

이럴 경우의 배열을 `sparse` 배열이라고 한다.

#### 배열의 인덱스

배열 인덱스는 숫자인데, 배열 자체도 하나의 객체여서 키/프로퍼티 문자열을 추가할 수 있다.
하지만 `length`가 증가하진 않는다.

주의할 점은 키로 넣은 문자열 값이 10진수로 타입이 바뀔 수 있다면, 문자열 키가 아닌 숫자 키를 사용한 것과 같은 결과를 초래한다.

```javascript
const arrayObject = [];
arrayObject["14"] = 10;

arrayObject.length === 15;
```

따라서, 배열을 사용할 경우엔 인덱스를 명시적으로 숫자만 사용하는 것을 권장한다.

#### 유사 배열 (Array-Like Object)

> 유사 배열은 숫자 인덱스가 있으며 `length` 프로퍼티를 가지는 객체를 의미한다.

~간혹가다~ 꽤나 자주 유사 배열을 배열의 `method`를 사용하여 제어하고 싶을 때가 생긴다.
예를 들면, DOM 쿼리로 가져온 노드들이 유사 배열로 넘어왔을 때 `reduce`나 `map` 같은 작업을 하고 싶을 때가 있다.

```javascript
// 과거에는 다음과 같이 사용했었고
Array.prototype.slice.call(arguments);

// 요즘에는 아래와 같이 사용한다
Array.from(arguments);
```

## 문자열

> 흔히 문자의 배열이라고 생각한다.

```javascript
const a = "foo";
const b = ["f", "o", "o"];

a.length === b.length;

a.indexOf("o") === 1;
b.indexOf("o") === 1;

const c = a.concat("bar"); // 'foobar'
const d = b.concat(["b", "a", "r"]); // 'foobar'.split()
```

> 하지만 생김새만 비슷할 뿐 문자 배열과 같지 않다.

```javascript
a[1] = "0";
b[1] = "0";

a; // 'foo'
b; // ['f', '0', 'o']
```

문자열은 불변 값(Immutable)이지만 배열은 가변 값(Mutable)이기 때문이다.
따라서, 문자열 메서드는 그 내용을 바로 변경하지 않고 **항상 새로운 문자열을 생성한 후 반환**한다.

```javascript
const a = "foo";
const c = a.toUppserCase();

a === c; // false
```

문자열을 다룰 때 유용한 대부분의 배열 메서드는 사실상 문자열에 쓸 수 없지만, 문자열에 대해 불변 배열 메서드를 빌려 쓸 수는 있다.

```javascript
const a = "foo";
a.join; // undefined

Array.prototype.join.call(a, "-"); // 'f-o-o'
```

하지만, 가변 메서드는 빌려 쓸 수 없다.

```javascript
Array.prototype.reverse.call(a); // 'foo' 라고 책에 나와있지만 지금은 조금 다르다.

/*
VM1924:1 Uncaught TypeError: Cannot assign to read only property '0' of object '[object String]'
    at String.reverse (<anonymous>)
    at <anonymous>:1:25
*/
```

엔진의 내부 동작이 약간 변경된 것 같다. ~예전에는 봐줬던 걸 지금은 단호하게 거절하는 것 같다.~
`string`의 경우 Immutable이기 때문에 `read-only`여서 과거에는 문자열 객체를 반환했는데 지금은 에러를 뱉어준다.

정말 해당기능을 쓰고 싶을 때는 문자열을 배열로, 배열을 문자열로 되돌리는 Hack이 존재한다.

```javascript
const a = "foo";
const b = a
  .split("")
  .reverse()
  .join(""); // 'oof'
```

## 숫자

> `number`가 유일하며 정수, 부동 소숫점 숫자를 모두 포함한다.

자바스크립트도 IEEE 754 표준을 따르며, 그중에서도 정확히 Double Precision(64bit)을 사용한다.

너무 크거나 아주 작은 숫자는 지수형(Exponent Form)으로 표기하며 `toExponential()` 메서드의 결괏값과 같다.

```javascript
const a = 5e10;
a; // 50000000000
a.toExponential(); // 5e+10
```

#### `Number.prototype`

숫자 값은 `Number` 객체의 래퍼로 박싱할 수 있기 때문에 `Number.prototype` 메서드로 접근 가능하다.
이 책을 읽다가 약간 오묘한 것들을 짚어보고자 한다.

```javascript
42.toFixed(3); // SyntaxError
42..toFixed(3); // 42.000
(42).toFixed(3); // 42.000
42 .toFixed(3); // 42.000
```

`42.`가 리터럴로 맞는 표현식이기때문에 파싱에러가 나는 것이기 때문이다. (참 오묘하다.)
심지어 `42` 뒤에 공백이 있었을 때 숫자를 `42`로 파싱하곤한다. (Lexer의 규칙을 보니 그러하다.)
하지만, 이런 패턴의 코드는 굳이 말하지 않아도 작성하지 않을 것이라 생각한다.

#### 진법

같은 숫자를 다양한 진법으로 나타낼 수 있는데, 표기법이 참 오묘하다.

```javascript
0xf3; // 243의 16진수

0363; // 8진법, 10진법으로 나타냈을 때 243
00363; // 8진법, 10진법으로 나타냈을 때 243
0o363; // 8진법, 10진법으로 나타냈을 때 243

0b11110011; // 243의 이진수
0b11110011; // 243의 이진수
```

`0363` 혹은 `00363`보다는 `0o363`이 명시적이고 이진수의 경우 소문자가 보기 편한 것 같지만 나름대로의 컨벤션을 잘 적용하길 바란다.

#### 작은 소수 값

부동 소수점 숫자의 문제 때문에 아주 가끔 어려움을 겪을 수 있다.

```javascript
0.1 + 0.2 === 0.3; // false, 0.30000000000000004
```

내 개인적인 생각이지만 보편적으로 자바스크립트를 쓸 때, 소수점 아랫 자리때문에 문제될 일은 거의 없을거라 생각한다.

하지만 코인 거래소라던지, 금전적인 문제가 끼어있을 땐 문제가 달라진다.

이 때 주로 사용되는 방법은 `Machine Epsilon`을 정하는 방법인데, 이는 컴퓨터가 이해할 수 있는 가장 작은 숫자단위를 의미한다.
즉, 어느 정도의 오차 범위 내에 있으면 같은 값이라고 서로 약속하는 것이다.

```javascript
if (!Number.EPSILON) {
  Number.EPSILON = Math.pow(2, -52);
}
```

부동 소수점 숫자의 최댓 값은 대략 1.798e+308 (ㄷㄷ..), 최솟 값은 5e-324 (ㄷㄷ...)이다.
이들은 각각 `Number.MAX_VALUE`, `Number.MIN_VALUE`로 정의한다.

#### 안전한 정수 범위

`Number.MIN_VALUE ~ Number.MAX_VALUE` 숫자는 사실 인간이 사용하기 너무 작고 큰 값이다.
따라서, 보편적으로 사용할 훨씬 작은 범위의 _안전 값_ 범위가 정해져있다.

이 값은 `Number.MAX_SAFE_INTEGER` 그리고 `Number.MIN_SAFE_INTEGER`라고 정의한다.

## 특수 값

#### null vs. undefined

[여기](./null_vs_undefined.md)를 참고한다.

#### NaN

> Not A Number; 숫자가 아니다.

책에서는 더 정확한 표현으로 유효하지 않은 숫자, 실패한 숫자, 몹쓸 숫자로 하는게 좀 더 정확하다고 한다.

NaN은 경계 값(Sentinel Value)의 일종으로 숫자 집합 내에서 특별한 종류의 에러상황을 나타낸다.
흔히 할 수 있는 실수는 다음과 같다.

```javascript
NaN === NaN; // false
```

왜냐하면 NaN은 반사성이 없는 유일무이한 값이기 때문이다. 비교는 아래와 같이 수행한다.

```javascript
isNaN(NaN); // true
isNaN(1); // false
isNaN("foo"); // true ????????
```

`isNaN`은 치명적인 결함이 있다. 말그대로 숫자가 아닌 것만 검사해서 `foo`가 문자열이기 때문에 `true`가 된다.
이를 방지하기 위해 `Number.isNaN`이 추가적으로 생겼다.

#### 무한대

`Number.POSITIVE_INFINITY` 그리고 `Number.NEGATIVE_INFINITY`가 존재한다.

```javascript
const a = Number.MAX_VALUE;
a + a; // 무한대
a + Math.pow(2, 970); // 무한대
a + Math.pow(2, 969); // 무한대가 아닌 어떤 숫자
```

IEEE 754 명세에 따르면, 덧셈 등의 연산 결과가 너무 커서 표현하기 곤란할 때 가장 가까운 수로 반올림한다.
`Number.MAX_VALUE + Math.pow(2, 969)`는 무한대보다는 `Number.MAX_VALUE`에 가깝다고한다.

그리고... 무한대 / 무한대의 결과 값은 **정의되지 않은 연산**이므로 `NaN`이다.

#### 영(0)

자바스크립트에는 +0과 -0이 존재한다. -0은 곱셈, 나눗셈으로부터만 나오고, 덧셈 뺄셈에는 나오지 않는다.
하지만 이를 stringify하면 값은 항상 `'0'` 이다.

```javascript
const a = 0 / -3; // -0
const b = 0 * -3; // -0
a.toString(); // '0'
```

이를 구분하기 위해서 아래와 같은 함수가 있을 수 있다.

```javascript
function isNegZero(n) {
  n = Number(n);
  return n === 0 && 1 / n === -Infinity;
}
```

이쯤 되면 도대체 이걸 왜 만들었을 까? 라는 생각이 든다.

대충 추측해보자면 덧셈과 뺄셈에서는 안된다고 하고, 곱셈과 나눗셈에서 존재한다고하니
어떤 값의 변화율에 따라 동작이 달라져야하는 일이 필요했던 것 같다.

책을 읽어보니 값의 크기로 어떤 정보(애니메이션 프레임당 넘김 속도)와 그 값의 부호로 또 다른 정보(넘김 방향)을 동시에 나타내야하는 애플리케이션이 있기 때문이다.

~예를 들면 속력이 아니라 속도에 따라 뭔가를 반영해야 하는 애플리케이션이 있나보다.~

## 동등 비교

ES6 부터 잡다한 예외를 걱정하지 않아도 두 값이 절대적으로 동등한지를 확인하는 새로운 유틸리티인 `Object.is()`를 지원한다.

```javascript
const a = 2 / "foo";
const b = -3 * 0;

Object.is(a, NaN); // true
Object.is(b, -0); // true
Object.is(b, 0); // false
```

폴리필은 다음과 같다.

```javascript
if (!Object.is) {
  Object.is = function(v1, v2) {
    // -0
    if (v1 === 0 && v2 === 0) {
      return 1 / v1 === 1 / v2;
    }

    // NaN
    if (v1 !== v1) {
      return v2 !== v2;
    }

    // 기타
    return v1 === v2;
  };
}
```

될 수있으면 `===`을 사용하도록 하고, 이런 특이한 동등비교는 지양하는 것이 좋다.

## 값 vs 레퍼런스

> 자바스크립트에서 레퍼런스는 (공유된) 값을 가리키므로 서로 다른 10개의 레퍼런스가 있다면 이들은 항상 공유된 단일 값을 개별적으로 참조한다. (서로에 대한 레퍼런스/포인터같은 건 없다.)

> 값 또는 레퍼런스의 할당 및 전달을 제어하는 구문 암시가 전혀 없고, 값의 타임만으로 값-복사, 레퍼런스-복사 둘 중 한쪽이 결정된다.

Primitive 값은 항상 Immutable하므로 값-복사 방식으로 할당/전달된다.
하지만 객체나 함수 등 합성 값(Computed Values)은 할당/전달 시 레퍼런스 사본을 생성한다.

```javascript
var a = 2;
// 값을 복사한다. 왜냐면 Immutable 이니까
var b = a;

b++;
a; // 2
b; // 3

var c = [1, 2, 3, 4];
// 공유된 [1,2,3,4] 값의 레퍼런스이다. c와 d가 [1,2,3,4]를 소유하는 겂이 아닌 동등하게 참조하는 것이다.
var d = c;
d.push(5);
c; // [1,2,3,4,5]
d; // [1,2,3,4,5]
```

함수 인자를 예시로 들어보자.

```javascript
function foo(x) {
  x.push(4); // [1,2,3,4]

  x = [4, 5, 6];
  x.push(7); // [4,5,6,7]
}

var a = [1, 2, 3];
foo(a);

a; // [1,2,3,4]
```

1\. a를 인자로 넘기면 레퍼런스 사본이 x에 할당되고, x와 a는 동일한 `[1,2,3]`값을 가리킨다.

2\. `push`연산 이후, x에 새 값을 할당 해도 a가 가리키던 값에는 아무런 영향이 없다.

3\. 즉, x가 a가 가리키는 값을 바꿀 도리는 없고, 같은 값을 공유할 때 공유값의 내용만 바꿀 수 있다.

아래와 같이 x에 새로운 값을 가키지 않고 공유값을 바꿔버리면 다음과 같은 결과가 나온다.

```javascript
function foo(x) {
  x.push(4); // [1,2,3,4]

  x.length = 0;
  x.push(4, 5, 6, 7);
}

var a = [1, 2, 3];
foo(a);

a; // [4,5,6,7]
```

명시적으로 side-effect를 없애기 위해서 `foo(a.slice())`와 같이 새로운 사본을 만들어 인자로 넘기곤한다.

반대로 스칼라 원시값을 레퍼런스 처럼 바뀐 값이 바로바로 반영되도록 넘기려면 원시 값을 다른 합성 값으로 감싸야한다.

```javascript
function foo(wrapper) {
  wrapper.a = 42;
}

const obj = { a: 2 };
foo(obj);
obj; // {a: 42}
```

아래와 같은 경우는 어떨까?

```javascript
function foo(x) {
  x = x + 1;
}

var a = 2;
var b = new Number(a);

foo(b);
a; // 2
b; // 2
```

1\. `x + 1`에서 x가 사용될 때, 자동으로 언박싱 된다.

2\. `x = x + 1`의 x는 공유된 레퍼런스에서 `Number`객체로 뒤바뀐다.

3\. x는 2 + 1 덧셈 결과인 스칼라 원시 값 3을 갖게 된다.

4\. b는 원시 값 2를 씌운, 변경되지 않은 원본 `Number` 객체를 참조한다.

이런 동작을 하게 할 거면 차라리 Immutable한 녀석을 새로 반환하거나 합성 값(object)으로 감싸서 프로퍼티를 변경하는게 속편할 것 같다.
