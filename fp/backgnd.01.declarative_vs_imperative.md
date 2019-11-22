### Declarative Programming
> Declarative
>> 서술문의
>> a sentence that makes a statement or states a fact

- *Def. 어떤 방법으로 해야하는 지를 나타내기보다 무엇을 할 것인가를 설명*
  - **expresses the logic of a computation without describing its control flow.**
  - e.g., 웹페이지: "무엇"이 나타나야하는지 묘사, "어떻게" 나타내야하는지를 묘사하는 것은 아님
- *Many languages that apply this style attempt to minimize or eliminate side effects by describing what the program must accomplish in terms of the problem domain, rather than describe how to accomplish*

### Imperative Programming
> Imperative
>> 반드시 해야하는; 위엄 있는; 명령을 나타내는;
>> extremely important or urgent
>> used to describe the form of a verb that is usually used for giving orders

- 상태를 변경시키는 구문의 관점에서 연산을 기술
- 수행할 명령들을 순서대로 나열한 것

### Diff declarative vs. imperative with example
- 명령형: HOW; 선언형: WHAT;
- 결국 language가 지원해줘야하는 것 or 이를 지원하기 위한 low-level의 프로그래밍/작업이 필요해보임

``` javascript
// Imperative
function add(array) {
  let result = 0
  for (let i = 0; i < array.length; i++) {
    result += array[i]
  }
  return result
}

// Declarative
function add(array) {
  return array.reduce((prev, current) => prev + current, 0)
}

/*
  명령형
    횡단보도까지 약 99m 이동(성남대로331번길) ,
    횡단보도를 이용하여 경기성남분당경찰서 방면으로 횡단,
    횡단보도까지 1개의 횡단보도를 지나 약 612m 이동,
    횡단보도를 이용하여 메르세데스벤츠코리아더클래스효성분당전시장 방면으로 횡단,
    네이버까지 약 50m 이동(불정로).

  선언형
    출발: 경기도 성남시 분당구 성남대로 333,
    도착: 네이버 주소는 경기도 성남시 분당구 불정로 6.
*/
```

### Object-Oriented Programming (객체 지향)

---
## Reference
- https://en.wikipedia.org/wiki/Declarative_programming
- https://en.wikipedia.org/wiki/Imperative_programming
- https://codeburst.io/declarative-vs-imperative-programming-a8a7c93d9ad2
- https://tylermcginnis.com/imperative-vs-declarative-programming/
- https://stackoverflow.com/questions/1784664/what-is-the-difference-between-declarative-and-imperative-programming
- https://medium.com/@hongseongho/%EC%84%A0%EC%96%B8%ED%98%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0-1d8247342f17