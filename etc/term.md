Feel free to describe any words with definition

## B
<details><summary>Backward compatibility</summary><p>

> a property of a system, product, or technology that allows for interoperability with an older legacy system, or with input designed for such a system, especially in telecommunications and computing 

https://en.wikipedia.org/wiki/Backward_compatibility
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

## T
<details><summary>TTFB</summary><p>
	
```
TTFB(Time to First Byte)
- a measurement used as an indication of the responsiveness of a webserver or other network resource.
- measures the duration from the user or client making an HTTP request to the first byte of the page being received by the client's browser.
- https://en.wikipedia.org/wiki/Time_to_first_byte
```
</p></details>

