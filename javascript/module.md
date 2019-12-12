# Module

## Background

초기 사용된 대부분의 자바스크립트는 본래 웹 페이지에 약간의 상호 작용을 제공하는게 목적. Client-side 쪽 앱이 점점 커짐에 따라(대표적으로 Ajax의 등장) 빠른 엔진이 등장하게 되었고(V8) 웹 브라우저 바깥에서도(Node.js) 자바스크립트가 사용됨에 따라 모듈에 대한 필요성이 대두

## Features

- 엄격 모드로 실행됨 ('use strict')
- 모듈 레벨 스코프
- 단 한 번만 평가됨
  - 동일한 모듈이 여러 곳에서 사용되더라도 모듈은 최초 호출 시 단 한번만 실행됨
  - 실행 후 결과는 이 모듈을 가져가려는 모든 모듈에 전달됨
- `import.meta`: 현재 모듈에 대한 정보를 제공해줌; e.g., `import.meta.url`
- 브라우저에서 모듈은 항상 지연 실행됨 (`defer`)
  - 스크립트의 상대적 순서는 유지됨 (문서 상 위쪽의 스크립트부터 차례대로 실행됨)
  - HTML 페이지가 완전히 로딩된 후에 모듈이 실행됨
- 인라인 스크립트의 비동기 처리
  - `async`는 외부 스크립트를 불러올 때 유효
  - 모듈 스크립트에선 외부/내부 상관없이 적용 가능함
- 외부스크립트: 일반 스크립트보다 CORS를 좀 더 꼼꼼히 봄. Origin을 잘 보고 고려해야함
- 호환을 위한 `nomodule`: 과거 버전의 브라우저를 위해 존재
- 요새는 보통 번들러를 통해 올리기때문에, 실제로 `type="module"`을 쓸 이유가 없어보이긴함

## 다양한 진영의 커뮤니티 그리고 표준

### CommonJS

#### 모듈화

- Scope: 모듈은 자신만의 독립적인 실행 영역이 있어야 함
- Definition: 모듈 정의는 `export` 객체를 사용
- Usage: 모듈 사용은 `require` 함수를 사용

#### Example

```javascript
// (Scope) define a module: simple-math.js
const add = (x, y) => x + y;
const multiply = (x, y) => x * y;
module.exports = { add, multiply }; // (definition)

// (Scope) use a module: app.js
const simpleMath = require("./simple-math.js"); // (usage)
console.log(add); // undefined
simpleMath.add(3, 4); // 7
```

- Scope: 자바스크립트는 파일 기준으로 Scope를 생성
- Definition: `module.exports`
- Usage: `require(...)` → local path 기준, 즉 서버사이드 환경을 전제로 함

#### 문제점: in browser!

- 우선, ECMA standard와 독립적이라 브라우저에서 공식적으론 지원하지 않음
- 로컬 환경을 기준으로 작성됨. synchronous 한 loading이 기본
  - 모든 모듈의 의존성이 download -> parsing -> execute 될 때 까지 rendering/interaction이 block됨

#### 비동기 모듈 로드

- 브라우저에서는 서버사이드와 달리 파일 단위의 Scope이 없음
- `<script>`를 사용하여 모듈들을 차례대로 로드하면, 전역 변수 pollution이 발생할 가능성이 있음
- `module transport format`을 추가로 정의했음

```javascript
// require.define을 통해, closure로 만듬
require.define(
  {
    "complex-numbers/plus-two": function(require, exports) {
      var sum = require("./complex-number").sum;
      exports.plusTwo = function(a) {
        return sum(a, 2);
      };
    }
  },
  ["complex-numbers/math"]
); // complex-numbers/math가 먼저 로드되어야 함
```

### AMD(Asynchronous Module Definition)

- 비동기 상황에서도 자바스크립트 모듈을 사용하기 위해. CommonJS에서 독립한 그룹
- 브라우저 내에서 실행에 중점
- CommonJS와 호환할 수 있는 기능 제공: `require(), exports`
- `define` 함수를 통해 스코프 역할을 정의

