## innerHTML
> 요소(element) 내에 포함 된 HTML 또는 XML 마크업을 가져오거나 설정합니다.

`element.innerHTML = ...` : 요소의 모든 자손 제거하고 string을 파싱한 뒤 노드를 대체

#### Operational details
- 지정한 값은 HTML 또는 XML(문서 타입에 따라)로 파싱되어, DocumentFragment 객체가 새 요소에 대한 새로운 노드 DOM 노드 집합을 나타냅니다.
- 내용이 대체되는 요소가 template 요소 인 경우, template 요소의 content 속성(attribute)은 1단계에서 작성한 새  DocumentFragment 로 대체됩니다.
- 다른 모든 요소의 경우, 요소의 내용은 새 DocumentFragment 의 노드로 대체됩니다.

## outerHTML
> 요소(element)의 자식 요소를 포함하여 요소를 나타내는 직렬화된 HTML 파편을 가져옵니다. 
> 또한 주어진 문자열에서 파싱한 노드로 요소를 대체할 수 있습니다.

> 요소의 내용만을 HTML 형태로 가져오거나 설정하기 위해서는 innerHTML 속성을 대신 사용하십시오.
>> outHTML은 요소 자기 자신을 가져오기 때문

- 부모 요소가 없는 요소에 outerHTML 속성을 설정하려고 하면 변경되지 않습니다. 
- 자기 자신을 가져오기 위해, 그리고 그것을 대체하기 위해서는 부모 요소가 필요하기 때문

``` javascript
var div = document.createElement("div");
div.outerHTML = "<div class=\"test\">test</div>";
// 많은 브라우저에서 DOMException 예외를 발생시킵니다.
console.log(div.outerHTML); // 결과: "<div></div>"
```

- 또한, 문서 내의 요소가 변경되더라도 변수의 outerHTML 속성은 원본 요소를 계속 참조합니다.
- 왜 참조하는 걸까? Memory Leak은 없는 걸까?
  - https://bugzilla.mozilla.org/show_bug.cgi?id=1496701 (이게 예시가 될진 아직 잘 모르겠다)

```javascript
var p = document.getElementsByTagName("p")[0];
console.log(p.nodeName); // "P"를 출력합니다.
p.outerHTML = "<div>This div replaced a paragraph.</div>";
console.log(p.nodeName); // 여전히 "P"를 출력합니다.
```

---
## Reference
- https://developer.mozilla.org/ko/docs/Web/API/Element/innerHTML
- https://developer.mozilla.org/ko/docs/Web/API/Element/outerHTML
