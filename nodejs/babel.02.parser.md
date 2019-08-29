# @babel/parser

## TL;DR
> JavaScript를 입력 값으로 받고, JSON 형태의 AST(Abstract Syntax Tree)를 반환한다.
> Plugin 적용은 기존 파서를 Mixin하여 파서를 재정의한다.

---
### Parsing Strategy: Predictive parsing
- 간단히 특징만 말하자면, back tracking 없이 k개의 token을 미리 확인해보고(lookahead)를 문법에 맞는지 확인함
- 부가적으로 parsing table이 필요함 등등의 자세한 내용까지는 여기서 다루지 않음
- https://en.wikipedia.org/wiki/Recursive_descent_parser

### 사용되는 AST Nodes
- [ast/spec.md](https://github.com/babel/babel/blob/master/packages/babel-parser/ast/spec.md), [types](https://github.com/babel/babel/blob/master/packages/babel-parser/src/types.js)
- 표준화된 ECMASpec에 나타나는 rule들 + @, harmony들은 plugin에 정의되어있을 것이라 짐작함
- estree에 뿌리를 두고 있는 것 같고 둘을 비교했을 때, babel이 좀 더 세분화 되어있음 (e.g., NullLiteral...). 
- 왜 estree 진영은 세분화된 노드를 반영하지 않을까? 좋아보이는데.
  - estree의 철학때문: backward compatibility; [link](https://github.com/estree/estree/issues/120#issuecomment-174512304)

### How Plugin Works?
- parsing을 시작하기 직전 기존의 파서를 mixin하여 재정의된 파서를 생성 (필요 시 method 재정의)
- mixin되는 순서가 중요함. plugin간 dependency가 있을 수 있음
- 만약, plugin을 custom해서 사용한다고 했을 때, 잘못된 재정의로 인해 unintended한 결과를 생성할 수 있음
- 이미 잘 알려진 plugin들은 파서가 이미 정의한 의존성에 의해 에러를 뱉어줌 (e.g., decorator)
- 재정의된 예시: estree; [plugins/estree](https://github.com/babel/babel/blob/master/packages/babel-parser/src/plugins/estree.js)
  - `isStrictBody` 재정의: estree와 babel이 사용하는 node의 shape이 다름. `body.directives` vs `ExpressionStatement`
  - `parseExprAtom` 등등도 위와 동일한 이유로 재정의가 필요함

``` bash
$ grep -r "isStrictBody" src
src/plugins/estree.js:    isStrictBody(node: { body: N.BlockStatement }): boolean {
src/parser/expression.js:  isStrictBody(node: { body: N.BlockStatement }): boolean {
```

``` javascript
// src/parser/expression.js                                                // src/plugins/estree.js
isStrictBody(node: { body: N.BlockStatement }): boolean {              |   isStrictBody(node: { body: N.BlockStatement }): boolean {
     const isBlockStatement = node.body.type === "BlockStatement";     |     const isBlockStatement = node.body.type === "BlockStatement";
     if (isBlockStatement && node.body.directives.length) {            |     if (isBlockStatement && node.body.body.length > 0) {
       for (const directive of node.body.directives) {                 |       for (const directive of node.body.body) {
         if (directive.value.value === "use strict") {                 |         if (
           return true;                                                |           directive.type === "ExpressionStatement" &&
         }                                                             |           directive.expression.type === "Literal"
       }                                                               |         ) {
     }                                                                 |           if (directive.expression.value === "use strict") return true;
     return false;                                                     |         } else {
   }                                                                   |           // Break for the first non literal expression
                                                                       |           break;
```

### User's perspective
``` javascript
var parser = require("..");
var fs = require("fs");

var filename = process.argv[2];
if (!filename) {
  console.error("no filename specified");
  process.exit(0);
}

// 사용하고자하는 plugin 적절히 기재
var plugins = [ ........ ];
var file = fs.readFileSync(filename, "utf8");

// 사용하고자 하는 option들 적절히 기재
var parseOptions = { someOptions, plugins }; 
var ast = parser.parse(file, parseOptions);

console.log(JSON.stringify(ast, null, "  "));
```

- input: JavaScript code, parseOptions(plugins, sourceType, etc.)
- output: JSON 형태의 Abstract Syntax Tree 

### Tokenizer
- input stream을 의미 있는 단위인 token으로 쪼개는 컴포넌트
- State
  - Tokenizer가 현재 바라보고있는 token의 상태를 나타냄
  - 파싱에 도움이 될만한 정보를 token이 가지고 있음
    - type: 현재 token이 어떤 token인지 나타냄. 예를 들면 '.'은 dot; [src/tokenizer/types.js](https://github.com/babel/babel/blob/master/packages/babel-parser/src/tokenizer/types.js)를 참조
    - value: token의 raw value
    - strict: strict mode의 scope에 존재하는 token 인지
    - tokens: token들의 저장소
    - context: (syntactic) context stack (context는 아래를 참조)
- Context
  - 'function', 'if', 'for', 'while', 'with', '(', '{', '`' 등 
  - 특정 context를 enter하는 token을 만났을 때 해당 context를 push, leave 할 때 pop
  - e.g., `this.state.context.push(types.functionStatement);`
- (immutable) input & input.length: JavaScript
- Methods
  - next: 현재 input stream position을 기준으로 다음 token을 가져옴
  - match: 현재 tokenizer가 바라보고있는 token의 type이 파라메터로 들어온 type과 일치하는지 확인
  - eat: match가 true를 반환 시, next() 호출
  - lookahead: 현재 token과 state를 저장해놓고, 다음 token을 가져온 뒤 복원
  - readWord/readNumber/....: input stream의 현재 index와 value을 기준으로 tokenizing 룰에 의해 일치할 때까지 값을 읽어들인 후, token 반환

### ScopeHandler
- [src/util/scopeflags.js](https://github.com/babel/babel/blob/master/packages/babel-parser/src/util/scopeflags.js)
- [src/util/scope.js](https://github.com/babel/babel/blob/master/packages/babel-parser/src/util/scope.js)
- Scope: JavaScript's Scope, 변수들과 Context를 저장 
  - 어떤 scope 인지는 bitset으로 표현. masking으로 판별 가능
  - var: "var-declared names"
  - lexical: "lexically-declared names"
  - functions: "lexically-declared FunctionDeclaration names"
- ScopeHandler
  - ScopeStack === Scope Chain
    - parse 과정 중, 가령 특정 scope을 가진 statement의 파싱이 시작될 때 enter
    - statement의 파싱이 끝날 때, exit
  - 각종 helper 함수들 존재. 예를 들면,
    - 현재 scope이 function 이냐,
    - 현재 scope에 해당 Variable이 선언되었는지 확인하고 등록해라 등등

### Parser
- extends Tokenizer, ScopeHandler를 가지고 있음
- parsing 진행하면서, 파싱 규칙에 상응하는 context 부여.
  - context에 위반하는 token이나
  - 정의된 파싱 규칙에 없는 token이나 node가 나오거나 등등의 오류 처리
- JSON 형태의 Abstract Syntax Tree 반환

``` javascript
// Async가 아닌 scope에서 await keyword를 사용했을 때 error handling
if (this.scope.inAsync && word === "await") {
  this.raise(
    startLoc,
    "Can not use 'await' as identifier inside an async function",
  );
}
```

---
## Questions
### Q1. Lexical Declaration?
- let and const를 사용한 variable declaration
- var: function or global scope, regardless block
- let: limited scope in a block
- const: let + readOnly

### Q2. @flow 는 어떤 annotation?
- https://flow.org/en/docs/types

### Q3. Scope Handler: How to handle hoisting?
- hoisting까지 고려할 필요는 없다. 당연하게도 runtime behavior까지 잡아줄 수 없다.
- let 과 같이 재정의 할 수 없는 부분만 잡아주면 되고, 
hoisting 하기전 어떤 변수나 함수가 쓰였다고해서 syntactically invalid 하진 않으니까
- 아래와 같이 명백히 재정의할 수 없는 변수를 정의하면 error를 뱉어준다.
``` javascript
const parser = require('@babel/parser')

const code = `
  function a() {
    let b = 10;

    function b() {
    }
  }
  a();
`
const ast = parser.parse(code) // SyntaxError: Identifier 'b' has already been declared (5:13)
console.log(JSON.stringify(ast)); 
```

## Reference
- https://github.com/babel/babel/tree/master/packages/babel-parser/src
- https://googlechrome.github.io/samples/lexical-declarations-es6