#### Example

```javascript
// moduleA를 정의할 때, moduleB가 필요함을 나타냄
define("moduleA", ["require", "exports", "moduleB"], function(
  require,
  exports,
  moduleB
) {
  exports.verb = function() {
    // 넘겨받은 파라메터 사용
    return moduleB.verb();

    // require()를 사용
    return require("moduleB").verb();
  };
});
```

### UMD(Universal Module Definition)

- CommonJS, AMD 모두 같은 목적, 다만 방식이 다름. 두 방식을 모두 지원해야하는 상황이 필요
- 스펙이라기보다는 패턴
- IIFE(Immediately Invoked Function Expressions)를 사용

```javascript
/* 
  returnExports.js: https://github.com/umdjs/umd/blob/master/templates/returnExports.js
*/
(function(root, factory) {
  if (typeof define === "function" && define.amd) {
    // AMD
    define(["b"], factory);
  } else if (typeof module === "object" && module.exports) {
    // Node
    module.exports = factory(require("b"));
  } else {
    // Browser
    root.returnExports = factory(root.b);
  }
})(typeof self !== "undefined" ? self : this, function(b) {
  return {};
});
```

### ESM(ECMAScript Modules Syntax)

- ECMA진영에서 module 을 지원
- `import`, `export` 키워드를 사용할 수 있음: top-level scope에 정의

#### Example: usage in html

```html
<!-- type=module attribute -->
<script type="module" src="./main.js"></script>

<!-- inline: import -->
<script type="module">
  import { something } from "./path-from-anywhere";
</script>
```

#### Example: default and import

- 따로따로 이해를 예시를 들다보니 놓쳤던 것/헷갈렸던 것들이 있었음
  - e.g., `export default [expr]`을 어떻게 `import`하는 쪽에선 어떻게 해야하는가?
  - 아래와 같이 자기가 쓰고싶은 Identifier 아무거나 쓰면됨
- 그냥 기존의 예시들을 merge 함

```javascript
// a.module.js
export default Object.assign({}, { prop: 4})

// b.module.js
import A from 'a.module.js' // { prop : 4 }
import B from 'a.module.js' // { prop : 4 }
import { default as C } from 'a.module.js' // { prop: 4 }
import { D } from 'a.module.js' // undefined
import * as E from 'a.module.js' // { prop : 4 }

// c.module.js
export const getRandom = function() { ... }

// d.module.js
import { getRandom } from 'c.module.js' // [Function: getRandom]
import F from 'c.module.js' // undefined
import * as G from 'c.module.js' // { getRandom: [Function: getRandom] }
import { default as H } from 'c.module.js' // undefined

// e.module.js
export { a as A, b }

function a() {}
function b() {}

// f.module.js
import { A, b } from 'e.module.js' // [Function: a] [Function: b]
import { A, B } from 'e.module.js' // [Function: a] undefined
import { A, b as B } from 'e.module.js' // [Function: a] [Function: b]
```

## 동적으로 모듈 가져오기

#### 제약사항

- import 문에 동적 매개변수를 사용할 수 없음: 문자열만 허용됨
- import, export는 static함: 런타임이나 조건부로 모듈을 불러 올 수 없음

#### `import()` Expression

- `import(module)`은 모듈을 읽고 모듈을 프라미스로 감싼채 반환함. 호출은 어디서나 가능하며 동적으로 사용가능

```javascript
// say.js
export const hi = () => alert("hi");
export const bye = () => alert("bye");
export default () => alert("wow");

// executor
let say = await import("./say.js");
say.hi();
say.bye();
say.default();
```

---

## Reference

- https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Modules
- https://d2.naver.com/helloworld/12864
- https://en.wikipedia.org/wiki/CommonJS
- https://en.wikipedia.org/wiki/Asynchronous_module_definition
- https://github.com/umdjs/umd
- https://objectpartners.com/2019/05/24/javascript-modules-a-brief-history
- http://hacks.mozilla.or.kr/2016/05/es6-in-depth-modules
- https://ko.javascript.info/modules-intro
