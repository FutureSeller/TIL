## Before read this..
먼저, 아래 JSCONOf EU에서 발표된 영상을 보는 걸 추천한다. 
굉장히 이해하기 쉽고 차근차근 설명해줌.
https://www.youtube.com/watch?v=8aGhZQkoFbQ

자바스크립트는 'single threaded' 인데 event loop을 통해 concurrency를 지원할 수 있음
https://meetup.toast.com/posts/89 읽는 것을 추천한다.

---

## Motivated Example
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

<details><summary> answer </summary><p>

script start
script end
promise1
promise2
setTimeout

</p></details>

## Eventloop, Task, MicroTask

### Eventloop
- 실행되어야할 작업이 있는지, 큐를 반복적으로 확인
- 비동기 API들은 작업이 완료되면 callback을 queue에 추가
- idle할 때(call stack에 아무것도 없을 때), 특정 큐들에서 작업을 가져옴
- Task Queue
  - Web API 에서 호출한 함수를 담아놓는 Queue
  - 쉽게 말하면 나중에 실행될 callback들을 담아놓는 Queue

> An event loop has one or more task queues.
> Each event loop has a microtask queue
> task queue = macrotask queue != microtask queue

``` javascript
while(queue.waitForMessage()) {
  queue.processNextMessage();
}
```

### Microtask
- Task보다 더 높은 우선 순위를 갖는 task. 별도의 queue를 가짐
- task queue에 task가 있어도 먼저 실행됨. (e.g., Promise callback)
- 비동기 작업이 현재 실행되는 스크립트 바로 다음에 일어남
- 대기 중에 있는 task 수행보다 먼저 수행되어야할 작업이 있을 때 사용

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


### Steps
1\. task queue의 가장 오래된 작업 수행
2\. microtask queue에 들어온게 있다면 모두 실행
3\. task queue에 들어있는 다음 작업 수행 후, goto 2

``` javascript
// 1. task 실행
console.log('script start');

// 2. timer task queue에 넣음
setTimeout(function() {
  // 8. 실행
  console.log('setTimeout');
}, 0);

// 3. micro task queue에 넣음
Promise.resolve().then(function() {
  // 5. micro task 실행
  console.log('promise1');
  // 6. micro task queue 에 넣음
}).then(function() {
  // 7. micro task 실행
  console.log('promise2');
});

// 4. 1 종료 후 실행
console.log('script end');
```

---
## Reference
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop
- https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules
- https://html.spec.whatwg.org/multipage/webappapis.html#event-loops
- https://stackoverflow.com/questions/25915634/difference-between-microtask-and-macrotask-within-an-event-loop-context
- https://javascript.info/event-loop
