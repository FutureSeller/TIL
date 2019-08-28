# @babel/parser

## TL;DR

---

### Export 되는 친구들
- parse & parseExpression
- parserOptions
  - 가까운 미래애 바뀔 표준이나 특정 조건등에도 지원하기 위한 Option들이 보임
  - sourceType: script(default), module, ambiguous
  - plugins
- ParserPlugin과 그에 따른 config 

### src/utils
#### scopeflags.js: bitset으로 scope 표현
#### scope.js
- Scope 
  - lexcial scope을 기준으로 하나씩 가지며, 변수들과 Context를 저장
  - var: "var-declared names"
  - lexical: "lexically-declared names"
  - functions: "lexically-declared FunctionDeclaration names"
- ScopeHandler
  - 특정 scope에서 scope chain을 참고하여 변수가 사용될 수 있는 지, 추적하는 용도
  - ScopeStack: scope chain track을 위한 stack
    - scope에 진입할 때, scope의 context를 가진 flags와 함께 push / escape할 때 pop
  - scopeflags related helper functions
    - flag에 masking하여 해당 scope이 어떤 성격을 가지는지 확인
  - declareName: 현재 scope에서 선언된 변수의 이름을 각 context에 맞게 저장
    - redeclaration을 막기위해, flag를 고려하여 scope의 object traversal
    - Lexical declared의 경우, 
      - lexical, functions만 체크
      - scope마다 고유하기 때문
    - Var-declared의 경우
      - scope chain을 다 순회하며 확인
  - currentThisScope
    - 이름만 보고는.. 이게 가능한가? runtime에 binding이 될 수도 있는데?
    - var-declared function && class && !arrow_function
    - 단순히, super를 사용할 수 있는지/arrow function이 아닌지만 봄
    - 바꿔말하면, 동적으로 this binding이 될 수 있는 녀석들인지 확인함

#### 종합하자면
- 주로 scope chain을 다루기 위한 util로 구성됨
- identifier, whitespace, location은 부가적

### src/tokenizer (좀 자세히 봐보자 나중에)
말 그대로 JS code as input stream을 tokenize하는 단게

#### types.js
- README
  - 토큰이 갖는 context를 저장. parsing에 도움을 주기 위함
  - Convention: `_`로 시작함
  - Context
    - `beforeExpr`: regex 구분을 위함. regex가 "/"로 시작하기때문임
    - `startsExpr`: ? 
    - `isLoop`: loop시작에 마킹해놓고 확인하기 위함 -> do, for, while
    - `isAssign`: `=, +=, -= 등등`
    - `prefix`: `+, -, --, ++, !, ~`
    - `postfix`: `--, ++`
    - `binop`: `+, -, ^, ||, 등등`
    - `rightAssociative`:
- type, punctuation, keywords, bashbang, operators 토큰들을 미리 정의함 

#### state.js
- 토큰마다 State를 가지고 있음
- Location: { line, column }, Strict 한 scope에 있는 지
- context stack: `syntactic context`, comment stack

#### context.js
- Token Stream을 보고 in/out을 통해 Token Specific한 Context를 update하는 과정
- 다볼수는 없고 하나의 Pair만 보자면, 
  - `tt.[braceR|parenR].updateContext`
  - '('에 해당하는 context가 context stack에 있을 거라 예상
  - stack에 하나만 남아있다면 return. '(', ')'의 pair가 완성되어 더 이상 tracking할 필요 없음
  - braceStatement 였고 function이였다면, function scope을 제거해줌
  - state가 expression이 허용되는 지에 대해 다시 재정의함

#### context.js: token specific한 context들을 정의 
#### state.js
- tokens: [], only push
- comments: [], only push
- strict mode 여부
- arrow function 관련 처리
  - potential arrow function: "("로 시작하면 일단 potential하다고 봄
  - noArrowAt: `a ? (b) : c => d`, arrow function이 아님
  - noArrowParamsConversionAt
- comma with spread 관련 처리: destructure handling
- flags
  - param이냐, property name이냐, 등등
  - nested class 내부에 있는가
- label: loop/switch
- comment 저장(trailing, leading 등)
- (syntactic) context stack 

### index.js
- Tokenizer
  - 하나의 State 보유, input string
  - `lookahead`: 하나 혹은 몇몇개의 토큰을 미리 보는 것, current token은 아님
  - `next`: location info 기입 후, 다음 토큰으로 이동 
  - `match`: 현재 state와 예상한 state가 동일한지
  - `eat`: match된 토큰에 한 해, next로 넘김
  - `getTokenFromCode`
    - input stream의 position으로 charCode 가져옴
    - 각 토큰의 성격에 따라, pair를 등록해주거나 '(' -> ')'

### src/plugin-utils
- validatePlugins: plugin들의 공생관계를 나타냄
  - decorators
    - "cannot use" with decorators-legacy
    - "requires an option" decoratorBeforeExport
  - flow <-- x --> typescript
- mixedinPlugins: 포함 혹은 의존성이 있어 ordering이 중요해 보임

---
## Questions
### Q1. Lexical Declataion?
- let and const를 사용한 variable declaration
- var: function or global scope, regardless block
- let: limited scope in a block
- const: let + readOnly

### Q2. @flow 는 어떤 annotation?
### Q3. Scope Handler: How to handle hoisting?
- 혹시 할 필요가 없나? 할 필요는 있을 것 같은데. unused var 같은 것을 noti한다거나.

## Reference
- https://github.com/babel/babel/tree/master/packages/babel-parser/src
- https://googlechrome.github.io/samples/lexical-declarations-es6
