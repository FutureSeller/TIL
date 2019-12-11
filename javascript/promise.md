# Promise

Callback-based 비동기 프로그래밍의 불편함을 해소하고자 나옴: 콜백 지옥(callback hell)

### Basic

```javascript
let promise = new Promise(funciton(rsolve, reject) {
  ...
})
```

- `new Promise(executor)`: { state: 'pending', result: undefined}
  - 전달되는 함수를 `executor`라고 부름
  - `executor`는 프라미스가 만들어질 때 자동으로 실행됨
  - `executor`는 둘 중에 하나를 반드시 호출해야하며, 둘 중 하나의 상태로 변경시킴. 여러 개를 호출해도 맨 앞에 호출된 것만 유효.
    - `resolve(value)`: { state: 'fulfilled', result: value }; 일이 성공적으로 끝난 경우 결과를 나타냄
    - `reject(error)`: { state: 'rejected', result: error }; 에러가 발생한 경우 에러 객체를 나타냄
  - 둘 중 하나가 처리된 상태의 프라미스는 `settled` 프라미스라고 부름
- 주의점: 프라미스 객체의 state, result 프로퍼티는 내부 프로퍼티이므로 개발자가 직접 접근할 수 없고 소비함수를 통해 접근 가능함

#### 소비함수

- `then`: 성공 및 에러를 다룸
  - 첫 번째 인자: resolved 되었을 때 실행되는 함수, 실행 결과를 받음
  - 두 번째 인자: rejected 되었을 때 실행되는 함수, 에러를 받음

```javascript
let promise = new Promise(function(resolve, reject) {
  setTimeout(() => resolve('done!'), 1000)
  // setTimeout(() => reject(new Error('error occurs')), 1000)
})

promise.then(
  result => alert(result) // 1초 후, 'done'
  error => alert(error) // UNREACHABLE
)
```

- `catch`: 에러를 다룸

```javascript
promise.then(null, error => alert(error));
promise.catch(alert);
```

- `finally`: 결과가 어떻든 마무리가 필요한 경우 쓰임

```javascript
new Promise((resolve, reject) => {}))
  .finally(() => _)
  .then(
    result => alert(result),
    error => alert(error)
  )
```

### Promise Chaning (프라미스 체이닝)

- 순차적으로 처리해야하는 비동기 작업이 여러개 있을 경우 유용함
- 가능한 이유: `promise.then`이 프라미스를 반환하기 때문

#### Example: 프라미스 반환하기

```javascript
new Promise(function(resolve, reject) {
  setTimeout(() => resolve(1), 1000);
})
  .then(result => {
    alert(result);
    return new Promise((resolve, reject) => {
      setTimeout(() => resolve(result * 2), 1000);
    });
  })
  .then(result => {
    alert(result);
  });
```

- `thenable`: `.then` 메서드를 가진 객체. 서드파티 라이브러리가 프라미스와 호환 가능한 자체 객체를 구현 가능
- 비동기 동작은 항상 프라미스를 반환하도록 하는 것이 좋음

```javascript
promise.then(f1).catch(f2); // 프라미스와 f1의 error catch 가능
promise.then(f1, f2); // f1의 error catch 안됨
```

### Error Handling

- 간단하게 말하면 `reject`로 던지고 `catch`로 받는다 (explicit)
- 실행하다가 throw 된 error를 `catch`로 받는다 (impliicit)
- 가장 가까운 에러 핸들러로 넘어감: 프라미스 체인 마지막에 catch가 있으면, 중간을 다 뛰어넘고 해당 블록으로 flow 흐름
- `unhandledrejection` 이벤트, `.catch`가 없을 때 해당 이벤트가 트리거 됨. 여기서 처리되지 않은 에러들을 핸들링하거나 확인할 수 있음

```javascript
window.addEventListener("unhandledrejection", function(event) {
  alert(event.promise); // [object Promise]; 에러를 생성하는 프라미스
  alert(event.reason); // Error 객체
});
```

### API: 5개의 정적 메서드들이 있음

#### Promise.all

- 여러 개의 프라미스를 동시에 실행시키고 모든 프라미스가 준비될 때까지 기다림
- `all` 내부에 지정된 순서에 따라 결과 값이 결정됨. 일반 값도 넣을 수 있음
- `all` 에 전달되는 프라미스 중 하나라도 거부되면, 바로 거부됨. 다른 프라미스들의 결과도 모두 무시됨. 그런데 프라미스를 취소하진 않음
- `let promise = Promise.all([...promises...])`
- 모 아니면 도일 때 유용

