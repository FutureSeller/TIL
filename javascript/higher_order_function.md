## Higher-order function
> A higher order function is a function that *takes a function as an argument*, or *returns a function as a result*

자바스크립트의 함수는 first-class citizen이니 위의 문구는 명백히 true 임을 알 수 있다.
first-class citizen에 대한 내용은 아래와 같다.

### FIRST-CLASS CITIZENS, FIRST-CLASS OBJECT/FUNCTION
> 변수(variable)에 담을 수 있다.
> 인자(parameter)로 전달할 수 있다.
> 반환값(return value)으로 전달할 수 있다.

#### FIRST-CLASS FUNCTION (theoretically)
- 익명 함수를 지원해야한다. (function literals)

아무튼, 자바스크립트에서 함수는 first-class citizen. first-class function 이다.

#### Example
``` javascript
// 1. 변수에 담을 수 있다.
const sayHello = () => "Hello, ";

// 2. 인자로 전달 할 수 있다.
function greeting = (helloMessage, name) => {
  console.log(helloMessage() + name);
}
greeting(sayHello, 'FutureSeller');

// 3. 반환값으로 전달할 수 있다.
function dummy() => {
  return function() {
    return "dummy function";
  }
}
```

### Usage

#### Array.prototype.[map | filter | ...... ]
``` javascript
// without higher-order function
const array = [1,2,3];
const doubledArray = [];
for(let i=0; i < array.length; i+=1) {
  doubledArray.push(array[i]);
}

// with higher-order function
const array = [1,2,3];
const doubledArray = array.map(item => item * 2);
```

#### DOM-related usage
``` javascript
const onToggle = (e) => ......;
document.querySelector('.className').addEventListener('click', onToggle);
```

---
## Reference
- https://en.wikipedia.org/wiki/First-class_citizen
- https://en.wikipedia.org/wiki/First-class_function
- https://developer.mozilla.org/ko/docs/Glossary/First-class_Function
- https://jrsinclair.com/articles/2019/what-is-a-higher-order-function-and-why-should-anyone-care/?fbclid=IwAR2RuHQENWNhekL3ZIJHzqWSG6vxoHOg6OD-bjg3zVvQX41NvYldwku7Yyo
- https://blog.bitsrc.io/understanding-higher-order-functions-in-javascript-75461803bad
- https://bestalign.github.io/2015/10/18/first-class-object (ko)
