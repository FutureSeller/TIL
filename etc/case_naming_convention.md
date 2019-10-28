# Case Naming Convention
***Motiv. 자꾸 헷갈려서 한 번 정리해 놓는 게 좋을 거라고 생각함***

#### Camel case
- Words are linked without spaces
- Each word begins with a **capital letter** (exception: first letter)

``` javascript
const getUserId = () => { ... };
```

#### Pascal case
- Words are linked without spaces
- Each word begins with a **capital letter**

``` javascript
const VirtualMachine = { ... };
```

#### Kebab case (= Spinal case)
- Words are in **lower case** and linked by hyphens(-)

```html
<div class=".alert-success .bg-primary"> ... </div>
```

#### Snake case (= Underscore case)
- Words are in **lower case** and linked by underscores(_)

``` c
// https://github.com/v8/v8/blob/master/src/d8/d8.cc#L211
v8::Platform* g_default_platform;
```

---
## Reference
- https://en.wikipedia.org/wiki/Naming_convention_(programming)
- https://wprock.fr/en/blog/conventions-nommage-programmation
- https://github.com/naver/yobi/blob/master/docs/ko/technical/javascript-naming-convention.md
