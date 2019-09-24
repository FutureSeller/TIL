### Question
JavaScript code들을 보면 `obj.hasOwnProperty(key)` 대신 
`Object.prototype.hasOwnProperty.call(obj, key)`와 같이 쓰이는 걸 볼 수 있다.
하려고하는 일은 같은데 도대체 왜 이렇게 쓰는 걸까?

### Content
항상 위와 같은 의문을 품고 있던 도중, ESLint의 `no-prototype-builtins`를 보게 되었다.

#### Examples
> hasOwnProperty is defined on the object.

``` javascript
let object = { value: 1, hasOwnProperty: 1 };
object.hasOwnProperty(); // TypeError: object.hasOwnProperty is not a function
```

> The object doesn't inherit from Object.prototype, it doesn't have hasOwnProperty.

``` javascript
let object = Object.create(null);
object.hasOwnProperty(); // TypeError: object.hasOwnProperty is not a function
```

method가 overwrite되거나, prototype chain을 거슬러 올라갔을 때 존재하지 않을 수 있어
의도치 않은 crash를 방지하기 위함. (prototype method에 pollution이 없다고 가정)

---
## Reference
- https://eslint.org/docs/rules/no-prototype-builtins.html
- https://github.com/eslint/eslint/issues/7071#issuecomment-245377924