```javascript
Promise.all([
  new Promise(resolve => setTimeout(() => resolve(1), 3000)), // 1
  new Promise(resolve => setTimeout(() => resolve(2), 2000)), // 2
  new Promise(resolve => setTimeout(() => resolve(3), 1000)) // 3
]).then(console.log); // 1,2,3

// more practical example
const connections = [...(await getPeersByClient(client)), client];
const peersOfConnectionsPromise = connections.map(client =>
  getAllFileNames({ userId: client.id })
);
const peersOfConnections = await Promise.all(peersOfConnectionsPromise);
const files = [].concat.apply([], peersOfConnections);
```

#### Promise.allSettled

- 모든 프라미스가 처리될 때 까지 기다림: 여러 요청 중 하나가 실패해도 다른 요청 결과는 여전히 있어야 함
- 성공: `{ status: 'fulfilled', value: result }`
- 에러: `{ status: 'rejected', reason: error }`

```javascript
let urls = [
  "https://api.github.com/users/iliakan",
  "https://api.github.com/users/remy",
  "https://no-such-url"
];

/*
  results: [
    {status: 'fulfilled', value: ...응답...},
    {status: 'fulfilled', value: ...응답...},
    {status: 'rejected', reason: ...에러 객체...}
  ]
*/
Promise.allSettled(urls.map(url => fetch(url))).then(results => {
  results.forEach((result, num) => {
    if (result.status == "fulfilled") {
      alert(`${urls[num]}: ${result.value.status}`);
    }
    if (result.status == "rejected") {
      alert(`${urls[num]}: ${result.reason}`);
    }
  });
});
```

#### Promise.race

- 가장 먼저 처리되는 프라미스 결과를 반환함. 승자가 나타난 순간 다른 프라미스 결과 또는 에러는 무시됨

```javascript
Promise.race([
  new Promise((resolve, reject) => setTimeout(() => resolve(1), 1000)),
  new Promise((resolve, reject) =>
    setTimeout(() => reject(new Error("에러 발생!")), 2000)
  ),
  new Promise((resolve, reject) => setTimeout(() => resolve(3), 3000))
]).then(alert); // 1
```

#### Promise.resolve/reject

- async/await 이 후 거의 사용되지 않으나 호환성을 위해 사용해야 하기도 함
- `Promise.resolve(value)`: 주어진 값을 이용해 `fulfilled` 상태의 프라미스를 만듬
- `Promise.reject(value)`: 주어진 에러를 이용해 `rejected` 상태의 프라미스를 만듬

### Promisification (프라미스화)

- 콜백을 받는 함수를 프라미스로 변환하는 함수로 바꾸는 것
- 왜? 콜백보다는 프라미스가 더 편함

```javascript
// callback
function loadScript(src, callback) {
  let script = document.createElement('script')
  script.src = src
  script.onload = () => callback(null, script)
  script.onerror = () => callback(new Error('error'))
  document.head.append(script)
}

loadScript('/path/to/script.js', (err, script) => { ... })

// promisification: targeted function
function loadScriptPromise(src) {
  return new Promise((resolve, reject) => {
    loadScript(src, (err, script) => {
      if (err) reject(err)
      else resolve(script)
    })
  })
}

loadScriptPromise('/path/to/script.js').then(
  result: () => { ... },
  error: () => { ... }
)

// promisification: generalization with helper
function promisify(f, manyArgs = false) {
  return function(...args) {
    return new Promise((resolve, reject) => {
      function callback(err, ...results) {
        if (err) {
          return reject(err)
        } else {
          resolve(manyArgs ? results : results[0])
        }
      }
      args.push(callback)
      f.call(this, ...args)
    })
  }
}

function test(...results) {
  const [callback] = results.splice(-1)

  // 여기서 하고 싶은 작업을 수행함. 에러가 발생하면 아래 callback에서 흘림
  console.log('multiple parameters: ', results.join(','))


  callback(null, results.map(v => v * 2))

  // error를 발생시키는 경우:
  // callback('error occurs', null)
}

const f = promisify(test, true)
f(1,2,3,4).then(result => console.log(result), err => console.log(err))

// multiple parameters: 1,2,3,4
// [2,4,6,8]
// Promise {<resolved>: undefined}
```

---

## Reference

- https://ko.javascript.info/async
