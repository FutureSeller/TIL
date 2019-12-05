# Rest vs. Spread

## Spread **Operator**

> unpacks the collected elements into single element

> Iterable Object의 엘리먼트를 **하나 씩 분리**하여 전개한다.

위치는 크게 중요하지 않음. 쉽게 생각하면 중간중간 flat해주는 느낌

``` javascript
let prev = [3,4]
let post = [7,8]
let spreaded = [1, 2, ...prev, 5, 6, ...post, 9]
console.log(spreaded) // [1,2,3,4,5,6,7,8,9]

let spreaded2 = [1, 2, ...[[1], 2, 3]]
console.log(spreaded2) // [1,2,[1],2,3]
```

기존의 몇몇 property를 그대로 두고 특정 property의 값을 바꾼 새로운 객체를 반환할 때 주로 쓰임.
주의할 점은 shallow copy라는 것.

``` javascript
let state = {
  id: 1,
  name: 'FutureSeller',
}

let newState = {
  ...state,
  name: 'JavaScript',
}

console.log(state) // { id: 1, name: 'FutureSeller' }
console.log(newState) // { id: 1, name: 'JavaScript' }
```

## Rest **Parameter**

> a collection of all remaining elements

- Spread 연산자로 파라미터를 작성한 형태
- arguments vs. rest parameter
  - arguments는 array-like한 object여서 Array.prototype.[...] 을 사용할 수 없음
  - rest는 Array. method들을 사용할 수 있음 + arrow function에서도 사용할 수 있음
- Dynamic 하게 생성되어, length를 알 수 없음. 따라서, 함수의 length에 포함되지 않음
- 파라미터의 맨 뒤에 위치해야 함

---
## Reference
- https://jaeyeophan.github.io/2017/04/18/ES6-4-Spread-Rest-parameter/
- https://medium.com/javascript-in-plain-english/es6-spread-parameter-vs-rest-operator-5e3c924c4e1f