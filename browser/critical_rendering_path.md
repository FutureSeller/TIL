### Critical Rendering Path
1\. DOM(Document Object Model)
  - Byte stream => HTML Parser(tokenizing, lexing) => DOM
  
2\. CSSOM(CSS Object Model)
  - Byte stream => CSS Parser(tokenizing, lexing) => CSSOM
  - 재귀적, 하향식으로 규칙 적용 : Inheritance, Cascading
  
3\. Render Tree : DOM + CSSOM
  - DOM 트리의 루트에서 시작해, 각각을 traverse
    - head, meta 태그 등을 생략
    - CSS에 의해 숨겨지는 노드도 생략: `display:none`, 
    - `hidden`은 보이진 않지만 레이아웃에서 공간 차지
  - 표시된 각 노드에 적절하게(?) 일치하는 CSSOM 규칙을 찾아 적용
  - 표시된 각 노드를 콘텐츠 및 계산된 스타일과 함께 내보냄
  
4\. Layout == Reflow
  - 기기의 뷰포트에서 노드의 정확한 위치과 크기 계산. 즉, 배치하는 것
  - 기준점: top left
  - 렌더링 트리의 루트에서 시작해, traverse
  - 'Box Model' & 상대적인 값을 절대적인 픽셀로 변환
  
5\. Paint == Rasterize
  - 레이아웃 완료 시, 렌더링 트리의 각 노드를 화면의 실제 픽셀로 변환 후 painting

--- 

## Reference
- https://developers.google.com/web/fundamentals/performance/critical-rendering-path/constructing-the-object-model?hl=ko
