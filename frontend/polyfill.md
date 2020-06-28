# Polyfill

> 이전 브라우저에서 최신 기능을 제공하는 데 필요한 코드; 혹은 브라우저가 다른 방식으로 동일한 기능을 구현하는 문제를 해결하는데 사용

## Modernizir에서 제공하는 목록
https://github.com/Modernizr/Modernizr/wiki/HTML5-Cross-Browser-Polyfills

## 지원하게 하려면?
#### 모든 폴리필을 전부 추가하고 싶다면?
- `babel-polyfill` 을 전역에 추가하는 방법
  - 7.4.0 부터 deprecated 되었음
  - 실제 사용되지 않는 폴리필도 추가되어 번들링되는 파일의 크기가 커짐
  - 한 페이지에서 하나의 babel-polyfill만 허용됨: 내부적으로 전역변수를 하나 두어 이미 실행되고 있는 지 체크; 전역 오염

```javascript
import "@babel/polyfill";
```

- `core-js` + `regenerator-runtime`
```javascript
import "core-js/stable";
import "regenerator-runtime/runtime";
```

- `@babel/preset-env` + `useBuiltIns: entry`: 사용된 폴리필 메서드만 전역 스코프에 추가
  - 지원할 브라우저 정보와 일부 옵션을 지정하면 자동으로 필요한 기능을 주입해줌 (babel plugins, core-js polyfills)
  - bable 설정의 preset 속성의 targets에 대상 브러우저의 버전을 명시
    - `"targets": "last 2 versions", "ie >= 11"`
    - https://github.com/browserslist/browserslist#full-list 
  
#### 필요한 폴리필만 추려서 추가하고 싶다면?
- `core-js`에서 필요한 폴리필 가져오기
  - 코드의 크기가 작지만 폴리필 타켓을 빠짐 없이 작성해야함
  - https://github.com/zloirock/core-js
  
```javascript
import 'core-js/features/array/from'; // <- at the top of your entry point
import 'core-js/features/array/flat'; // <- at the top of your entry point
import 'core-js/features/set';        // <- at the top of your entry point
import 'core-js/features/promise';    // <- at the top of your entry point
```
  
- `@babel/plugin-transform-runtime`
  - 실제로 코드에서 사용한 폴리필 메서드만 번들에 포함함
  - 트랜스파일링 과정에서 폴리필이 필요한 부분을 내부의 헬퍼 함수를 사용하도록 치환함
  - 샌드박스 제공
    - 내부적으로 core-js 내장 후 alias를 생성
    - 트랜스파일링 과정에서 폴리필이 필요한 부분들이 이 alias를 참조하도록 원본 코드를 변경
  - 최신 브러우저에 관계 없이 폴리필 코드가 무조건 물림
  - https://babeljs.io/docs/en/babel-plugin-transform-runtime
- `@babel/preset-env` + `useBuiltIns: usage`: 사용된 폴리필 메서드만 전역 스코프에 추가

## Polyfill.io: https://cdn.polyfill.io/v3/

#### 문제점
- 어떤 기능이 Polyfill에 의해 지원되는 지 알아야 함
- 어떤 Polyfill이 우리가 필요한 기능을 잘 지원하는 지 알아내는 것이 쉽지 않음
- 필요하지 않은 기능이 들어갈 경우, 커다란 번들 형태로 제공할 수 있음
- 최신 브라우저가 아닌 Polyfill이 필요한 브라우저에서만 쓰고 싶음

#### Polyfills as a Service
- 개발자가 페이지에 Polyfill 서비스를 로딩하는 스크립트 추가
- UA를 보고 필요한 Polyfill 목록을 만듬
- 상호간의 의존성 관계를 만족시킬 수 있도록 그래프 소팅 알고리즘에 의해 정렬됨
- 선택된 Polyfill 들은 minified 되어 CDN을 통해 제공됨

#### 이용 방법
```html
<script src="//cdn.polyfill.io/v1/polyfill.min.js" async defer></script>

<!-- Just the Array.from polyfill -->
<script src="//cdn.polyfill.io/v1/polyfill.min.js?features=Array.from" async defer></script>
```

---
## Reference
- https://developer.mozilla.org/ko/docs/Glossary/Polyfill
- http://hacks.mozilla.or.kr/2014/12/an-easier-way-of-using-polyfills/
- https://babeljs.io/docs/en/babel-polyfill/
- https://babeljs.io/docs/en/babel-plugin-transform-runtime/
- https://okchangwon.tistory.com/3
- https://okchangwon.tistory.com/4
