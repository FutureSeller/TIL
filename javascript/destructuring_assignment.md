# Destructuring Assignment

너무 편리하고 잘 사용하고 있는 방법인데, 놓쳤던 것들을 일부 적어놓으려고 함

#### 할당 연산자 좌측엔 뭐든지 올 수 있습니다.
- Assignable 한 것이면 어떤 것이든 올 수 있음

``` javascript
// 보통 이렇게 많이 썼음
const [name, surname] = "Ilya Kantor".split(' ')

// 이렇게도 가능하다고 함
let user = {};
[user.name, user.surname] = "Ilya Kantor".split(' ');

// 이렇게도 가능은 하다고 하는데, 이렇게 까진 쓰지 않을 것 같음
let [name = prompt('name?'), surname = prompt('surname?')] = ["Julius"];
console.log(name) // Julius
console.log(surname) // from Prompt
```

#### 너무 잘 쓰고 있는 alias 와 assign
``` javascript
let options = {
  title: "Menu",
}

let { width: w = 100 } = options
console.log(w) // 100

function showMenu({ title = "Untitled", width = 200 }) {
  ...
}
```

---
## Reference
- https://ko.javascript.info/destructuring-assignment