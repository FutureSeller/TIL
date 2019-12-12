# Generators

### 제너레이터 함수

- Syntax: `function*` 으로 작성되는 함수, 하나 이상의 `yield`가 포함되어있어야함
- 제너레이터 함수를 호출하면 코드가 실행되지 않고, **제너레이터** 객체를 반환함

#### Example

```javascript
function* generateSequence() {
  yield 1;
  yield 2;
  return 3;
}

let generator = generateSequence();
generator.next(); // { value: 1, done: false }
generator.next(); // { value: 2, done: false }
generator.next(); // { value: 3, done: true }
```

### 제너레이터

- 제너레이터는 **제너레이터 함수가 반환한 객체** 임
- 제너레이터는 이터러블 그리고 이터레이션 프로토콜을 따름: 이터러블에서 반환하는 이터레이터가 자기 자신임

```javascript
generator.toString(); // [object Generator]
generator === generator[Symbol.iterator](); // true

// done: true일 경우, value를 무시하기 때문이라고 함. return을 yield로 바꾸는 방법이 있음
for (let value of generator) {
  console.log(value); // 1, 2
}
```

### 제너레이터 컴포지션(Generator Composition)

- 제너레이터 안에 제너레이터를 임베딩(embedding, composing)할 수 있게 해주는 제너레이터의 기능
- `yield* generator`: 실행을 다른 제너레이터에 위임함
  - `generator`를 대상으로 반속을 수행하고, 산출 값들을 외부 제너레이터에 의해 산출된 것 처럼 외부로 전달함

```javascript
function* generateSequence(start, end) {
  for (let i = start; i <= end; i++) yield i;
}

function* generatePasswordCodes() {
  yield* generateSequence(48, 57);
  yield* generateSequence(65, 90);
  yield* generateSequence(97, 122);
}

let generator = generatePasswordCodes();
console.log(generator.next()); // { value: 48, done: false }
// ...
console.log(generator.next()); // { value: 57, done: false }
console.log(generator.next()); // { value: 65, done: false }
// ...

console.log([...generator]); // [66, ..., 122]
```

### 제너레이터 안/밖으로 정보교환

- `yield`가 양방향 길과 같은 역할을 함: 결과를 반환하는 것 뿐만아니라 값을 제너레이터 안으로 전달하기까지 함
- `generator.next(arg)`를 호출하면 arg는 yield의 결과 값으로 반환됨

```javascript
function* gen() {
  // 질문을 제너레이터 밖 코드에 던지고 답을 기다림
  let result = yield "2 + 2 = ?"; // (*)

  // 답을 받아옴
  console.log(result);
}

let generator = gen();
let question = generator.next().value; // "2 + 2 = ?", 이 시점에서 실행이 suspend 되고 다음 next를 기다림
generator.next("asdfasdf"); // "adsfasdf"
```

### Methods

#### `generator.throw(error)`

- 외부 코드가 제너레이터에 에러를 던질 수 있도록 해줌; { done: boolean, value: any }를 반환함
- 제너레이터의 실행을 재개시키고, 제너레이터 함수의 실행 문맥속으로 에러를 주입
- 에러 핸들링은 제너레이터 내부, 외부에서 모두 가능함; 양쪽 어디에서든 핸들링하지 않으면 죽을 수 있음

```javascript
function* gen() {
  while (true) {
    try {
      yield 42;
    } catch (e) {
      console.log("Error caught!");
    }
  }
}

var g = gen();
g.next(); // { value: 42, done: false }
g.throw(new Error("Something went wrong")); // "Error caught!", { value: 42, done: false }
```

#### `generator.return(value)`

- 메서드 호출과 함께 `value`에 주어진 값을 반환하고 제너레이터를 종료시킴

```javascript
function* gen() {
  yield 1;
  yield 2;
  yield 3;
}

const g = gen();

g.next(); // { value: 1, done: false }
g.return("foo"); // { value: "foo", done: true }
g.next(); // { value: undefined, done: true }
```

### Async 이터레이터와 제너레이터

#### 이터러블 객체를 비동기적으로 만드는 방법

- `Symbol.iterator` 대신 `Symbol.asyncIterator`를 사용해야함
- `next()`는 프라미스를 반환해야함
- `for..of`가 아닌 `for await (let item of iterable)`을 사용해야함

```javascript
let range = {
  from: 1,
  to: 5,
  // for await..of 최초 실행 시, Symbol.asyncIterator가 호출됩니다.
  [Symbol.asyncIterator]() {
    // (1) Symbol.asyncIterator 메서드는 이터레이터 객체를 반환합니다.
    // 이후 for await..of는 반환된 이터레이터 객체만을 대상으로 동작하는데,
    // 다음 값은 next()에서 정해집니다.
    return {
      current: this.from,
      last: this.to,

      // for await..of 반복문에 의해 각 이터레이션마다 next()가 호출됩니다.
      async next() {
        // (2) next()는 객체 형태의 값, {done:.., value :...}를 반환합니다.
        // (객체는 async에 의해 자동으로 프라미스로 감싸집니다.)
        // 비동기로 무언가를 하기 위해 await를 사용할 수 있습니다.
        await new Promise(resolve => setTimeout(resolve, 1000));
        if (this.current <= this.last) {
          return { done: false, value: this.current++ };
        } else {
          return { done: true };
        }
      }
    };
  }
};

// TypeError: range is not iterable. (Symbol.iterator가 없어서)
// 즉, [...range]도 사용할 수 없음
for (let value of range) {
}

for await (let value of range) {
  console.log(value); // 1,2,3,4,5
}
```

#### Async 제너레이터: 제너레이터 함수 앞에 async를 붙여주면 됨. `async function* ...`

### Usecases: 페이지네이션

<details><summary> Code snippet </summary><p>

```javascript
async function* fetchCommits(repo) {
  let url = `https://api.github.com/repos/${repo}/commits`;

  while (url) {
    const response = await fetch(url, {
      headers: { "User-Agent": "Our script" }
    });

    const body = await response.json();
    console.log(response.headers.get("Link"));

    // (3) 헤더에 담긴 다음 페이지를 나타내는 URL을 추출합니다.
    let link = response.headers.get("Link");
    let nextPage = null;
    if (link) {
      nextPage = link.match(/<(.*?)>; rel="next"/);
      nextPage = nextPage && nextPage[1];
    }

    url = nextPage; // (4) 다음 페이지 url 업데이트

    for (let commit of body) {
      // (4) 페이지가 끝날 때까지 커밋을 하나씩 반환(yield)합니다.
      // (30개의 커밋을 담고 있는데, 30번째 comment를 방문하면 while 조건문으로 돌아가서 위의 과정을 반복한 뒤 yield에서 next를 하기까지 기다림)
      yield commit;
    }
  }
}

let count = 0;

for await (const commit of fetchCommits(
  "javascript-tutorial/en.javascript.info"
)) {
  console.log(commit.author.login);
  if (++count == 100) {
    // 100번째 커밋에서 멈춥니다.
    break;
  }
}

for await (const commit of fetchCommits("FutureSeller/TIL")) {
  console.log(commit.author.login);
  if (++count == 100) {
    // 100번째 커밋에서 멈춥니다.
    break;
  }
}
```

</p></details>

### Usecases: Redux Saga; https://meetup.toast.com/posts/140

---

## Reference

- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Generator
- https://meetup.toast.com/posts/140
- https://ko.javascript.info/generators
- https://ko.javascript.info/async-iterators-generators
