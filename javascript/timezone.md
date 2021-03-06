> TOAST Meetup의 **자바스크립트에서 타임존 다루기** 를 읽고 정리한 내용입니다.

## 타임존이란?
- 동일한 로컬 시간을 따르는 지역. 주로 해당 국가에 의해 법적으로 지정됨
- 보통 국가별로 각자의 고유한 타임존을 사용하고 있음
- 면적이 넓은 나라인 경우 다른 타임존을 사용하기도 함
  - 중국의 경우 국가에서 하나의 타임존을 사용하고 있어 서쪽 지역에서는 오전 10시는 되어야 해를 볼 수 있다고 함

## GMT, UTC and Offset

#### GMT (Greenwich Mean Time)
- 경도 0도에 위치한 영국 그리니치 천문대를 기준으로 하는 태양 시간을 의미
- 1925년 2월 5일부터 사용하기 시작했고, 1972년 1월 1일까지 세계 표준시로 사용되었음
- 한국의 타임존은 GMT+09:00

#### UTC (협정 세계시; Universal Time Coordinated)
- 지구 자전주기의 흐름이 늦어지고 있는 문제를 해결하기 위해 1972년에 세슘 원자의 진동수에 기반한 국제 원자시를 기준으로 지정된 시간대
- 좀 더 정확한 시간측정을 위해 GMT를 대체하기 위해 제정된 새로운 표준; 특히 소프트웨어에서 사용할 때 더 정확한 표현일 수 있음

#### Offset
- 현재 로컬 시간의 타임존과 UTC와의 차이를 나타낸 것
- 오프셋과 타임존의 관계는 1:1이 아닌 1:N; 어떤 것을 사용하기 정하기 나름이기 때문
- 오프셋은 hour 단위가 아닐 수 있고, 분까지 고려하기도 함; 이것도 정하기 나름이라는 것
- UTC+09:00 에서 +09:00의 의미는 UTC의 기준시간보다 9시간이 빠르다는 의미
  - e.g., KST(Korea Standard Time) = UTC+09:00

## 타임존 !== 오프셋?
타임존을 단순히 오프셋이라고 지칭하기는 어려움

#### 서머 타임 (DST, Daylight Saving Time)
- 주로 영국이나 유럽, 미국, 캐나다 일부 지역 등에서 쓰이는 용어인데, 일광 시간 절약제라 불림
- 하절기에 표준시를 월래 시간보다 한 시간 앞당긴 시간으로 이용
- 캘리포니아 지역은 평소 PST(Pacific Standard Time)를 사용하고, 하절기에는 PDT(Pacific Daylight Time)를 기준시로 이용
  - 2006년 3월 31일은 PDT(-07:00)
  - 2007년 3월 31일은 PST(-08:00)

#### 타임존이 변함
- 각 지역이 어떤 타임존을 이용할 지는 해당 지역의 정치적, 경제적 이유로 변경될 수 있기 때문
- 예를 들면, 미국에서 2007년 부터 DST의 적용시점이 변경된 점

## 타임존 1 : 오프셋 N
> 한 지역의 타임존은 하나 혹은 그 이상의 오프셋을 가짐; 해당 지역의 상황에 따라 계속 달라짐

> 일상 생활에선 문제가 없지만, 시스템의 관점에서 특정 지역의 타임존을 지칭하기 위해서는 역사적으로 표준 시간대 혹은 
> DST 적용 룰이 언제 변경되었는지에 대한 데이터를 모두 갖고 있어야 함

역사적으로 표준 시간대나 DST의 변경이 동일하게 적용되었던 지역을 하나의 타임존으로 묶어서 지칭

## IANA(Internet Assigned Numbers Authority) Time Zone Database 
- tz database 혹은 tzdata라고 불리며 전 세계 모든 지역의 표준시와 DST 변경 내역을 담고 있음
- UNIX 시간(1970.01.01 00:00:00) 이후의 데이터의 정확도를 보장; 이전의 시간에 대해선 보장하진 않음
- 이름: Area / Loaction
  - Area: 대륙이나 대양명; Asia, America, Pacific 등
  - Location: 국가명 보다는 큰 도시 위주; Seoul, New_York, Tokyo
  - 예를 들면, 대한민국의 타임존은 Asia/Seoul | 일본의 타임존은 Asia/Tokyo 인데 둘 다 UTC+09:00을 표준시로 씀
- OS나 PL등 많은 시스템 들에서 이 데이터베이스를 내부적으로 사용하고 있음

#### 자바스크립트와 IANA Time Zone Database
- 과거 기본적으로는 현재 지역의 타임존을 따르게 되어있어, 명시적으로 타임존을 변경할 수 있는 방법이 없음
- 이 후, `Intl.DateTimeFormat`에서 IANA timezone을 사용하는 옵션이 추가되긴 하였음; 나중에 Intl에 대한 정리가 필요


## 서버 - 클라이언트 환경에서의 타임존

