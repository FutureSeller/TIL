# Tag, Node, 그리고 Element

EventTarget <- Node <- Element

#### EventTarget

모든 객체가 이벤트를 받거나 리스닝할 수 있도록 정의한 인터페이스

#### Tag

HTML 문서들은 태그를 포함하지만 요소를 포함하지는 않는다. 요소는 구문 분석 단계 이후 이 태그로부터 생성된 객체이다.

#### Node

MDN을 나름 요약하자면, DOM Tree의 노드를 의미하며 추상클래스이라 서브클래스에서 동작을 명시해줘야 한다. 우리가 알만한 유명한 노드들은 Document, Element, DocumentFragment 같은 것이 있다.
(또한, Attr, CharacterData, DocumentType 등등도 있다.)
참고로 EventTarget을 부모로 두고 있다.

#### Element

Document의 모든 요소의 기본 클래스를 의미한다. 요소는 시작 태그로 신장되며 자식 컨텐츠를 포함할 수 있고 종료 태그로 종료된다.
각각 자식 요소들은 자신들이 의미하는 바가 있으며, 대표적으로 HTMLElement, SVGElement 같은 인터페이스들이 있고 각각의 기능들을 상속하는 쪽에서 명시해줘야한다.

예를 들면 `<p>` 요소는 하나의 문단을 나타내며 문단 내부의 글귀는 Text 노드이다.

---

## Reference

- https://developer.mozilla.org/en-US/docs/Web/API/EventTarget
- https://developer.mozilla.org/ko/docs/Web/API/Node
- https://developer.mozilla.org/en-US/docs/Web/API/Element
