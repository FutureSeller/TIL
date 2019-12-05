# Map and Set

몰랐던 것, 애매하게 알고 있었던 것들을 정리하는 겸 나열

## Map

### 객체와 거의 유사한데 다른 점
몇 가지가 있는데, 알아둬야할 것만 일부 가져옴

#### Key에 **다양한 자료형을 허용함**
- 객체의 key: String and Symbol, 다른 형태일 경우 stringify 해서 저장함
- Map은 key에 자료형 제약이 없음
- Key Equality: sameValueZero
  - NaN도 Key로 동작함. 실제 JS에서 NaN === NaN은 false임
  - 커스터마이징 하는 것이 불가능함

``` javascript
let john = { name: 'John' }

// Object
let visitsCounterObj = {}
visitsCounterObj[john] = 123
console.log(visitsCounterObj) // {[object Object]: 123}
console.log(visitsCounterObj[john]) // undefined
console.log(visitsCounterObj['[object Object]']) // 123

// Map
let visitsCounterMap = new Map()
visitsCounterMap.set(john, 123)
console.log(visitsCounterMap.get(john)) // 123

```

#### Ordered Feature
- Map은 set한 순서대로 iterating, 객체는 내부적으로 정렬

``` javascript
const obj = { 3: 1, 1: 0 }
console.log(obj) // { 1: 0, 3: 1}

const map = new Map()
map.set(3, 1)
map.set(1, 0)
console.log(map) // { 3 => 1, 1=> 0 }

```

#### Object.entries and Object.fromEntries
- `Object.entries`: 객체를 맵으로

``` javascript
let obj = {
  name: "John",
  age: 30
};

let map = new Map(Object.entries(obj));

alert( map.get('name') ); // John
```

- `Object.fromEntries`: 맵을 객체로

``` javascript
let map = new Map();
map.set('banana', 1);
map.set('orange', 2);
map.set('meat', 4);

let obj = Object.fromEntries(map.entries()); // 맵을 일반 객체로 변환 (*)

console.log(map.orange) // undefined
console.log(obj.orange) // 2
```

#### Map.size
entry의 갯수를 바로 반환 해줌

### WeakMap vs. Map
- 메모리 관리 측면: GC의 대상이 될 것이냐 여부를 결정
- Map이 객체를 키로 사용한 경우, Map이 free되지 않는 한 메모리에 남아있음. (leak 가능성)

``` javascript
let john = { name: 'john' }
let map = new Map()
map.set(john, 1)

john = null
console.log(map) // { name: 'john' } => 1
```

- WeakMap은 키가 반드시 객체여야 함. primitive한 값은 키가 될 수 없음
- WeakMap은 키로 사용된 객체를 reference하는 것이 없으면 free됨

``` javascript
let john = { name: 'john' }
let wmap = new WeakMap()
wmap.set(john, 1)

john = null
console.log(wmap) // GC가 수행된 후에, {}
```

#### 특징 및 Usage
- 특징: GC에 의해 entry가 사라짐. non-deterministic함
  - 따라서, 키나 값 전체를 얻는 것 불가능
  - 단점: 한 번에 저장된 data를 얻을 수 없어 iterate 불가능
- Usage: 주로 Liveness와 큰 연관이 있음
  - 캐싱: free 된 값을 수동으로 처리해 줄 필요가 없어짐
  - 써드파티: 특정 객체가 살아 있을 때만 새롭게 추가할 데이터를 등록한다던지 등등

## Set

#### forEach가 먹힌다 + forEach의 idx 값에 value가 그대로 박힌다.
- Set을 잘 안쓰니까 몰랐다

``` javascript
set = new Set(["oranges", "apples", "bananas"]);

for (let value of set) console.log(value);

// forEach를 사용해도 동일하게 동작합니다.
set.forEach((value, valueAgain, set) => {
  console.log(value, valueAgain, set);  
});

// oranges, oranges,  {"oranges", "apples", "bananas"}
// apples, apples,  {"oranges", "apples", "bananas"}
// bananas, bananas,  {"oranges", "apples", "bananas"}
```

- `valueAgain` 즉 idx에 오는 값이 value와 같은 이유는 Map과의 호환성 때문이라고 한다.

---
## Reference
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map
- https://ko.javascript.info/map-set
- https://ko.javascript.info/weakmap-weakset