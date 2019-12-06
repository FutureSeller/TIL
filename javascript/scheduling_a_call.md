# Scheduling a call (호출 스케줄링)
일정 시간이 지난 후에 원하는 함수를 예약 실행(호출)할 수 있게 하는 것

## setTimeout
- 일정 시간이 지난 후에 함수를 실행
- 지연 간격이 보장됨: 다음 함수 호출에 대한 계획이 이전 함수의 실행이 종료된 이후에 세워지기 때문

``` javascript
/*
  @param procedure: function | string; 보통 함수를 넘김
  @param delay?: number;  millisecond 단위
  @param args: T[]; 함수에 전달할 인수들. IE9 이하에선 지원하지 않음
  @return timerId: number; 타이머 식별자
*/
let timerId = setTimeout(procedure, delay, args)

// 지연 간격에 대한 괜찮은 예시: 반복문(현재 스크립트)가 다 돈 뒤에 setTimeout 실행됨
let i = 0;
setTimeout(() => alert(i), 100); // 100000000
for(let j = 0; j < 100000000; j++) {
  i++;
}
```

#### 대기 시간이 0인 setTimeout
- 설정 방법: `setTimeout(func, 0)` 혹은 `setTimeout(func)`
- 가능한 빨리 실행 가능
  - 좀 더 자세히: 현재 스크립트 실행이 완료된 후 가능한 빠르게 함수 호출 가능
  - 지연 간격이 보장되므로, 이전 함수의 실행이 종료되어야한다는 점을 유의
- 브라우저 환경에서 실제 대기시간은 0이 아니라고 함

``` javascript
// 다섯 번째 중첩 타이머 이후엔 대기 시간을 최소 4밀리초 이상으로 강제해야 한다.
let start = Date.now();
let times = [];

setTimeout(function run() {
  times.push(Date.now() - start); // 이전 호출이 끝난 시점과 현재 호출이 시작된 시점의 시차를 기록

  if (start + 100 < Date.now()) alert(times); // 지연 간격이 100ms를 넘어가면, array를 얼럿창에 띄워줌
  else setTimeout(run); // 지연 간격이 100ms를 넘어가지 않으면 재스케줄링함
});

// 출력창 예시:
// 1,1,1,1,9,15,20,24,30,35,40,45,50,55,59,64,70,75,80,85,90,95,100
```

## clearTimeout 
취소하고 싶을 때, 타이머 식별자를 이용하여 스케줄링 취소

``` javascript
let timerId = setTimeout(() => alert("아무런 일도 일어나지 않습니다."), 1000);
alert(timerId); // 타이머 식별자

clearTimeout(timerId);
alert(timerId); // 위 타이머 식별자와 동일함 (취소 후에도 식별자의 값은 null이 되지 않습니다.)
```

## setInterval
- 일정 시간 간격을 두고 함수를 (계속) 실행
- 함수가 실행되는 시간이 지연 간격에 포함됨
  - 지연간격이 실제 명시한 간격보다 짧아짐
  - 함수를 호출할 때마다 걸리는 시간이 delay보다 길면, 모든 함수가 쉼 없이 연속 호출됨

``` javascript
/*
  @param procedure: function | string; 보통 함수를 넘김
  @param delay?: number;  millisecond 단위
  @param args: T[]; 함수에 전달할 인수들. IE9 이하에선 지원하지 않음
  @return timerId: number; 타이머 식별자
*/
let timerId = setInterval(procedure, delay, args)
```

## CPU 소비가 많은 작업을 Splitting 하기
- 브라우저: Whale
- 제약
  - 캐싱 될 여지를 없애기 위해, 브라우저를 재가동
  - Main Thread에 event handler들이 있는 newtab에서 실험
  - 현재 tab을 focusing 해둠. (background로 보내지 않음)
  - 사용자의 개입을 최소화 (어떤 이벤트도 발생시키지 않음)
  - Approch 당 3번 돌림. (최소 10번은 하고 싶긴했는데 너무 오래걸림...)

#### Baseline: 1부터 1e10까지 숫자를 세는 함수
- 걸린 시간: 107923ms
- Renderer의 Main Thread가 blocking 됨. 반복문 수행하는데 CPU를 잡아먹고 안놔주기 때문

``` javascript
let i = 0;
let start = Date.now();

function count() {
  for (let j = 0; j < 1e10; j++) {
    i++;
  }
  alert("Done in " + (Date.now() - start) + 'ms');
}

count(); // Done in 107923ms
```

#### Approach 1: recursive setTimeout
- 걸린 시간: [168354ms, 169365ms, 168650ms] ~ 168789ms
- Renderer의 Main Thread가 blocking 되지 않음
- 그런데 더 오래걸리고 들쭉날쭉 함. 실행하는 동안 다른 task에 리소스를 쓴 것 같음
  - Whale의 newtab의 작업이 영향을 끼쳤을 것이라 생각함

``` javascript
let i = 0;
let start = Date.now();

function count() {
  // 약간의 무거운 작업을 해봅시다. (*)
  do {
    i++;
  } while (i % 1e6 != 0);

  if (i == 1e10) {
    alert("Done in " + (Date.now() - start) + 'ms');
  } else {
    setTimeout(count); // 호출을 스케줄링합니다. (**) 
  }
}

count();
```

#### Approach 2: 스케줄링을 먼저 함
- 결과: [129299ms, 126957ms, 125628ms] ~ 127294ms
- Renderer의 Main Thread가 blocking 되지 않음
- Approach 1에 비해 성능 향상 (41495ms ↓). 차이점. 그리고 왜?
  - event queue에 먼저 넣어놓고, 스크립트를 실행함
  - 이거 하나만으로 생각보다 큰 차이가 나서 놀라웠음

``` javascript
let i = 0;
let start = Date.now();

function count() {
  // move the scheduling at the beginning
  if ( i < 1e10 - 1e6) {
    setTimeout(count);  
  }
  do {
    i++;
  } while (i % 1e6 != 0);
  if ( i == 1e10) {
    alert("Done in " + (Date.now() - start) + 'ms');
  }
}

count();
```

---
## Reference
- https://ko.javascript.info/settimeout-setinterval
- https://velog.io/@jakeseo_me/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%9D%BC%EB%A9%B4-%EC%95%8C%EC%95%84%EC%95%BC-%ED%95%A0-33%EA%B0%80%EC%A7%80-%EA%B0%9C%EB%85%90-10-%EC%8A%A4%EC%BC%80%EC%A5%B4%EB%A7%81-setTimeout-%EA%B3%BC-setInterval-y6juukjsey