## Type Conversion vs Type Coercion
``` javascript
const value1 = '5'
const value2 = 9 
let coerced_sum = value1 + value2 // '59', coerced a number into a string
let conversed_sum = Number(value1) + value2 // explicitly conversed a string into a number
```

- Type Conversion = typecasting
  - 개발자에 의해 의도적으로 type을 변경
  - `Number(), String(), Boolean(), parse*(), toString() ...`
- Type Coercion
  - 자바스크립트 엔진에 의해 암묵적/자동적으로 type을 변경
  - Context-guided
    - primitive type 중 하나로 자동 변환
    - 엔진이 연산자(`+, -, *, ...`), 특정 type이 와야하는 Rule(`if(...)`)에 따라 변환
  - examples
    ``` javascript
    +''  // 0
    +'0' // 0
    +'1' // 1
    +'string' // NaN
    +NaN // NaN
    +true // 1
    +null // 0
    +undefined // NaN

    'Cat' && 'Dog' // 'Dog'
    'Cat' || 'Dog' // 'Cat
    ```

### Question
`('b' + 'a' + + 'a' + 'a').toLowerCase()`의 결과 값은?
<details><summary> example </summary><pre>

1. ('b' + 'a' + (+'a') + 'a')
2. ('b' + 'a' + 'NaN' + 'a')
3. (baNaNa).toLowerCase() // => banana

</pre></details>
- https://stackoverflow.com/questions/57456188/why-is-the-result-of-ba-a-a-tolowercase-banana  

---
## Reference
- https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion
- https://developer.mozilla.org/en-US/docs/Glossary/Type_conversion
- https://poiemaweb.com/js-type-coercion
