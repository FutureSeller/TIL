VanillaJS와 달리 Typescript 사용 시, 실수를 정수로 만들 때 주의해야할 점이 있다.
`parseInt`의 경우, 첫 번째 파라메터의 타입이 string으로 정의되어있어 의도치 않은 에러가 발생할 수 있다.

``` javascript
let num = 101;

// 10.1
console.log(num / 10);

// error TS2345: Argument of type 'number' is not assignable to parameter of type 'string'.
// parseInt(string: string, radix?: number): number;
parseInt(num / 10, 10); 
```

아래와 같은 방법들이 있는 데, 
파라메타가 음수인 경우를 반드시 고려하여 
`Math.floor` 혹은 `toFixed`, `Math.trunc`를 적절한 의도에 맞게 사용해야 한다.
이는 VanillaJS 에서 또한 반드시 주의해야한다.

``` javascript
let num = 101;

Math.floor(num / 10);  // 10
(num / 10).toFixed(0); // 10
Math.trunc(num / 10);  // 10

let num = -101;

Math.floor(num / 10);  // -11
(num / 10).toFixed(0); // -10 
Math.trunc(num / 10);  // -10
```

---
## Reference
https://stackoverflow.com/questions/39475166/typescript-error-when-using-parseint-on-a-number
