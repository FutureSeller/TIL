# enum vs const enum

최근 declaration file 에 enum을 넣었을 때, 아래와 같은 에러를 뱉어주었다.

> Cannot read property 'AllowedCountries' of undefined

코드는 대략 아래와 같다.

```typescript
enum AllowedCountries {
  KR = 'KR',
  CN = 'CN',
  US = 'US'
}

console.log(AllowedCountries.KR)
```

이 때, 자바스크립트로 컴파일된 결과는 다음과 같았다.

```javascript
var AllowedCountries;
(function (AllowedCountries) {
    AllowedCountries["KR"] = "KR";
    AllowedCountries["CN"] = "CN";
    AllowedCountries["US"] = "US";
})(AllowedCountries || (AllowedCountries = {}));

console.log(AllowedCountries.KR);
```

그런데 declaration file에서는 타입을 선언만 하고 JS를 만들지 않기 때문에, AllowedCountries 는 실제 런타임에는 없는 얘나 마찬가지인 셈이다.

찾아보니 이런 문제를 겪는 개발자들이 꽤 있었고 이를 해결하기위해 아래와 같은 방법이 있었다.

```typescript
type AllowedCountries = 'KR' | 'CN' | 'US'
```

하지만 꼭 enum으로 가져가고 싶었고, `const enum`으로 만드는 방법이 있었다.

> Const enums can only use constant enum expressions and unlike regular enums they are completely removed during compilation. 
> Const enum members are inlined at use sites. This is possible since const enums cannot have computed members.


const enum의 멤버는 사용부에 인라인 되어있고, 이는  const enum은 computed member를 가질 수 없기 때문이라고 한다.

```typescript
const enum AllowedCountries {
  KR = 'KR',
  CN = 'CN',
  US = 'US'
}

console.log(AllowedCountries.KR)
console.log(AllowedCountries)
/*
'const' enums can only be used in property or index access expressions or the right hand side of an import declaration or export assignment or type query.
*/


```

```javascript
"use strict";
console.log("KR" /* KR */);
```


---
## Reference
- https://www.typescriptlang.org/docs/handbook/enums.html
- https://github.com/Microsoft/TypeScript/issues/1689
