# Async and Await

### `Async`

function 앞에 위치하며 항상 프라미스를 반환함. 프라미스가 아닌 값을 반환하더라도 resolve된 프라미스로 값을 감싸 프라미스가 반환되도록 함

```javascript
async function f() {
  return 1;
}

f().then(v => console.log(v)); // 1

async function p() {
  return Promise.resolve(1);
}
p().then(v => console.log(v)); // 1
```

### `Await`

async 함수 안에서만 동작함. 실행이 잠시 suspend되었다가 프라미스가 처리되면 실행이 재개됨

현재는 최상위 scope에서 await을 사용할 수 없지만, V8등 조만간 지원할 예정.

```javascript
async function getUserInfo() {
  const username = "FutureSeller";
  // github 사용자 정보 읽기
  let githubResponse = await fetch(`https://api.github.com/users/${username}`);
  return await githubResponse.json();
}

getUserInfo(); // Promise { pending }
getUserInfo().then(result => console.log(result)); // {login: "FutureSeller", …}
(async () => {
  const userInfo = await getUserInfo();
  console.log(userInfo); // {login: "FutureSeller", …}
})();
```

### Error Handling

- `await` with `try..catch statement` 사용
- `await` 없이 프라미스를 받고, catch로 핸들링

---

## Reference

- https://ko.javascript.info/async-await
