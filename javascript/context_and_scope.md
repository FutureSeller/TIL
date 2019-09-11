# Execution Context
- 실행 가능한 코드가 실행되는 환경
- 실행 가능한 코드 (executable code)를 만나면 생성됨
  - 전역 코드
  - 함수 코드
  - Eval
- 구성 요소
  - 변수: 전역/지역/매개변수, 객체의 프로퍼티
  - 함수 선언
  - 변수의 유효범위(Scope)
  - this


``` javascript
var x = 'xxx';

function foo () {
  var y = 'yyy';

  function bar () {
    var z = 'zzz';
    console.log(x + y + z);
  }
  bar();
}
foo();

/*
                       |bar|
            |foo|      |foo|      |foo|
|global| > |global| > |global| > |global| > |global|
  [1]        [2]        [3]         [4]       [5]

[1] 시작할 때, 전역 컨텍스트 스택에 push. 종료될 때 까지 유지
[2-4] 함수 호출 시 마다 컨텍스트 생성과 동시에 push
[2-4] 함수 실행이 끝나면 직전 실행 컨텍스트에 컨트롤 반환
*/
```

## 실행 컨텍스트의 3가지 객체
```
ExecutionContext {
  VariableObject {
    Variables: [],
    FunctionDeclarations: [],
    Arguments: []
  },
  ScopeChain {
    parent: 
  },
  thisValue: Context
}
```

### Variable Object
- parameters, arguments
- function declartaions
- variables
- 브라우저에서 globalEC의 VO는 window임

``` javascript
// 모든 전역 변수/함수 등을 포함하는 전역객체 가리킴
// 전역 객체는 전역에 선언된 전역 변수와 전역함수를 프로퍼티로 소유
const GO = {
  foo : { 'type': 'FunctionDeclaration', ... },
  x : { 'type': 'VariableDeclaration', ... }
}
const globalEC = {
  VO: GO 
}
```

- 함수 컨텍스트
``` javascript
// Activation Object(AO): 활성객체
// 매개변수와 인수들의 정보를 배열의 형태로 담고 있는(Array-like) arguments 추가됨
const AO = {
  arguments: { length: 0 },
  bar: { 'type': 'FunctionDeclaration', ... },
  y: { 'type': 'VariableDeclaration', ... }
}
const fooEC = {
  VO: AO
}
```

### Scope Chain
- 현재 EC의 VO + 상위 EC의 Scope Chain
- 전역 객체와 중첩된 함수의 스코프의 레퍼런스를 저장
- 식별자 중에서 객체(전역 객체 제외)의 프로퍼티가 아닌 변수를 검색
-  프로퍼티를 검색하는 것은 `Prototype Chain`
``` javascript

-----------------------------
// foo()

ExecutionContext {
  VariableObject {
    Variables: [
      y: { 'type': 'VariableDeclaration', ... }
    ],
    FunctionDeclarations: [
      bar: { 'type': 'FunctionDeclaration', ... },
    ],
    Arguments: []
  },
  ScopeChain {
    parent: global
  },
  thisValue: global
}

-----------------------------
// global

ExecutionContext {
  VariableObject {
    Variables: [
      x : { 'type': 'VariableDeclaration', ... }
    ],
    FunctionDeclarations: [
      foo : { 'type': 'FunctionDeclaration', ... }
    ]
  },
  ScopeChain {
    parent: global
  },
  thisValue: global
}
```


### This
- 함수 호출 패턴에 의해 결정됨.

--- 
## Reference
- https://poiemaweb.com/js-execution-context
