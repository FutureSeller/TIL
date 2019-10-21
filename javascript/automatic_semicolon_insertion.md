``` javascript
function arrayFromValue(item) {
  return
    [item];
}

arrayFromValue(10); // => ???
```

`return` 뒤에 `newline`이 오면 자동으로 세미콜론을 추가한다.
`[item]`은 deadcode가 되고 `undefined` 를 리턴한다.

---
## Reference
https://dmitripavlutin.com/simple-but-tricky-javascript-interview-questions/#4-automatic-semicolon-insertion