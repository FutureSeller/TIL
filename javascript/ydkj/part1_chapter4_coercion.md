# Chapter4. 강제변환

## 값 변환
> 어떤 값을 다른 타입의 값으로 바꾸는 과정이 명시적이면 타입 캐스팅(Type Casting) 암시적이면 강제변환(Coercion)이라고 한다.

> 이 책에서는 명시적 강제변환(Explicit Coercion)과 암시적 강제변환(Implicit Coercion) 두 가지로 구분한다.

```javascript
var a = 42;
var b = a + ''; // 암시적 강제변환: 부수 효과(Side Effect)로부터 발생함
var c = String(a); // 명시적 강제변환: 코드만 봐도 의도적으로 타입변환을 일으킴
```

## 추상 연산 (Abstract Operation)

#### `ToString`
> 문자열이 아닌 값을 문자열로 변환하는 작업을 담당하는 로직

- 원시 값: 본연의 문자열화 방법이 정해져 있음 (null > null, undefined > undefined ...)
- 숫자: 문자열로 바뀌거나 지수형태로 바뀜
- 일반 객체: 특별히 지정하지 않으면 기본적으로 `Object.prototype.toString`에 있는 메서드가 내부 `[[Class]]`를 반환 (`[object Object]`)
- `toString` 메서드를 가진 객체: 자동으로 기본 호출 됨

#### `JSON.stringify()`

> JSON 안전 값(JSON-Safe Value: JSON 표현형으로 확실히 나타낼 수 있는 값)은 모두 문자열화 할 수 있음

인자가 undefined, 함수, 심벌 값이면 자동으로 누락시키며 배열에 포함되어 있으면 null로 바꾸며, 객체 프로퍼티에 있으면 지워버림

```javascript
JSON.stringify(undefined) // undefined
JSON.stringify(function() {}) // undefined

JSON.stringify([1, undefined, function(){}, 4]) // [1, null, null, 4]

JSON.stringify({ a: 2, b: function() {} }) // { a: 2 }
```

환형 참조 객체를 넘기면 에러가 나고, 객체 자체에 `toJSON()`이 정의 되어 있으면 이를 먼저 호출함.
따라서, 부적절한 값이나 직렬화하기 곤란한 객체를 문자열화 하려면 이를 재정의해야함.

> `toJSON()`은 적절히 평범한 실제 값을 반환하고 문자열화 처리는 `JSON.stringify()`가 담당함

다시 말해 `toJSON()`의 역할은 **문자열화 하기 적당한 JSON 안전 값으로 바꾸는 것**이지 JSON 문자열로 바꾸는 것이 아님

```javascript
const a = {
  val: [1,2,3],
  toJSON: function() { return this.val.slice(1) }
}

const b = {
  val: [1,2,3],
  toJSON: function() { return '[' + this.val.slice(1).join() + ']' }
}

JSON.stringify(a) // [2,3]
JSON.stringify(b) // '[2,3]'
```

`JSON.stringify()`의 두 번재 인자인 대체자(Replacer)를 지정하면 재귀적으로 직렬화 하면서 필터링 함

```javascript
const a = {
  b: 42,
  c: '42',
  d: [1,2,3]
}

JSON.stringify(a, ['b', 'c']) // { b: 42, c: 42 }
JSON.stringify(a, function(k, v) { if (k !== 'c') return v }) // {b: 42, d: [1,2,3] }
```

정리하자면 `JSON.stringify()`는 아래와 같이 강제변환을 한다.

1\. 문자열, 숫자, 불리언, null 값은 `toString` 규칙에 따라 강제변환됨

2\. `toJSON()`을 갖고 있다면, 문자열화 전 이를 자동으로 호출하여 JSON 안전 값으로 강제변환됨

## 명시적 강제변환
~이 장은 몰랐었던 것 위주로만 기록을 남기도록 하자~

#### 날짜 > 숫자
> `+` 단항 연산자를 해당 용도로 쓰곤 하고, 결과 값은 유닉스 타임스탬프 표현형으로 강제변환됨

```javascript
const d = new Date() // Sun Apr 05 2020 01:31:59 GMT+0900 (대한민국 표준시)
+d // 1586017919883
```

사실 위의 방법보다는 아래의 방법이 **매우 명시적**이여서 권장함

```javascript
// Date 객체의 timestamp를 얻을 때 권장
const timestamp = new Date().getTime() // 1586017919883

// 현재 타임스탬프를 얻을 때 권장
const timestamp = Date().now()
```

