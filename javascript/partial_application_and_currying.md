## Motivated Example
#### Mission: `sum(2, 5) => sum(2)(5)` 형태로 바꿔라.
#### My Initial Approach

``` javascript
function sum(a) {
  return function(b) {
    return a + b;
  }
}

let baseTwo = sum(2);
baseTwo(5); // 7
baseTwo(7); // 9
```

해당 요구사항은 위의 작성된 함수로 문제 없다. 하지만 항상 극단적인 질문을 던져봐야한다. 
굳이 이럴 상황이 있을까 싶지만 `sum(2)(5)(1)(4)(5)(8)...`은 어떻게 구현할거에요?
계속 함수를 추가하기엔 너무 복잡해진다.

나도 모르게 작성한 위의 함수가 일종의 currying이다.

## Partial Application
- 일부 인자를 고정하며, 하나 이상의 파라메타를 받아올 수 있음
- Currying == 1-ary Partial Application으로 볼 수 도 있을 것 같음

``` javascript
// 가장 먼저 떠오른 생각은, 그냥 hard coding..
function add1(x) {
  return 1 + x;
}

// or
function add(x, y, z) {
  return x + y + z;
}

let addOne = add.bind(null, 1);
addOne(3, 4); // 8
addOne(3); // NaN
```

## Currying
> Currying is converting a single function of n arguments into n functions with a single argument each. 
> Currying always returns another function with only one argument until all of the arguments have been applied.

- 두 문구를 읽어봤을 때, 중요하다고 느낀 두 가지
 - 원하는 동작을 마무리하기까지 n 번의 call이 필요하다
 - n번의 call을 하기까지 파라메터의 순서가 매우 중요할 수 있다.
- 함수를 반환하기 때문에, 동작을 마무리하기까지 context 유지. caching/memoization 가능

``` javascript
// https://javascript.info/currying-partials#advanced-curry-implementation
function curry(func) {
  return function curried(...args) {
    if (args.length >= func.length) {
      return func.apply(this, args);  
    } else {
      return function pass(...args2) { 
        return curried.apply(this, args.concat(args2));
      }
    }
  };

}

// 약간 극단적인 예제를 만들어보자면..
function add(a, b, c, d, e, f, g) {
  return a + b + c + d + e + f + g;
}

let curried_add = curry(add);
curried_add(1)(2)(3)(4)(5)(6)(7); // 이렇게도 되고 currying
curried_add(1, 2, 3, 4)(5)(6)(7); // 이렇게도 되고 partial application
```

---
## Reference
- https://stackoverflow.com/questions/218025/what-is-the-difference-between-currying-and-partial-application
- https://codeburst.io/javascript-currying-vs-partial-application-4db5b2442be8
- https://javascript.info/currying-partials
