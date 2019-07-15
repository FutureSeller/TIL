# 첫 인상
- JavaScript Compiler라고?
- JS Engine의 최적화 컴파일러는 아닌 것 같고 목적이 뭘까?

## 무엇을 하는가?
- Input: (최신 버전의 문법으로 작성된) 자바스크립트 코드
- Output: (상대적으로 과거 버전의 문법으로 작성된) 자바스크립트 코드
- 즉, 새로운 문법을 과거 문법으로. Semantically equivalent한 코드를 생성
- 왜? "compatiable version of JS in current and 'older' browers or environments"
``` javascript
// ES2015 arrow function
[1, 2, 3].map(n => n+1);

// ES5 equivalent
[1, 2, 3].map(function(n) {
  return n + 1;
});
```
- Q. ECMASpec을 사람이 하나도 안 거스르고 잘 작동하게 할 수 있나?
  - 바꿔말하면, Syntactic Transformation이 Semantically Equivalent하다고 보장할 수 있나?
  - 쉽게말하면, Semantic Bug가 매우 많을 것 같은데 없나?
  - 자바스크립트는 너무 dynamic함..
  - 역시 issue가 많다.  e.g., https://github.com/babel/babel/issues/10027
  - 쓰려면 Babel의 이슈인지, 내 코드의 이슈인지 구분할 수 있어야한다.

## flow
```
--------------------------------------------------------------------
input  ->   parse   -> (AST) transform -> (Code) generator -> output
 [JS]     [@parser]      [@transform]        [@generator]     [JS`]
--------------------------------------------------------------------
```
- parse: tokenize -> AST (ESTree와 약간 달라보임. Misc같은 것도 있고..)
- transform: 아직 보진 않았지만, ast에 visitor를 plugin 형태로 끼워넣어 transform 할 듯
- generator: AST기반 code generate. 이것또한 plugin 형태가 존재할 것 같음

## 특징
- Spec Compliant: ECMAScript 표준을 따름
- Pluggable
- Debuggable: Source map 지원

## Preset
- 버전별로 필요한 플러그인들을 모아놓은 set
- Why?
  - babel은 코어 기능만 있고 실제 코드 변환시 기능별로 확장된 플러그인들 필요
  - arrow-function, class, object-rest-spread etc.
  - 위의 기능들을 다 따로따로 설치하기 너무 힘들기때문에 모아 놓은 것
- @babel/preset-react, @babel/preset-flow

--- 
## Reference
- https://babeljs.io/docs/en/
