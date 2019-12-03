# Automatic Semicolon Insertion (ASI)

> when JavaScript assumes a `;` in certain places in your JS program 
> even if you didn't put one there

자세한 내용은 https://tc39.es/ecma262/#sec-automatic-semicolon-insertion 을 참고하면 됨.

## ASI fails
- 가끔 ASI때문에 unexpeceted behavior로 인해 에러가 발생할 수 있음

#### Example: `return`
``` javascript
function arrayFromValue(item) {
  /* 
    return after newline without semi-colon 
    return;
      [item];
  */
  return
    [item];
}

arrayFromValue(10); // => undefined
```

- `return` 뒤에 `newline`이 오면 자동으로 세미콜론을 추가한다.
- `[item]`은 deadcode가 되고 `undefined` 를 리턴한다.

#### Example: IIFE
``` javascript
/*
  Uncaught TypeError: {} is not a function
  at <anonymous>:2:1
*/
let something = {}
(function() {})()

// how to resolve?
let something = {};
(function() {})()

// or,
let something = {}
;(function() {})()
```

#### Example: [...]
- 자바스크립트가 대괄호 `[...]` 앞에서는 세미콜론이 있다고 가정하지 않기 때문

``` javascript
alert("에러가 발생합니다.")

[1, 2].forEach(alert)

// Simplify: error-prone
alert("에러가 발생합니다.")[1, 2].forEach(alert)
```

---
## Reference
- https://dmitripavlutin.com/simple-but-tricky-javascript-interview-questions/#4-automatic-semicolon-insertion
- https://medium.com/@divyanshu013/to-semicolon-or-not-89c3dc73edf7
- https://ko.javascript.info/structure