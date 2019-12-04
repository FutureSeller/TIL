코드리뷰 스터디에서 코드를 읽다가 어떤 분의 유틸함수에서 *Falsy(), *Truthy() 이런식의 함수를 보게 되었음.
Falsy와 Truthy가 뭔지 궁금해져서 찾아보았음.

조건: JavaScript에서는 boolean 타입이 와야 하는 자리에 다른 타입의 값이 와도 에러가 나지 않고 실행됨.

### Falsy
- 위의 조건에서 false로 취급되는 것들을 의미함
``` javascript
false
0
''
""
null
undefined
NaN
```

### Truthy
- 위의 조건에서 true로 취급되는 것들을 의미함
- 위의 경우를 제외한 나머지 것들

### What the...

``` javascript
$ node
> false == 0
true
> false === 0
false
```

* 더불어 알게 된점
  * 이런 저런 코드를 읽다보면 다른 언어와 달리 JS에는 negate가 참 많이 쓰이는 걸 알 수 있었음
  * 레퍼런스의 예시들을 보고 든 생각은 풀어쓰려면 얼마든지 풀어서 검증할 수 있는데, 좀 짧게 그리고 포괄적으로 비교하고자 하는 것처럼 보임

``` javascript
// 1. Avoid direct comparisons
// instead of
if (x == false) // ...
// runs if x is false, 0, '', or []

// use
if (!x) // ...
// runs if x is false, 0, '', NaN, null or undefined

// 2. Use === strict equality
// instead of
if (x == y) // ...
// runs if x and y are both truthy or both falsy
// e.g. x = null and y = undefined

// use
if (x === y) // ...
// runs if x and y are identical...
// except when both are NaN

// 3. Convert to real Boolean values where necessary
$ node
> a = NaN
NaN
> b = NaN
NaN
> a === b
false
> !!a === !!b
true
```

### AND, OR 연산자와의 관계

#### OR (||) with truthy

- 가장 왼쪽 피연산자부터 시작해 오른쪽으로 피연산자를 evaluate
- 각 피연산자를 불린형으로 변환. 변환 후, true면 멈추고 해당 피연산자의 원래 값을 반환
- 피연산자 모두를 evalutate 했으면, 마지막 피연산자를 반환

``` javascript
// json_input1 : null
// json_input2 : undefined
const foo = json_input1 || json_input2 || {}
console.log(foo) // {}

// json_input2 : { props: 1 }
const bar = json_input1 || json_input2 || {}
console.log(bar) // { props: 1 }

let x;
true || (x = 1)
console.log(x) // undefined; if문 대용으로 쓰임

false || (x = 1)
console.log(x) // 1
```

#### AND (&&) with falsy
- OR과 동일한데, 변환 후 값이 false인 경우에 해당 피연산자의 원래 값을 반환함

``` javascript
const result = 5 && 0 && 1
console.log(result) // 0

let x = 1
(x > 0) && console.log('here') // here; if문 대용으로 쓰임
```

### Questions
<details><summary> 10 == 5 </summary><pre>
False, if 10 == 10 then True
</pre></details>
<details><summary> 1 == "1" </summary><pre>
True, if 1 === "1" then False
</pre></details>
<details><summary> NaN == NaN </summary><pre>
False
</pre></details>
<details><summary> NaN === NaN </summary><pre>
False, Not a Number 임을 알려줄 뿐, 어떤 값인지 알 수 없음
</pre></details>

--- 
## Reference
- https://helloworldjavascript.net/pages/150-boolean.html
- https://www.sitepoint.com/javascript-truthy-falsy
- https://ko.javascript.info/logical-operators