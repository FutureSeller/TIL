### Closure
> combination of a function and the lexical environment within which that function was declared - MDN

- 직역하자면 함수 + 함수가 속해있는 lexical environment를 가지고 있는 것
- lexical environment? → Lexical Scoping `Scope { Variable Object }`
- closure는 outer function의 변수에 접근할 수 있다.

``` javascript
// MDN의 예제: closure
function init() {
  var name = 'Mozilla'
  function displayName() {  // closure: init의 lexical scope에 속해있는 함수
    alert(name)             // init의 name을 referencing
  }
  return displayName        // lexical scope의 reference를 유지한 채, displayName을 return
}
var myFunc = init()         // 이 시점에서 myFunc -> displayName -> [[Scope: init]]
myFunc()
```
- 예제를 풀어서 말하자면
  - `displayName`은 자기자신 뿐만 아니라 `init`의 scope를 referencing하고 있는 상태
  - Engine의 입장: GC는 아직 해당 object(`name`, 정확히 말하자면 scope를 wrapping하는 object)를 referencing하고 있기때문에 sweep할 수 없음
  - `init`의 `name`은 engine의 계속 참조될 수 있고 해당 object에 연산 또한 가능함
  - `init()`은 내부 함수인 `displayName` object (function)을 return
  - 이러한 `displayName`을 Closure라고 함

``` javascript
// Example: inner function
function add(num) {
  var acc = 0
  function _ops() {
    return acc + num
  }
  return _ops()
}
var result = add(1) // 1
result = add(1) // 1
```

- 예제를 풀어서 말하자면
  - `_ops`는 `acc`에 접근 할 수 있음. (lexical scoping에 의해)
  - Engine의 입장
    - `acc`와 `num`은 `add`의 scope에 바인딩 되어있음. outer scope에선 볼 수 없음
    - `_ops()`는 `acc + num`라는 결과 값을 반환 함
    - `acc`와 `num`은 outer scope에서 볼 수 없으니 sweep함

### Questions
- Q. 이런 특징이 있는 건 알겠는 데 Closure를 왜 쓰는 거지? == 장점은?
  - Stateful. Encapsulation
- Q. 단점은?
  - 제대로 관리해주지 않으면 memory leak → explicitly free가 필요 (적절한 nullify)
  - memory leak
    - 사용하지 않는 메모리가 남아있는 경우 (general)
    - (= memory disclosure in security) 잘 구분해서 쓰도록 하자..
- Q. Nested function은 모두 Closure 이다? → No
  - 공통점: 내부 함수가 외부 함수의 변수에 접근할 수 있음
  - 다른점: outer function이 return 되었을 때, inner function이 outer function의 lexical scope을 참조할 경우에만 Closure
- Q. 아래 코드의 문제점과 해결법? (from MDN)
  ``` javascript
  function showHelp(help) {
    document.getElementById('help').innerHTML = help;
  }

  function setupHelp() {
    var helpText = [
      {'id': 'email', 'help': 'Your e-mail address'},
      {'id': 'name', 'help': 'Your full name'},
      {'id': 'age', 'help': 'Your age (you must be over 16)'}
    ];

    for (var i = 0; i < helpText.length; i++) {
      var item = helpText[i];
      document.getElementById(item.id).onfocus = function() { // [1]
        showHelp(item.help);
      }
    }
  }
  setupHelp();
  /*
    root cause: [1]이 closure. item.help를 공유하기 때문에 item의 help는 모두 age의 help가 됨
    resolve:
      - Closure를 덧댄다 : Closure는 enclosing lexical scope만 바라보기 때문에 lexical scope을 하나 더 만들면됨
      - var 대신 let 을 쓴다. (lexical scope 알아서 해 줌)
  */
  ```

## Reference
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures