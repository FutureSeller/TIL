# foreignObject

> The *foreignObject* SVG element includes elements from a different XML namespace. In the context of a browser, it is most likely (X)HTML.
>> 다른 네임스페이스의 요소를 포함하는 컨테이너를 만든다. 주로 HTML 요소를 삽입하는 용도로 사용된다.
  
- svg 하위에는 svg관련 xml namespace에 정의된 녀석들만 그릴 수 있는데, 아주 간혹... 정말 간혹...(알고 싶지 않았다) 하위에 html을 그려야한다.
- 이때, foreignObject로 감싸고 하위에 원하는 작업을 하면 된다.
- IE를 제외한 모든 브라우저에서 지원하고 있어서, 요런 케이스가 없길 바라지만 생기면 꼭 고려해보자.

```jsx
<foreignObject x={6} width={width} height={height}>
  <div>blahblash</div>
</foreignObject>
```

---
## Reference
- https://developer.mozilla.org/en-US/docs/Web/SVG/Element/foreignObject
