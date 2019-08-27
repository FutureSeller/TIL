### Description from MDN
> Generator는 빠져나갔다가 나중에 다시 돌아올 수 있는 함수입니다. 
> 이때 컨텍스트(변수 값)는 출입 과정에서 저장된 상태로 남아 있습니다.
> Generator 함수는 호출되어도 즉시 실행되지 않고, 대신 함수를 위한 Iterator 객체가 반환됩니다. 
> Iterator의 next() 메서드를 호출하면 Generator 함수가 실행되어 yield 문을 만날 때까지 진행하고, 
> 해당 표현식이 명시하는 Iterator로부터의 반환값을 반환합니다. 
> yield\* 표현식을 마주칠 경우, 다른 Generator 함수가 위임(delegate)되어 진행됩니다.
> 이후 next() 메서드가 호출되면 진행이 멈췄던 위치에서부터 재실행합니다. 
> next() 가 반환하는 객체는 yield문이 반환할 값(yielded value)을 나타내는 value 속성과, 
> Generator 함수 안의 모든 yield 문의 실행 여부를 표시하는 boolean 타입의 done 속성을 갖습니다. 
> next() 를 인자값과 함께 호출할 경우, 
> 진행을 멈췄던 위치의 yield 문을  next() 메서드에서 받은 인자값으로 치환하고 그 위치에서 다시 실행하게 됩니다.

- Iteration Protocol
  - Iterable protocol
    - JavaScript 객체가 그들의 iteration behavior를 custom할 수 있도록 해줌
    - @@iterator를 define 해야함: [Symbol.iterator] (used by for...of)
    ``` javascript
    const iterable1 = new Object();

    iterable1[Symbol.iterator] = function* () {
      yield 1;
      yield 2;
      yield 3;
    };

    console.log([...iterable1]); // [1,2,3]
    ```
  - Iterator protocol
    - value들의 sequence를 만드는 방법을 정의
    - `next` method를 가지고 있고, iterator result object: `done`, `value`가 있음
    - `next: Function`, `done: Boolean`, `value: any`
    ``` javascript
    function idMaker() {
      var index = 0;
      return {
        next: function(){
          return {value: index++, done: false};
        }
      };
    }

    var it = idMaker();

    console.log(it.next().value); // '0'
    console.log(it.next().value); // '1'
    console.log(it.next().value); // '2'
    ```

### Content: Wrap up
- 제너레이터 함수: `function*` 키워드로 작성되는 함수, 하나 이상의 yield 포함, 반환 시 제너레이터 반환
- 제너레이터
  - iterable + iterator (Symbol.iterator + next/value/done)
  - 별도로 iterator를 구현할 필요 없음

- Syntax & Example
``` javascript
// Syntax
function* name([param[, param[, ... param]]]) {
   statements
}

/***************************************************/
/* Generator: iterable + iterator: iterable에서 반환하는게 iterator */
function *gen() {
  yield 1
  yield 2
  yield 3
}

let generator = gen()
generator[Symbol.iterator]() === generator // true

/***************************************************/
function* gen(n) {
  let res;
  res = yield n;    // n: 0 ⟸ gen 함수에 전달한 인수

  console.log(res); // res: 1 ⟸ 두번째 next 호출 시 전달한 데이터
  res = yield res;

  console.log(res); // res: 2 ⟸ 세번째 next 호출 시 전달한 데이터
  res = yield res;

  console.log(res); // res: 3 ⟸ 네번째 next 호출 시 전달한 데이터
  return res;
}
const generatorObj = gen(0);

console.log(generatorObj.next());  // 제너레이터 함수 시작
console.log(generatorObj.next(1)); // 제너레이터 객체에 1 전달
console.log(generatorObj.next(2)); // 제너레이터 객체에 2 전달
console.log(generatorObj.next(3)); // 제너레이터 객체에 3 전달
```

### Summary
- iterable + iteration protocol을 준수하는 객체 (cutomized @@iterator + next/done/value)
- iterator를 반환, yield를 만나기 전까지 수행됨, context를 유지

### Usecases
<details><summary> Linear build tests for async tool </summary><pre>

``` javascript
watch({}, function* (compilation) {
  yield compilation(); // pause and wait
  t.false(fs.readdirSync('./node_modules').includes('lodash'));

  // make changes
  const packageJson = JSON.parse(fs.readFileSync('package.json', 'utf8'));
  packageJson.dependencies.lodash = '*';
  fs.writeFileSync('package.json', JSON.stringify(packageJson, null, 2));

  yield compilation(); // pause and wait
  // assert they were reflected
  t.true(fs.readdirSync('./node_modules').includes('lodash'));
  t.end();
});
```
</pre></details>

---
## Reference
- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Generator
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols
- https://poiemaweb.com/es6-generator
- https://meetup.toast.com/posts/140
- https://goshakkk.name/javascript-generators-understanding-sample-use-cases
- https://jasonhpriestley.com/array-distance-and-recursion
