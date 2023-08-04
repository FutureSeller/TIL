현재 작업하고 있는 프로젝트는 피그마에서 icon들을 figma API를 통해 가져오고 있다.
파일이름 기준으로 아이콘을 생성하고 있는데, svg 파일이름이 동일한 경우 viewbox가 다른 녀석들이 덮어씌워져서 종종 원치않는 결과가 나오게된다.
이 문제를 해결하기 위해 size별 directory로 나누는 작업을 진행중이다. (기존 오픈소스 라이브러리들이 왜 이렇게 구분하는지 알 거 같기도하다.)

아무튼, directory별로 나누고 `import { ABCD } from @package/24` 이런 꼴로 컴포넌트를 가져오고자 했는데, 이때 package.json의 `exports`를 사용해서 문제를 풀면 나이스헤보였다.
(정리된 글이 아니라 의식의 흐름대로 적은 글임)

ts 컴파일러는 모듈을 해석하고 가져오기 위해 classic, node 두 가지 전략을 취한다. 현재 라이브러리 사용처는 `node`로 세팅되어있는 상태.
- node: node.js의 cjs로 모듈을 찾으려함.
- classic: <= ts@1.5. 이전 버전의 모듈 해석 방식이 필요한 경우 사용. 특별히 쓸일이 없어보인다.


기존 라이브러리 중 하나가 esm 파일만 생성해주고 있었다. 혼란스러운 부분은 위의 설명에 따르면 cjs 모듈 해석 방식으로 import를 해석하려고 하는데, 여기선 에러를 내뱉고 있지 않았다.

```typescript
export function add(a:number, b:number){
  return a + b;
}

import {add} from 'a-library'
```

왜? `moduleResolution: node`로 설정되면, ts 컴파일러는 esm의 라이브러리를 cjs 형식에서 사용할 수 있도록 적절히 해석한다. 이런 호환성은 node.js 내장 기능에 의해 지원된다고 한다.

`Paths will be evaluated by tsc under Node’s CJS rules, but then at runtime, Node will evaluate them under its ESM rules since you’re emitting ESM.`

즉, cjs path resolve 알고리즘으로 모듈을 찾고, 찾았는데 esm 파일이면 알아서 esm으로 evaluate하기 때문에 문제가 없다는 것이다.
오해했던 것이 `모듈 해석 알고리즘`이였는데, *모듈 해석(module resolution)은 컴파일러가 import가 무엇을 참조하는지 알아내기 위해 사용하는 프로세스*라는 것이다.

`import {a} from "moduleA"`라고 했을 때, 정확히 무엇을 참조하는지 알아내기 위한 과정인 것이다.
나는 이걸 어떤 파일을 참조할 지 resolve하는 과정 + evaluation까지라고 생각했는데 구분해서 생각해야하는 것이였다. (정적으로 봐야하니 좀 당연한가?)
이 참조하는 로직은... 설명이 여기저기 많으니 참조

이제 `exports` 기능을 사용하기위해 아주 간단한 세팅을 해보자. `type="module"`이 지정되어있지 않으니 js는 cjs, module은 mjs라는 확장자명을 주어 구분한다.

```js
{
  name: "a-library",
  files: ["dist"],
  exports: {
    "./math": {
      "type": "./dist/math/index.d.ts",
      "import": "./dist/math/index.mjs",
      "require": "./dist/math/index.js"
    }
  }
}
```

이때 `moduleResolustion: node`기 때문에 exports를 인식하지 못하고 각각 가져와서 쓰려면 `@a-library/dist/math` 이런식으로 써야했다.

package.json의 `exports`를 지원하기 위해서는 moduleResolustion을 nodenext나 node16 정도로 해두면 된다. (nodenext는 node.js의 esm 기능과 exports 필드를 지원하기 위함)
일반적으로 `moduleResolution: node`는 cjs 형식을 기대하지만, nodenext에서는 exports 필드를 사용하면 더 적합한 동작을 제공하곤 한다.

`moduleResolution: nodenext`로 변경하니 기존에 사용하고 esm만 내뱉고 있는 아래와 같은 라이브러리가 문제가 생겼다.

> The current file is a CommonJS module whose imports will produce 'require' calls; 
> however, the referenced file is an ECMAScript module and cannot be imported with 'require'.
> Consider writing a dynamic 'import("b-library")' call instead.

`node`와 `nodenext`의 차이점을 되짚어보자.

1. node
  - node.js의 기본 cjs 모듈과 호환
  - ts 컴파일러는 js, json, node 확장자를 가진 파일을 cjs로 간주하고 cjs 모듈 해석 알고리즘사용
  - esm 형식의 모듈과 exports 필드를 인식하지 않음. package.json의 type도 열심히 참조함.
2. nodenext
  - ts에서 node.js의 esm 기능과 exports를 지원
  - node보다 더 esm에 적합한 모듈 해석 방식을 사용

(추측 및 가설) 
- 현재 상황: 라이브러리 package.json의 "type"이 module도 세팅되어있고 이녀석의 확장자는 `.js`
- [`moduleResolution: node`에서는 node.js가 "알아서" 해줬는데](https://www.typescriptlang.org/tsconfig#moduleResolution), nodenext가 되면서 명시적으로 취급하면서(?) cjs로 resolving하려니 에러가 난게 아닐까?

[module resolution full algorithm](https://nodejs.org/api/modules.html#modules_all_together)을 보면 아래와 같은 과정을 거친다(cjs -> require)

- LOAD_NODE_MODULES(X, dirname(Y))
  - LOAD_AS_DIRECTORY(DIR / X): X/package.json is a file > look for "main" > `path.resolve(Y, ${main})`
      - LOAD_AS_FILE: X is a file. load X as its file extension format. STOP

(esm - resolution and loading)[https://nodejs.org/api/esm.html#resolution-and-loading-algorithm](https://nodejs.org/api/esm.html#resolution-algorithm-specification)]을 보면 아래와 같은 과정을 거친다

- ESM-RESOLVE(specifier, parentURL)
  - PACKAGE_RESOLVE(specifier, parentURL)
    - 11. parentURL is not the file system root > return package.json ['main']

좀 더 파봐야하겠지만.... 뭐 아무튼 요약하자면. type="module"이니 ESM-RESOLVE를 사용하려고 했을 것인데, 현재 환경이 CJS여서 그런게 아닐까 싶다. (아직도 추측 중. 시간이 없어 나중에 다시 살펴보기로)

---

암튼. exports를 사용하려면 `moduleResolution: nodenext | node16`을 써야 지원하고, 기존 패키지들 중에 esm만 지원하는 녀석이 있다면, cjs/esm을 모두 지원하길. 쉽지 않군..



---
## Reference 
- https://nodejs.org/api/modules.html#modules_all_together
- https://www.typescriptlang.org/docs/handbook/module-resolution.html
- https://www.typescriptlang.org/tsconfig#moduleResolution
- https://typescript-kr.github.io/pages/module-resolution.html
- https://stackoverflow.com/questions/70296652/how-can-i-use-exports-in-package-json-for-nested-submodules-and-typescript
- https://stackoverflow.com/questions/71463698/why-we-need-nodenext-typescript-compiler-option-when-we-have-esnext