#### 이상한 나라의 틸드(~)
> `~` 연산자는 먼저 32비트 숫자로 강제변환한 후 NOT 연산을 한다.

자바스크립트 비트 연산자는 오직 32비트 연산만 가능하다. 즉, 비트 연산을 하면 피연산자는 32비트 값으로 강제로 맞춰지는데, 
`ToInt32`가 이 역할을 담당한다.

엄밀히 얘기하면 틸드는 2의 보수를 구한다.
```javascript
~42; // -(42+1) ==> -43
```

뒤의 예제들과 글을 읽어봤을 때, 이해는 되는데 개인적으로 Readability가 떨어지는 것 같다. 예시를 보자.

```javascript
const a = 'Hello World'

// 우리는 보통 이렇게 쓴다.
if (a.indexOf('lo') > -1) {
}

// 책에서 주장하는 바는 왜 틸드가 쓸모 있는지를 보여주고자한다.
if (~a.indexOf('lo')) {
}
```

자바스크립트에서 `-1`과 같은 성질의 값을 흔히 경계 값(Sentinel Value)라고 한다.
예를 들면, 위와 같이 배열에 존재하지 않는 인덱스면 -1을 반환하는 식이다.

이를 틸드로 먹이면 falsy한 0이 나오고, -1을 제외한 나머지는 truthy한 값이 나오기 때문에 책에서는
예제에서 위의 방식이 자바스크립트 엔진의 내부 구현 방식을 내 코드에 반영한다고 하고 있다.
하지만 개인적으로는 내부 구현 방식을 그대로 드러내는게 더 읽기 좋고 의도한 바가 잘 나타난다고 생각한다.

> 숫자의 소수점 이상 부분을 잘라내기 위해 더블 틸드(`~~`)를 사용하는 경우가 있다. (Wow....)

```javascript
~~3.141592 // 3
~~-3.141592 // -3

// 하지만 나는 이 경우에도 아래의 연산을 더 선호한다.
Math.trunc(3.141592) // 3
```

#### 숫자 형태의 문자열 파싱
> 문자열로부터 숫자 값의 파싱은 비 숫자형 문자(Non-Numeric Character)를 허용함

위의 말이 무엇이냐면, 좌 > 우 방향으로 파싱하다가 숫자같지 않은 문자를 만나면 멈추는 것을 의미함.
~이 부분은 사실 전혀 몰랐다.~

```javascript
Number('42px') // NaN
parseInt('42px') // 42
```

`parseInt`는 애초에 문자열에 쓰는 함수이므로, 문자열화를 먼저 진행 한 뒤 숫자로 변환함.
따라서, 반드시 **문자열**만을 인자 값으로 넘기는 것을 권장함.

과거 `parseInt`는 문자열의 앞부분을 보고 진수를 판단하면서 자잘한 에러들이 많았다고 함. (특히 8진수)
하지만 ES5 이후부터는 `0x`로 시작할 때만 16진수로 처리하고 나머지 경우는 무조건 10진수로 처리한다.

아래의 예시에서 매우 충격적인 결과를 볼 수 있었다.

```javascript
// parseInt의 첫번째 인자에 Infinity를 넣은 것 부터 잘못되긴 했다.
// 19진법의 유효한 숫자는 0부터 0, (대소문자 구분 없이) a부터 i 까지이다.
parseInt(1/0, 19) // 18
```

1\. `1/0`의 결과는 Infinity이다. 이를 `ToString`한 결과 또한 Infinity이다.

2\. I는 19진수의 18에 해당한다.

3\. `parseInt`는 변환 가능할 때 까지만 수행하고 해당 결과를 반환해주므로 n에서 멈추게 된다.

## 암시적 변환
> 부수효과가 명확하지 않게 숨겨진 형태로 일어나는 타입변환

#### 문자열 <> 숫자
보통 `+` 연산자가 지대한 영향을 끼치는데, 덧셈/문자열 접합 두가지 목적으로 연잔사 오버로딩이 이루어짐.

```javascript
var a ='42'
var b ='0'

var c = 42
var d = 0

a + b // '420'
c + d // 42
a + d // '420'
```

`+` 알고리즘은 한쪽 피연산자가 문자열이거나 다음 과정을 통해 문자열 표현형으로 나타낼 수 있으면 문자열 붙이기를 함.
그 밖에는 언제나 숫자 덧셈을 한다.

```javascript
// TODO: 이건 뭘까? 나중에 생각해보자
[] + {} // [object Object]
{} + [] // 0
```





