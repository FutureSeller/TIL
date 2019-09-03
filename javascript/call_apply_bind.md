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
- bind 시, `bound function`을 반환함. (A bound function is an exotic object that wraps another function object.)
- chaining bind는 안되는데 rebind는 됨
  - chaining bind: `a.bind().bind()`
  - rebind: `a.bind(); \n a.bind(); ...`
  - 왜? (https://stackoverflow.com/questions/26545549/chaining-bind-calls-in-javascript-unexpected-result#answer-26547029)
  - `Function.prototype.bind`의 [pollyfill](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#%ED%8F%B4%EB%A6%AC%ED%95%84)을 보면 bind가 이전 this를 물고있음

```javascript
function a() {
  console.log(this);
}

a.bind({foo:"bar"}).bind({oof:"rab"})(); // { foo: "bar" }
a.bind({foo:"bar"})(); // { foo: "bar" }
a.bind({oof:"rab"})(); // { oof: "rab" }
```

## 응용
- `arguments`같은 array-like object를 다룸
  - array-like: index로 접근 가능 + length 속성 있음. 그러나 array method 사용 불가
  
```javascript
function example3() {
  // Array.from(arguments).join(',');
  console.log(Array.prototype.join.call(arguments)); 
}
example3(1, 'string', true); // '1,string,true'
```

---
## Reference
- https://www.zerocho.com/category/JavaScript/post/57433645a48729787807c3fd
