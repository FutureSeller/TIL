``` javascript
function foo() {
  let a = b = 0;
  a++;
  return a;
}

foo();
console.log(typeof a); // undefined
console.log(typeof b); // number
```

`let a = b = 0`을 풀어서 쓰면 `let a = 0; b = 0;`이 된다.
따라서, 의도치 않게 `b`는 global scope에 위치하게 된다.
한 줄로 꼭 줄이고 싶다면 CommaExpression을 사용하면 된다. (`let a = 0, b = 0`)
다만, 내부에서 정한 convention을 반드시 따르는 걸 추천한다.

---
## Reference
https://dmitripavlutin.com/simple-but-tricky-javascript-interview-questions/#1-accidental-global-variable