#### 시나리오
클라이언트 환경에서 사용자가 등록 페이지에서 입력박스에 일정(날짜 및 시간) 입력하면, 그 정보를 서버로 전송해서 DB에 저장된다. 
그리고 목록 페이지에서는 클라이언트가 다시 서버로부터 등록된 일정의 정보를 받아와서 화면에 보여주게 된다.

#### 주의점
- 서버에 저장된 동일한 데이터에 접근하는 클라이언트들이 서로 다른 타임존을 갖고 있을 수 있음
- 예시
  - 서울에서 2017년 3월 10일 오전 11시 30분 일정 등록
  - 뉴욕에서 조회 시, 2017년 3월 10일 오후 9시 30분이라 표시되어야 함

#### 보통의 해결방법
- **서버에 저장되는 데이터가 타임존에 영향을 받지 않는 절대값이여야 함**
- 클라이언트에서 서버에 전달하는 날짜 및 시간 정보가 동일한 오프셋에 맞추어진 값이거나, 타임존 정보까지 포함된 것
  - UTC를 기준으로 한 유닉스 시간: 1489113000
  - 오프셋 정보가 포함된 ISO-8601: 2017-03-10T11:30+09:00
- 브라우저에서 이러한 처리를 해야할 경우, 타임존에 맞게 변환해야 하고 Parsing - Formatting이 필요함  

## 자바스크립트의 `Date` 객체
- 날짜나 시간과 관련된 모든 작업을 처리하는 ECMAScript 스펙에 정의되어 있는 네이티브 객체
- mutable한 데이터이고, Month가 0으로 시작
- 내부적으로 유닉스 시간과 같은 절대값으로 시간 데이터를 관리
- 그러나 생성자나 메소드들은 모두 클라이언트의 로컬 타임존(브라우저가 실행되는 운영체제에 설정된 타임존)에 영향을 받음

#### 사용자의 입력값을 이용한 `Date` 객체 생성
- 입력 값: 2017년 3월 11일 오전 11시 30분
- Constructor
  - 년도, 월, 일, 시, 분 단위로 각각 숫자의 형태로 저장
  - 문자열 데이터: 내부적으로 Date.parse()를 호출해서 적절히 계산; 
    - 브라우저마다 상이한 결과를 낼 수도 있음
    - ECMAScript 5 부터 ISO-8601을 지원하도록 명시되어 있음
      - IE9 이상의 브라우저는 가능
      - 최신 브라우저가 아닌 경우 마지막에 Z문자가 없으면 UTC 기준으로 해석해야하는데 로컬 타임 기준에서 해석하는 경우가 있음(IE10)
  - UNIX Time: 숫자를 하나만 받을 경우 밀리초 단위의 유닉스 시간으로 인식

```javascript
const d1 = new Date(2017, 2, 11, 11, 30); // Sat Mar 11 2017 11:30:00 GMT+0900 (KST)

const d2 = new Date('2017-02-11 11:30:00'); // Sat Mar 11 2017 11:30:00 GMT+0900 (KST)

const d3 = new Date(1489199400000); // Sat Mar 11 2017 11:30:00 GMT+0900 (KST)

const d4 = new Date('2017-03-11T11:30:00'); // "Sat Mar 11 11:30:00 UTC+0900 2017"
const d5 = new Date('2017-03-11T11:30:00Z'); // "Sat Mar 11 20:30:00 UTC+0900 2017
```

#### 서버로 전달할 데이터 생성
- `getTime()`: 유닉스 시간을 얻는 방법
- `toISOString()`
  - ISO-8601 형식을 지원하며 ISO-8601 형식의 문자열을 생성할 수 있음
  - `toJSON()` 으로도 가능하여 `JSON.stringify` 시에도 적절히 변환 가능
- `toGMTString()`, `toUTCString()`을 사용할 수도 있음

```javascript
const d1 = new Date(2017, 2, 11, 11, 30);
d1.toISOString(); // "2017-03-11T02:30:00.000Z"
d1.toJSON();      // "2017-03-11T02:30:00.000Z"
```

#### 로컬 타임존 변경하기
- 다양한 타임존에서의 시간을 하나의 어플리케이션에서 동시에 보여주어야 한다거나...
- 원하는 타임존의 오프셋 값을 알고 있는 경우, 오프셋 값을 더하거나 빼서 직접 날짜를 계산할 수 있음
- `getTimeZoneOffset()`: 현재 타임존의 오프셋을 분 단위 숫자로 반환

```javascript
const seoul = new Date(1489199400000);
seoul.getTimeZoneOffset(); // -540 ;; +09:00 인데 왜 음수인지는 잘 모르겠음
```

#### 결론
- 적절히 잘 계산해서 쓰거나... 시간을 쓰기 어렵거나 검증하기 귀찮다면 moment를 쓰세요.

---
## Reference
- https://meetup.toast.com/posts/125
- https://meetup.toast.com/posts/130
