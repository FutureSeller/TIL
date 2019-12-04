Feel free to describe any words with definition

## A
<details><summary>Astroturfing</summary><p>

> "어떤 사안에 대해서 인기있는 풀뿌리 운동처럼 보이기 위해서 공적인 관계나 정치적인 캠페인을 이용하는 것"

- https://en.wikipedia.org/wiki/Astroturfing
- https://m.blog.naver.com/il090234/221305243665

</p></details>
<!-- delimiter -->

## B
<details><summary>Backward compatibility</summary><p>

> a property of a system, product, or technology that allows for interoperability with an older legacy system, or with input designed for such a system, especially in telecommunications and computing 

https://en.wikipedia.org/wiki/Backward_compatibility
</p></details>
<!-- delimiter -->

## C
<details><summary>Crowdsourcing</summary><p>

> '대중'(crowd)과 '외부 자원 활용'(outsourcing)의 합성어로, 전문가 대신 비전문가인 고객과 대중에게 문제의 해결책을 아웃소싱하는 것

- https://ko.wikipedia.org/wiki/%ED%81%AC%EB%9D%BC%EC%9A%B0%EB%93%9C%EC%86%8C%EC%8B%B1
</p></details>
<!-- delimiter -->

<details><summary>Crowdturfing</summary><p>

> Crowdturfing: Crowdsourcing + Astroturfing

> A relatively new spamming phenomenon that mobilizes large numbers of users to artificially boost support for, or the reputations of, companies, organizations, products, or even opinions.


> 많은 고객이 온라인 제품 리뷰 및 등급에 의존하고 온라인 평판이 구매 결정을 내리는 중요한 요소로 자리 잡고 있다. 

> 리뷰 시스템의 영향력이 증가함에 따라 제품의 리뷰를 일부러 높이거나 낮추는 허위 리뷰를 게재하여 경제적 이득을 취하려는 봇 또는 스패머도 증가하고 있다.

한국 학술지들을 보면 **집단 스팸 리뷰** 라고 보는 듯 함.

- https://www.technologyreview.com/s/528506/fake-followers-for-hire-and-how-to-spot-them/
- https://sites.cs.ucsb.edu/~ravenben/publications/abstracts/crowdturf-www12.html
- https://medium.com/@alitech_2017/countering-crowdturfing-5e37dfc90048
- https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07567552&language=ko_KR

</p></details>
<!-- delimiter -->

## D
<details><summary> Digital nomads </summary><p>

많이 듣던 단어지만 뜻을 몰라서 기억하고자 남김.

> 한국어로 "디지털 유목민". 나아가 삶을 영위하는 데에 원격 통신 기술을 적극 활용하는 사람들

> 단일한 고정된 사무실에서 일하는 전통적인 방식 대신, 외국에서, 또는 카페, 공공 도서관, 협업 공간(coworking spaces), 심지어 RV까지 포함해, 원격으로 근무하는 경우가 많다.

- https://ko.wikipedia.org/wiki/%EB%94%94%EC%A7%80%ED%84%B8_%EC%9C%A0%EB%AA%A9%EB%AF%BC
</p></details>
<!-- delimiter -->

## F
<details><summary> FOUC(Flash of unstyled content) </summary><p>

> an instance where a web page appears briefly with the browser's default styles prior to loading an external CSS stylesheet, due to the web browser engine rendering the page before all information is retrieved. The page corrects itself as soon as the style rules are loaded and applied

- 한마디로 `CSS`가 적용되지 않은 채 로딩되었다가, 적용된 페이지로 바뀜. 깜빡이는 것 처럼 보여 Flash가 들어간 것 같음
- 왜 생기는 걸까? : "the web browser engine rendering the page before all information is retrieved."
- 어떻게 해결해야 하나?
  - 문제가 되는 것(CSS, JS 등)를 `<head>`에 위치 시킴. (body를 불러들이기 전에)
  - "may choose to hide all content until it is fully loaded, at which point a load event handler is triggered and the content appears." : 이러려면 로딩 중에, UX를 위해 로딩 중이라는 걸 넣으면 좋을 듯 하다.
  - https://gist.github.com/johnpolacek/3827270
