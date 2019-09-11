## Motivated Example
아래 코드의 실행 결과는?
``` javascript
console.log('script start');

setTimeout(function() {
  console.log('setTimeout');
}, 0);

Promise.resolve().then(function() {
  console.log('promise1');
}).then(function() {
  console.log('promise2');
});

console.log('script end');
```

<details><summary> 결과 </summary><p>

script start <br>
script end <br>
promise1 <br>
promise2 <br>
setTimeout <br>

</p></details>

## Run-to-Completion & Single Call Stack
- JavaScript 엔진은 Single Call Stack을 사용함 (이 관점에서 Single-threaded라고 보는 듯)
- but, 실제 구동환경(browser, node.js 등)에선 multi-threaded → 뒤에서 다뤄볼 event loop을 통해
- Run-to-Completion
  - 다른 메세지가 처리되기 전, 각각의 메세지는 완전히 처리됨
  - 메세지가 완료되기까지 너무 오래걸리면 block됨

#### Example (basic)
``` javascript
/*
  Call Stack

  [Step 1]  | [Step 2]  |  [Step 3]   | [Step 4] | [Step 5] |
            |           |             |          |          |
            |           |             |          |          |
            |   add     | console.log |          |          |
  printAdd  | printAdd  | printAdd    | printAdd |          |
-------------------------------------------------------------
*/

function add(a, b) {
  return a + b;
}

function printAdd(x) {
  let sum = add(x, x);
  console.log(sum);
}

printAdd(10);
```

#### Example with setTimeout
``` javascript
/*
  Call Stack
---------------------------------------------------------------------------------------
|  [Step 1]  |    [Step 2-4]   | [Step 5 | [Step 6] |   [Step7]   | [Step8] | [Step9] |
|            |                 |         |          |             |         |         |
|            |                 |         |          |             |         |         |
|            |                 |         |          | console.log |         |         |
| setTimeout | 위의 예제와 동일 |         |  timed   |    timed    |  timed  |         |
---------------------------------------------------------------------------------------
*/

setTimeout(funciton timed(){
  console.log('here');
}, 0);

printAdd(10);
```
- Q. setTimeout의 timed는 도대체 어떻게 저 시점에 실행 되는 것일까?
- A. Eventloop & task queue

## Task Queue
- Web API 에서 호출한 함수를 담아놓는 Queue
- 나중에 실행될 callback들을 대기 시켜놓기 위해 담아놓는 Queue

## Eventloop
- 무엇을 하는가?
  - 실행되어야할 작업이 있는지, 큐를 반복적으로 확인
  - Callback을 queue에서 가져옴
- 언제? Call Stack이 비어 있을 때

> An event loop has one or more task queues. Each event loop has a microtask queue.
>> task queue = macrotask queue != microtask queue.

``` javascript
while(queue.waitForMessage()) {
  queue.processNextMessage();
}
```

## Microtask
- 무엇? Task보다 더 높은 우선 순위를 갖는 task. 별도의 queue를 가짐
- 언제 수행? 
  - 마찬가지로, call stack이 비어 있어야 함
  - task queue에 task가 있어도 먼저 실행됨. (e.g., Promise callback)
- Usecases
  - "reacting to a batch of actions"
  - "make something async without taking the panalty of a whole new task"

``` javascript
// https://blog.bitsrc.io/microtask-and-macrotask-a-hands-on-approach-5d77050e2168

while (eventLoop.waitForTask()) {
  const taskQueue = eventLoop.selectTaskQueue();
  if (taskQueue.hasNextTask()) {
    taskQueue.processNextTask();
  }

  const microtaskQueue = eventLoop.microTaskQueue;
  while(microtaskQueue.hasNextMicrotask()) {
    microtaskQueue.processNextMicrotask();
  }
}
```

#### 예시를 다시 보자면
``` javascript
console.log('script start');

setTimeout(function() {
  console.log('setTimeout');
}, 0);

Promise.resolve().then(function() {
  console.log('promise1');
}).then(function() {
  console.log('promise2');
});

console.log('script end');

/*
  (Approximated) Call Stack & what event loop does
                                                              1. dequeue microtask queue ---
                      add to microtask queue                  2. add to microtask queue    |
                                 ∨                                          ∨              ∨
| console.log | setTimeout | Promise... | console.log | (empty stack) | promise1 cb | promise2 cb | (empty stack) | timeout cb |
                    ∧                                                                                                   ∧
             add to task queue                                                                                  dequeue task queue
*/
```

---
## Reference
- https://www.youtube.com/watch?v=8aGhZQkoFbQ
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop
- https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules
- https://html.spec.whatwg.org/multipage/webappapis.html#event-loops
- https://stackoverflow.com/questions/25915634/difference-between-microtask-and-macrotask-within-an-event-loop-context
- https://javascript.info/event-loop
