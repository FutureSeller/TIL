## call, apply
``` js
var obj = {
  string: 'zero',
  yell: function() {
    alert(this.string);
  }
};
var obj2 = {
  string: 'what?'
};
obj.yell(); // 'zero';
obj.yell.call(obj2); // 'what?'
```
- call과 apply의 차이는, 파라미터를 넘길때 각각을 넘기느냐 배열로 묶어서 넘기느냐의 차이
- 첫 번째 argument는 `this`를 의미
  - `obj.yell();`이면 this가 obj니까
  - `obj.yell.call(obj2);`면 this가 obj2니까

## bind
- 함수 호출은 하지 않고, bind까지만 하고 끝
- 나중에 호출할 때, this를 binding 해놓음

## 응용
- `arguments`같은 array-like object를 다룸
  - array-like: index로 접근 가능 + length 속성 있음. 그러나 array method 사용 불가
  
```js
function example3() {
  // Array.from(arguments).join(',');
  console.log(Array.prototype.join.call(arguments)); 
}
example3(1, 'string', true); // '1,string,true'
```

---
## Reference
- https://www.zerocho.com/category/JavaScript/post/57433645a48729787807c3fd