- Reference
  - https://en.wikipedia.org/wiki/Flash_of_unstyled_content
  - https://webkit.org/blog/66/the-fouc-problem/

</p></details>
<!-- delimiter -->

## G
<details><summary>Grassroots</summary><p>

한국어로: **풀뿌리 운동**

> 평범한 민중들이 지역 공동체의 살림살이에 자발적인 참여를 함으로써 지역 공동체와 실생활을 변화시키려는 참여 민주주의의 한 형태

- https://ko.wikipedia.org/wiki/%ED%92%80%EB%BF%8C%EB%A6%AC_%EB%AF%BC%EC%A3%BC%EC%A3%BC%EC%9D%98

</p></details>
<!-- delimiter -->

## M
<details><summary>Mixin</summary><p>

> a class that contains methods for use by other classes without having to be the parent class of those other classes.

``` javascript
// https://blog.seotory.com/post/2017/08/javascript-es6-use-class-and-mixin
var calculatorMixin = function ( Base ) {
	return class extends Base {
  		calc() { }
	};
}

var randomizerMixin = function ( Base ) {
	return class extends Base {
  		randomize() { }
	};
}
```

https://en.wikipedia.org/wiki/Mixin
</p></details>
<!-- delimiter -->

<details><summary>Modal Window</summary><p>

> 사용자 인터페이스 디자인 개념에서 자식 윈도에서 부모 윈도로 돌아가기 전에 사용자의 상호동작을 요구하는 창

> 응용 프로그램의 주 창의 작업 흐름을 방해

> It creates a mode that disables the main window but keeps it visible, with the modal window as a child window in front of it

> Users must interact with the modal window before they can return to the parent application

https://ko.wikipedia.org/wiki/%EB%AA%A8%EB%8B%AC_%EC%9C%88%EB%8F%84

</p></details>
<!-- delimiter -->

## P
<details><summary>POJO</summary><p>

```

POJO(Plain Old Java Object, Plain Old JavaScript Object)

the simplest kind of object that should not (in Java):
1. extend prespecified class
2. implement prespeficied interfacse
3. contain prespecified annotations

Reference: 
- https://en.wikipedia.org/wiki/Plain_old_Java_object
- https://www.geeksforgeeks.org/pojo-vs-java-beans/
```
</p></details>
<!-- delimiter -->

<details><summary>POSIX</summary><p>

> 이식 가능 운영 체제 인터페이스의 약자로, 
> 서로 다른 UNIX OS의 공통 API를 정리하여 이식성이 높은 유닉스 응용 프로그램을 개발하기 위한 목적으로 IEEE가 책정한 애플리케이션 인터페이스 규격

- https://ko.wikipedia.org/wiki/POSIX
</p></details>
<!-- delimiter -->

## S
<details><summary>SEO</summary><p>

> 웹 페이지 검색엔진이 자료를 수집하고 순위를 매기는 방식에 맞게 웹 페이지를 구성해서 검색 결과의 상위에 나올 수 있도록 하는 작업

> 검색어로 검색한 검색 결과 상위에 나오게 된다면 방문 트래픽이 늘어나기 때문에 효과적인 인터넷 마케팅 방법 중의 하나

> 기본적인 작업 방식은 특정한 검색어를 웹 페이지에 적절하게 배치하고 다른 웹 페이지에서 링크가 많이 연결되도록 하는 것

- algorithm/metric에 따라 벤더마다 다른 순위를 매겨주지 않을까.
- https://ko.wikipedia.org/wiki/%EA%B2%80%EC%83%89_%EC%97%94%EC%A7%84_%EC%B5%9C%EC%A0%81%ED%99%94
- 읽어봄직한 것들
  - https://www.twinword.co.kr/blog/what-makes-naver-seo-difficult
  - https://brunch.co.kr/@magictbl/22
  


</p></details>

## T
<details><summary>TTFB</summary><p>
	
```
TTFB(Time to First Byte)
- a measurement used as an indication of the responsiveness of a webserver or other network resource.
- measures the duration from the user or client making an HTTP request to the first byte of the page being received by the client's browser.
- https://en.wikipedia.org/wiki/Time_to_first_byte
```
</p></details>
<!-- delimiter -->
