## Optional Chaining (Stage 3)
> nullish = [null | undefined]

아래 v8.dev의 예시를 보자.

``` javascript
// [1] error prone-version, could throw
const nameLength = db.user.name.length;

// [2] less error-prone, but harder to read
let nameLength;
if (db && db.user && db.user.name)
  nameLength = db.user.name.length;

// [3] using the ternary
const nameLength = 
  (db
    ? (db.user
      ? (db.user.name
        ? db.user.name.length
        : undefined)
      : undefined)
    : undefined);
```

`db.user.name.length`를 (에러 핸들링을 하면서) 구하기 위해 위와 같이 복잡한 코드가 양산될 수 있다.

> opional chaining: a chain of one or more property accesses and function calls, the first of which begins with the token `?.`

자바스크립트 엔진 단애서 위의 문제점을 syntactic하게 풀 수 있게 만들어주고자 제안된 proposal.
(+ falsy가 아닌 nullish를 고려함)

정의되지 않는 프로퍼티에 접근 시, throw하지 않고 undefined를 반환해줌

``` javascript
const nameLength = db?.user?.name?.length;

// validateAdminAndGetPrefs: function -> returnVal.option
// validateAdminAndGetPrefs: others -> undefined
const adminOption = db?.user?.validateAdminAndGetPrefs?.().option;

// thorws error
const adminOption = db?.user?.validateAdminAndGetPrefs().option;

function test() {
  return 42;
}
test?.(); // 42
foo?.(); // undefined

const object = { id: 123, names: { first: 'Alice', last: 'Smith' }};
const firstName = object?.names?.first; // 'Alice'
const middleName = object?.names?.middle; // undefined
}
```

---
## Reference
- https://v8.dev/features/optional-chaining
- https://github.com/TC39/proposal-optional-chaining
- https://babeljs.io/docs/en/babel-plugin-proposal-optional-chaining
